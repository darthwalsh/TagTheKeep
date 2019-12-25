import argparse
import getpass
import json
from os import path

import gkeepapi

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Labels un-labled Google Keep notes for easier searching',
        epilog='If your account uses 2FA, use a App Password')
    parser.add_argument('-u', '--username', help='Google account email')
    parser.add_argument('-l', '--label', default='NO_LABEL', help='Label to use for unlabeled notes')

    args = parser.parse_args()

    username = args.username or input('Google username: ')

    keep = gkeepapi.Keep()

    print('Logging in...')

    if path.exists('.token'):
        with open('.token', 'r') as file:
            token = file.read()
        keep.resume(username, token)
    else:
        pw = getpass.getpass('Password: ')
        keep.login(username, pw)
        token = keep.getMasterToken()
        with open('.token', 'w') as file:
            file.write(token)

    notes = keep.all()
    print(f'Fetched {len(notes)} notes...')

    unlabel = keep.findLabel(args.label, create=True)
    keep.sync()

    added = 0
    removed = 0
    for note in notes:
        labels = note.labels.all()
        other_count = sum(l.id != unlabel.id for l in labels)
        has_unlabel = note.labels.get(unlabel.id)

        if (has_unlabel and other_count):
            note.labels.remove(unlabel)
            removed += 1
            # Sync every so often to prevent big sync at end
            if not (added + removed) % 100:
                print(f'Added {added} and removed {removed} labels so far. Incremental sync...')
                keep.sync()
        elif (not has_unlabel and not other_count):
            note.labels.add(unlabel)
            added += 1
            if not (added + removed) % 100:
                print(f'Added {added} and removed {removed} labels so far. Incremental sync...')
                keep.sync()

    print(f'Added {added} and removed {removed} labels. Final Sync...')
    keep.sync()

    print('Done!')
