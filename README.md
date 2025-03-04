# **Mental Health Chatbot 🤖❤️**  

## **Overview**  
This is an AI-powered chatbot designed to provide emotional support, mental health resources, and Cognitive Behavioral Therapy (CBT)-based exercises. The chatbot uses **Natural Language Processing (NLP)** to understand user messages, analyze sentiment, and provide helpful responses.  

---

## **Features 🚀**  
- ✅ **Sentiment Analysis** – Understands user emotions and tailors responses.  
- ✅ **CBT-based Support** – Provides Cognitive Behavioral Therapy exercises.  
- ✅ **Mood Tracking** – Remembers user mood to personalize responses.  
- ✅ **Mental Health Resources** – Offers crisis hotlines and self-help guides.  
- ✅ **Interactive Web UI** – Simple chat interface using Flask and JavaScript.  

---

## **Tech Stack 🛠**  
- **Backend**: Flask (Python)  
- **Frontend**: HTML, JavaScript  
- **NLP**: VADER Sentiment Analysis  
- **Database (Optional)**: SQLite / JSON  
- **Deployment**: Docker, GitHub Actions, Cloud (e.g., Heroku, Azure)  

---

## **Project Structure 📂**  
```
📦 mental-health-chatbot
 ┣ 📂 static
 ┃ ┗ 📜 styles.css   # (Optional) Custom styles for frontend
 ┣ 📂 templates
 ┃ ┗ 📜 index.html   # Frontend chat UI
 ┣ 📜 chatbot_dataset.json  # Chatbot responses and intents
 ┣ 📜 app.py   # Flask server and chatbot logic
 ┣ 📜 requirements.txt  # Required dependencies
 ┣ 📜 README.md  # Project documentation
 ┣ 📜 .gitignore  # Ignore unnecessary files
 ┗ 📜 Dockerfile  # For containerized deployment (Optional)
```

---

## **Installation & Setup 🛠**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/mental-health-chatbot.git
cd mental-health-chatbot
```

### **2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Run the Chatbot Server**  
```bash
python app.py
```
The chatbot will run at: **http://127.0.0.1:5000/**  

---

## **Usage 🗣**  
1. Open `index.html` in a browser.  
2. Type your message in the chatbox and hit **Send**.  
3. The chatbot will analyze your input and respond with appropriate suggestions.  
4. If you're feeling down, the bot can offer **CBT exercises** and **mental health resources**.  

---

## **API Endpoints 📝**  
| Endpoint     | Method | Description |
|-------------|--------|-------------|
| `/`         | GET    | Loads the chatbot UI |
| `/chat`     | POST   | Processes user messages and returns chatbot responses |
| `/set_mood` | POST   | Stores the user's mood for personalized responses |
| `/cbt`      | POST   | Provides CBT-based guidance |
| `/resources`| POST   | Suggests mental health resources |

---

## **Deployment with Docker 🐳** (Optional)  
To run the chatbot in a Docker container:  
```bash
docker build -t mental-health-chatbot .
docker run -p 5000:5000 mental-health-chatbot
```

---

## **Contributing 🤝**  
We welcome contributions! To contribute:  
1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Added a new feature"`).  
4. Push to your branch (`git push origin feature-name`).  
5. Open a **Pull Request**.  

---

## **Acknowledgments 💡**  
- This chatbot is not a replacement for professional therapy. If you're in crisis, please seek immediate help from a licensed therapist or mental health professional.  
- Special thanks to **VADER Sentiment Analysis**, **Flask**, and **NLP libraries** that power this chatbot.  
