# VidSense: Lock in with YouTube!

<p align="center">
  <img src="https://github.com/user-attachments/assets/f6607a6e-f1b8-45b9-87f9-96153be44013" width="400" alt="VidSense Logo">
</p>

<p align="center">
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB" target="_blank">
    <img src="https://img.shields.io/github/watchers/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Watchers"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/fork" target="_blank">
    <img src="https://img.shields.io/github/forks/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Forks"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Stars"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Issues"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/pulls" target="_blank">
    <img src="https://img.shields.io/github/issues-pr/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Pull Requests"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/blob/master/LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="License" />
  </a>
</p>

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

VidSense is a browser extension that provides instant answers and concise summaries based on the YouTube video you're watching. It offers AI-powered responses directly within your current tab, enhancing your video-watching experience.

## Key Features

### Question-Answering
VidSense uses YouTube video captions to provide accurate and contextually relevant answers to user queries. This feature allows users to quickly find precise information without watching the entire video.

### Summarization
Get concise summaries of YouTube videos to grasp the main points and essential information quickly. This feature helps users efficiently access key ideas without watching the full content.

### Additional Prompts
The question-answering tab also supports any other prompts such as "Generate a quiz" or "Translate to Hindi", further enhancing the utility of the extension.

## Technologies Used

- Frontend: HTML/CSS/JavaScript
- Backend: Flask
- AI Integration: Google Gemini
- Containerization: Docker
- API Integration: MindsDB

## Installation

### Download the Latest Release

1. Download the latest release [here](https://github.com/apoorvsxna/VidSense-MindsDB/releases).
2. Extract the files to your preferred location.

### Backend Setup

1. Install [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/).
2. Set up MindsDB on Docker following this [guide](https://docs.mindsdb.com/setup/self-hosted/docker-desktop).
3. Open the SQL editor in the MindsDB extension and run the following queries:

   ```sql
   CREATE ML_ENGINE google_gemini_engine
   FROM google_gemini
   USING
         google_gemini_api_key = 'your-api-key';

   CREATE MODEL google_gemini_model
   PREDICT answer
   USING
         engine = 'google_gemini_engine',
         column = 'question',
         model = 'gemini-pro';

4. Download and install [Python](https://www.python.org/downloads/). Skip this step if it is already installed on your computer.

5. Run the `install-dependencies.bat` file in the extracted folder.

### Extension Setup

1. Enable Extension developer mode in your browser.
2. Click on "Load Unpacked" and select the extension folder from the extracted files.
3. The VidSense extension will now be available in your browser's extensions menu.

## Usage

1. Make sure the MindsDB Docker container is running
2. Start the server by running `start.bat`.
3. Navigate to a YouTube video.
4. Click the VidSense extension icon to open the interface.
5. Use the summary or question-answering features as needed.
6. Stop the server using `stop.bat` when finished.


## Demo
(Click to watch on YouTube)

[![Demo Video](https://img.youtube.com/vi/ajPk465WY4E/0.jpg)](https://www.youtube.com/watch?v=ajPk465WY4E)

## Screenshots

### Question-Answering:

![Screenshot (32)](https://github.com/user-attachments/assets/a3d9b41f-21f7-4300-b39b-fae9cc7bf0aa)


### Summarization:

![summary](https://github.com/user-attachments/assets/036f5447-4e3a-4b83-8147-c1c8a3395b12)


### Additional prompt using Question-Answering (Quiz):

![quiz](https://github.com/user-attachments/assets/084883fb-f7d5-4eae-a7bf-73b1ce01725a)


## Contributing

If you'd like to contribute, please follow these steps:

1. **Fork the repository**
2. **Create your feature branch**:

   ```bash
   git checkout -b your-name/feature
   ```

3. **Commit your changes**:

   ```bash
   git commit -m 'Add some feature'
   ```

4. **Push to the branch**:

   ```bash
   git push origin your-name/feature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [MindsDB](https://docs.mindsdb.com/what-is-mindsdb) for AI Data automation
- [Google Gemini API](https://ai.google.com/gemini) for LLM tasks
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) for the backend framework
- [Docker](https://www.docker.com/) for containerization
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) for extracting YouTube captions.
---
