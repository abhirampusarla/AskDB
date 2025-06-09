# 🗣️ AskDB – Talk to Your Database with Natural Language

**AskDB**  is a **Generative AI-powered tool** that lets you interact with your MySQL database using plain English—no SQL required. Leveraging Google Gemini, LangChain, and Gradio, AskDB brings the power of conversational AI to data access, enabling seamless, natural interaction with structured data.

At its core, AskDB uses Generative AI via Gemini to understand your questions, generate SQL queries, and deliver accurate results from your database—all in real-time. Whether you're asking “What are the top courses offered this semester?” or “List all instructors with salaries above $100K,” AskDB intelligently converts your input into valid SQL using LangChain’s structured prompt chains.

With a lightweight setup and an intuitive Gradio web interface, AskDB is perfect for:

Business analysts who need insights without writing SQL
Students and educators exploring database concepts
Developers and data scientists building rapid AI prototypes
Anyone who wants to bring Generative AI to relational data

**AskDB includes:**

📊 Natural language to SQL translation via Generative AI.

⚙️ MySQL backend support for live querying.

🧠 Intelligent SQL extraction and safety filtering.

🌐 Easy-to-use browser interface for asking questions and viewing results.

By combining **LLM capabilities**, **prompt engineering**, and **real-time execution**, AskDB transforms traditional database interaction into a Generative AI experience. It empowers users to ask, explore, and discover data insights with the ease of a conversation.

With AskDB, Generative AI meets SQL, turning complex data exploration into a smooth, code-free experience.

---

## Project Structure

├── AskDB.py # Main app logic: LLM, query extraction, Gradio UI

    ├── Connecting to Google API.py # Gemini API key setup and integration
        ├── DB Connection Check.py # MySQL DB connection checker
            ├── requirements.txt # Dependencies
└── README.md # Documentation

---

## Installation

### **1. Clone the Repository**

git clone https://github.com/abhirampusarla/AskDB.git

cd AskDB

### **2. Install Requirements**

pip install -r requirements.txt





## API Key Setup

AskDB uses Google Gemini for converting natural language into SQL.


### Option 1: Set API key in environment
export GOOGLE_API_KEY="your_api_key_here"
### Option 2: Use a .env file
Create a .env file in the root directory:

GOOGLE_API_KEY=your_api_key_here


## Database Configuration

Update your MySQL connection details in DB Connection Check.py and AskDB.py:

host='localhost'

user='root'

password='your_password'

database='your_database'

Run DB Connection Check.py to confirm the connection:

### python "DB Connection Check.py"

## 🚀 Running the App

Launch the app via:

### python AskDB.py
