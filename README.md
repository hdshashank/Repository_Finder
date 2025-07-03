# Random GitHub Repository Finder

A Flask web application for discovering random GitHub repositories by programming language. Built as a learning project to understand Flask fundamentals, templating, and API integration.

## 🎯 Learning Objectives

This project demonstrates:

- **Flask Basics**: Setting up routes, handling GET/POST requests
- **Flask Templating**: Using Jinja2 templates with conditional rendering
- **API Integration**: Making HTTP requests to GitHub's REST API
- **Form Handling**: Processing user input and maintaining state
- **Error Handling**: Managing API failures and edge cases
- **Frontend Integration**: Combining Flask with Bootstrap for responsive design

## 🌟 Features

- **Language-based Search**: Find repositories by specifying any programming language
- **Random Discovery**: Get a random repository from the top 100 most starred repositories
- **Find Another**: Discover multiple repositories of the same language without re-entering it
- **Repository Details**: View name, description, language, star count, and direct GitHub link
- **Responsive Design**: Beautiful UI that works on desktop, tablet, and mobile devices

## 🚀 Demo

![Random GitHub Repository Finder](/screenshots/demoScreenshot_1.png)
![Random GitHub Repository Finder](/screenshots/demoScreenshot_2.png)

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap
- **API**: GitHub REST API v3
- **Dependencies**: requests, flask

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/hdshashank/RepoFinder.git
   cd RepoFinder
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies from `requirements.txt`**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open your browser**  
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### GitHub API Rate Limits

The application uses GitHub's public API without authentication, which has the following limits:

- 60 requests per hour per IP address
- For higher limits, you can add GitHub token authentication

### Search Parameters

The application searches for repositories with these parameters:

- **Sort**: By stars (most starred first)
- **Order**: Descending
- **Per page**: 100 repositories
- **Selection**: Random choice from results

## 🚦 API Endpoints

| Method | Endpoint        | Description                                  |
| ------ | --------------- | -------------------------------------------- |
| GET    | `/`             | Display the main page                        |
| POST   | `/`             | Search for repositories by language          |
| POST   | `/find-another` | Find another repository of the same language |

---
