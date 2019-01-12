chrome.runtime.onInstalled.addListener(() => {
  chrome.declarativeContent.onPageChanged.removeRules(undefined, () => {
    chrome.declarativeContent.onPageChanged.addRules([
      {
        conditions: [
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { hostEquals: 'keep.google.com', schemes: ['https'] },
          })
        ],
        actions: [ new chrome.declarativeContent.ShowPageAction() ],
      }
    ]);
  });
});

chrome.pageAction.onClicked.addListener(tab => {
  chrome.tabs.executeScript(tab.id, {file: "filter.js"});
})
