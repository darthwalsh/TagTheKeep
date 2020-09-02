# TagTheKeep

Do you wish Google Keep gave you the option to search for un-labled notes, [like][1] [these][2] [requests][3]?

You can use this script to create the label `NO_LABEL` which allows you to easily find all un-labed notes. Each time you run it, it will loop through all your notes and assign the `NO_LABEL` label for all un-labeled notes, and remove the `NO_LABEL` label if there is also another label.

## How to use

    git clone https://github.com/darthwalsh/TagTheKeep.git
    cd TagTheKeep
    python3 -m pip install gkeepapi

    python3 main.py -u sally

Visit https://keep.google.com/#label/NO_LABEL and add labels or archive notes. No need to remove `NO_LABEL`, just run again:

    python3 main.py -u sally

### Dependencies:

Uses [`gkeepapi`](https://github.com/kiwiz/gkeepapi) to interact with Google Keep.

### Help

```
usage: main.py [-h] [-u USERNAME] [-l LABEL]

Labels un-labled Google Keep notes for easier searching

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Google account email
  -l LABEL, --label LABEL
                        Label to use for unlabeled notes. Default: 'NO_LABEL'
  -a, --include_archived
                        include all notes, instead of notes not archived

If your account uses 2FA, use a App Password
```

So if your email is sally@gmail.com, then run:

    python3 main.py -u sally

and at the prompt type your account password.

After the first time you run it, a `.token` file is created that contains an auth token that gives permission to your entire Google account, so future runs to not need a password. Delete this if you are worried about security.

## 2FA needs App Password

If you use 2FA on your Google account (which you should!) then you will need an extra step or you will get the error:

    gkeepapi.LoginException: ('NeedsBrowser', 'To access your account, you must sign in on the web.

Create a [Google App Password](https://myaccount.google.com/apppasswords) and use that as your password in the script.

[1]: https://webapps.stackexchange.com/questions/88648/hide-work-google-keep-items-on-the-weekend
[2]: https://www.quora.com/How-do-you-show-only-notes-with-no-label-in-Google-Keep
[3]: https://webapps.stackexchange.com/questions/80509/google-keep-search-options
