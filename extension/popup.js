document.addEventListener('DOMContentLoaded', function () {
  var answerButton = document.getElementById('answerButton');
  var summarizeButton = document.getElementById('summarizeButton');
  var questionInput = document.getElementById('questionInput');
  var outputElement = document.getElementById('output');
  var loader = document.getElementById('loader');

  // Listen for "Enter" key press in the input box
  questionInput.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') {
          handleAnswerButtonClick();
      }
  });

  answerButton.addEventListener('click', handleAnswerButtonClick);

  summarizeButton.addEventListener('click', function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
          var activeTab = tabs[0];
          showLoader();
          chrome.tabs.sendMessage(activeTab.id, { action: "summarize", video_url: activeTab.url });
      });
  });

  function handleAnswerButtonClick() {
      var question = questionInput.value;
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
          var activeTab = tabs[0];
          showLoader();
          chrome.tabs.sendMessage(activeTab.id, { action: "answer", question: question, video_url: activeTab.url });
      });
  }

  // Function to show the loading animation
  function showLoader() {
      loader.style.display = 'block';
      outputElement.style.display = 'none';
  }

  // Function to hide the loading animation and display the output
  function hideLoader() {
      loader.style.display = 'none';
      outputElement.style.display = 'block';
  }

  // Function to display output in the popup
  function displayOutput(output) {
      hideLoader();
      outputElement.textContent = output;
  }

  // Listen for messages from the content script
  chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
      if (request.output) {
          displayOutput(request.output);
      }
  });
});
