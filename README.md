# 🤖 AI Code Assistant for Students

## 📌 Project Overview

AI Code Assistant for Students is a web-based programming assistant designed to help students with common programming tasks.

The application provides code generation, code explanation, Python syntax debugging, test case generation, code copying, code downloading, and support for Python, Java, and C++.

## 🎯 Objectives

* Help beginners generate programming code easily.
* Explain programming code in simple language.
* Identify Python syntax errors.
* Generate basic test cases.
* Support multiple programming languages.
* Provide a simple and user-friendly interface.
* Help students practice programming concepts.

## ✨ Features

### 💻 Code Generation

Generate basic programming solutions for Python, Java, and C++.

### 📖 Code Explanation

Provides a simple explanation of the generated code.

### 🐞 Code Debugging

Checks Python code for syntax errors using Python's AST parser.

### 🧪 Test Case Generation

Generates sample test cases for common programming problems.

### 📋 Copy Code

Allows users to copy generated code quickly.

### ⬇️ Download Code

Allows users to download generated code in the appropriate file format.

### 🌙 Dark Mode

Provides a dark-mode interface for comfortable viewing.

### 📚 Code History

Stores the latest programming questions during the application session.

### 📱 Responsive Design

The interface adapts to desktop, tablet, and mobile screen sizes.

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Python AST
* Jinja2

## 📂 Project Structure

```text
AI-Code-Assistant/
│
├── app.py
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## ⚙️ Installation

### 1. Clone or download the project

Open the project folder in Visual Studio Code.

### 2. Install required packages

```bash
pip install flask python-dotenv openai
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in a browser

Open:

```text
http://127.0.0.1:5000
```

## 🔐 Security

The `.env` file should not be uploaded to public repositories.

API keys and other secret credentials should always remain private.

## ⚠️ Current Limitations

* Code generation currently uses predefined rule-based programming examples.
* Debugging checks Python syntax rather than executing the submitted program.
* The application does not execute arbitrary user code on the server.
* The code generator supports a selected set of common programming problems.

## 🚀 Future Enhancements

* Integration with a live AI model.
* Support for additional programming languages.
* Advanced code debugging.
* Automatic code optimization.
* User accounts and saved projects.
* Online code execution using a secure sandbox.
* More advanced test-case generation.
* Personalized learning recommendations.

## 🎓 Academic Purpose

This project is developed as a student-oriented programming assistance application. It demonstrates concepts of web development, Python programming, Flask, frontend design, code analysis, and software engineering.

## 👨‍💻 Project

**AI Code Assistant for Students**

Developed as an academic project.
