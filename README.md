# To-Do List with AI Chatbot

A **modern, interactive To-Do List application** with an **AI Chatbot** for enhanced functionality. Built using **Python**, **customtkinter**, and **OpenAI's GPT-3.5 Turbo**, this application provides an intuitive task management system with a sleek dark-themed UI.

---

## 🚀 Features

✅ **Modern UI** - Built with `customtkinter` for a stylish dark mode theme.  
✅ **Task Management** - Add, delete, and mark tasks as done.  
✅ **AI Chatbot** - Ask the AI chatbot questions within the app.  
✅ **Emoji Indicators** - ✅ (Done), ❌ (Not Done) for better visualization.  
✅ **Persistent Tasks** - Saves tasks in a text file (`To-Do-List.txt`).

---

## 📌 Installation

### **1️⃣ Install Dependencies**
Make sure you have Python installed. Then, install the required libraries:

```bash
pip install customtkinter openai
```

### **2️⃣ Set OpenAI API Key**
To enable the AI chatbot, set your OpenAI API key in the environment variables:

```bash
export OPENAI_API_KEY="your-api-key"  # Mac/Linux
set OPENAI_API_KEY=your-api-key  # Windows
```

Alternatively, you can replace `api_key = os.getenv("OPENAI_API_KEY")` in the script with:

```python
api_key = "your-api-key"
```

---

## 🎮 Usage

### **Running the Application**
```bash
python todo_ai.py
```

### **Basic Functions:**
- **Add Task:** Type in a task and press `Add Task`.
- **Mark Done:** Select a task and click `Mark Done`.
- **Delete Task:** Select a task and click `Delete`.
- **Ask AI Chatbot:** Enter a query in the chatbot field and click `Chat`.

---

## 🛠️ Technologies Used
- **Python** (Programming Language)
- **CustomTkinter** (Modern UI Framework)
- **OpenAI GPT-3.5 Turbo** (AI Chatbot)
- **Pyttsx3** (Optional: Text-to-Speech)

---

## 📸 Screenshots
![To-Do List with AI](https://github.com/Dahire100/TO-Do-List/blob/main/Screenshot%20.jpg)

---

## 🏆 Contributing
Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!

---

## 📜 License
This project is **open-source** under the MIT License.

---

## 📧 Contact
For any questions, feel free to reach out via [GitHub](https://github.com/your-profile) or email at `your-email@example.com`.

---

🚀 **Enjoy managing your tasks efficiently with AI!** 🎉

