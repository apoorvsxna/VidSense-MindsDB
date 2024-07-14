// background.js
chrome.browserAction.onClicked.addListener(function(tab) {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      var activeTab = tabs[0];
      chrome.tabs.sendMessage(activeTab.id, { action: "answer", question: "Your question here", video_url: activeTab.url });
    });
  });
  
  chrome.runtime.onInstalled.addListener(function() {
    chrome.contextMenus.create({
      title: "Summarize",
      contexts: ["browser_action"],
      onclick: function() {
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
          var activeTab = tabs[0];
          chrome.tabs.sendMessage(activeTab.id, { action: "summarize", video_url: activeTab.url });
        });
      }
    });
  });
  