# LinGine – A Linux AI Assistant for the Command Line

LinGine (Linux + Engine) is an AI-powered assistant designed to help Linux users—especially beginners—interact with the terminal more effectively. With natural language input and intelligent command generation, LinGine bridges the gap between everyday language and complex shell commands. It is deployed using Streamlit for an easy-to-use web interface.

## 🔧 Features

* 🧠 AI-powered natural language to shell command conversion
* 💡 Explains commands before execution
* 🎯 Error handling with suggestions
* 🖥️ Clean and responsive Streamlit interface
* 🔁 Copy-paste and command history functionality
* 💬 Lightweight chatbot mode for interactive Linux help

## 🚀 Demo

You can try the live demo here (replace with your Streamlit Cloud link or localhost instructions):

```bash
streamlit run app.py
```

## 📦 Tech Stack

* Python
* Streamlit
* OpenAI/GPT API or local LLM (optional)
* subprocess, os, platform
* Linux CLI

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Mounishkr/LinGine---A-Linux-AI-assiant-for-CTL.git
cd LinGine---A-Linux-AI-assiant-for-CTL
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

## 🧠 How It Works

* User types a query in natural language (e.g., “how do I list all files including hidden ones?”)
* LinGine uses an LLM to interpret the intent and generates the correct shell command (e.g., ls -a)
* The command is explained in simple terms and optionally executed on the user’s system (if enabled)

## ⚠️ Disclaimer

This tool can execute shell commands on your system. Please review commands carefully before running them.

## 📄 License

MIT License. See LICENSE for details.

## 🙌 Credits

Built with ❤️ by Mounish. Special thanks to the open-source Linux and AI communities.
