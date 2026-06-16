# using-rest-api
I created a chatbot using GROQ_API_KEY

# Groq AI Chat Application

A Python-based AI chat application powered by the Groq API.

## Features

* Connects to Groq LLMs
* Interactive chat interface
* Environment variable support for API keys
* Simple and lightweight implementation

## Requirements

* Python 3.9 or higher
* Groq API key

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install groq python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Run the application:

```bash
python app.py
```

## Example Code

```python
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
)

print(response.choices[0].message.content)
```

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── venv/
```

## Dependencies

```text
groq
python-dotenv
```

## Troubleshooting

### NameError: name 'Groq' is not defined

Make sure you have imported Groq:

```python
from groq import Groq
```

and installed the package:

```bash
pip install groq
```

### Invalid API Key

Verify that your `.env` file contains a valid Groq API key:

```env
GROQ_API_KEY=your_api_key
```

## License

MIT License

