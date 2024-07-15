# VidSense: Lock in with YouTube!

<p align="center">
  <img src="https://github.com/user-attachments/assets/f6607a6e-f1b8-45b9-87f9-96153be44013" width="400" alt="eye">
</p>

<p align="center">
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB" target="blank">
    <img src="https://img.shields.io/github/watchers/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Watchers"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/fork" target="blank">
    <img src="https://img.shields.io/github/forks/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Forks"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/stargazers" target="blank">
    <img src="https://img.shields.io/github/stars/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Star"/>
  </a>
</p>
<p align="center">
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/issues" target="blank">
    <img src="https://img.shields.io/github/issues/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Issues"/>
  </a>
  <a href="https://github.com/apoorvsxna/VidSense-MindsDB/pulls" target="blank">
    <img src="https://img.shields.io/github/issues-pr/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="Open Pull Request"/>
  </a>
</p>
<p align="center">
  <a href="https://github.com/apoorvsxna/VidSense-MindsDBblob/master/LICENSE" target="blank">
    <img src="https://img.shields.io/github/license/apoorvsxna/VidSense-MindsDB?style=for-the-badge&logo=appveyor" alt="License" />
  </a>
</p>

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Installation](#installation)
  - [Frontend Setup](#frontend-setup)
  - [Backend Setup](#backend-setup)
- [Usage](#usage)
- [Demo](#demo)
- [Technical Demo](#technical-demo)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

> _And you run and you run, to catch up with the sun but it's sinking,_
> 
> _Racing around to come up behind you again._
>
> _Sun is the same, in a relative way, but you're older_
> 
> _Shorter of breath and one day closer to death_
> 
> _-Pink Floyd_

**VidSense** is a powerful extension for instant answers and concise summaries based on the YouTube video you're watching, all within your current tab. Precise AI-powered answers a click away!

## Key Features

### Question-Answering
The Vidsense Q&A feature leverages YouTube video captions to provide accurate and contextually relevant answers to user queries. This innovative functionality enhances the browsing experience by allowing users to tap into the vast repository of knowledge embedded in YouTube videos, utilizing the power of captions to quickly find precise information.By utilizing YouTube video captions for precise answers, this feature significantly decreases the time users spend searching for information, providing quick and accurate responses directly from video content.

### Summarization
The Summarization feature provides concise summaries of YouTube videos, allowing users to quickly grasp the main points and essential information without watching the entire content. By integrating this Summarization feature, users can efficiently access the main ideas and key points from YouTube videos, drastically reducing the time required to consume and comprehend video content.

### Quiz Generation
The Quiz Creation feature utilizes the Q&A capabilities to generate interactive quizzes from YouTube video content. This feature extracts key information from video captions and formulates questions, offering users a dynamic way to test their understanding and retention of the material. You can also use other similar feauture via other gemini prompts in the extension.

## Technologies Used

- **Frontend**: HTML/CSS
- **Backend**: Flask
- **AI Integration**: Google Gemini
- **Containerization**: Docker
- **API Integration**: MindsDB

## Getting Started

To get started with CarePlus, you'll need to set up both the frontend and backend components of the application.

## Installation

### Clone the Repository

```bash
git clone https://github.com/apoorvsxna/VidSense-MindsDB.git
```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd CarePlus/frontend
   ```

2. Install dependencies:

   ```bash
   yarn install
   ```

3. Start the development server:

   ```bash
   yarn run dev
   ```

### Backend Setup

1. Ensure you have Docker installed on your system and RUNNING. Windows users may install Docker Desktop.

2. Navigate to the backend directory:

   ```bash
   cd CarePlus/backend
   ```

3. Setting up a virtual environment (recommended):

   - Install virtualenv:

     ```bash
     pip install virtualenv
     ```

   - Create a virtual environment:

     ```bash
     virtualenv venv
     ```

   - Activate the virtual environment:
     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

     - On macOS and Linux:

       ```bash
       source venv/bin/activate
       ```

4. Initialize Policies folder as a Git repository (For Opal configuration):

   ```bash
   cd policies
   git init
   git add .
   git commit -m "Initial commit"
   cd ..
   ```

5. Create a `.env` file in the backend directory with the following content:

   ```
   DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=thiswillalsowork
   OPAL_SERVER_URL=http://opal_server:7002
   OPA_SERVER_URL=http://opa:8181
   API_KEY=YOUR_GEMINI_API_KEY
   ```

   Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

6. Build and start the Docker containers from backend directory (this may take a few minutes):

   ```bash
   docker compose up --build
   ```

   For subsequent runs, you can simply use:

   ```bash
   docker compose up
   ```

   To stop the containers:

   ```bash
   docker compose down
   ```

## Usage

1. Ensure the extension updated to the latest version.
2. Choose a YouTube video.
3. Click on the extension icon in the top right corner to open summary.
4. For summary:
   - click on the summary button.
   - Wait for summary generation.
   - Have read at a consise summary of the video.<br>
For Question-Answering:
   - Enter your prompt in the text box.
   - Click on the Answer button.
   - Get you queries done on the go.
6. You may use these features howerever you want. The prompts can be tampered for your purpose.


## Demo

[Click here to watch the demo video](https://github.com/apoorvsxna/VidSense-MindsDBassets/89499267/d24c8ff7-2614-414b-b85f-5ef1a7979360)

## Technical Demo

[Click here to watch the technical demo video](https://github.com/apoorvsxna/VidSense-MindsDBassets/89499267/c0823003-73ff-4b60-babc-b5daa3b38882)

## Screenshots

Landing Page:
Q&A Interaction:
Quiz Creation:
Summary View:

## Contributing

We welcome contributions to CarePlus! If you'd like to contribute, please follow these steps:

1. **Fork the repository**
2. **Create your feature branch**:

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit your changes**:

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the branch**:

   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [MindsDB] for easy api integration
- [Google Gemini API](https://ai.google.com/gemini) for AI-powered symptom analysis
- [HTML/CSS]([https://reactjs.org/](https://developer.mozilla.org/en-US/)) for the frontend framework
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) for the backend framework
- [Docker](https://www.docker.com/) for containerization

---
