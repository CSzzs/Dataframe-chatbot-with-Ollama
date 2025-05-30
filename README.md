# Dataframe Chatbot with Ollama

A Streamlit-based chatbot that allows users to interact with their data using natural language queries. The application uses Ollama's Gemma model and LangChain to enable conversational analysis of CSV and Excel files.

## Features

- 📊 Upload and analyze CSV and Excel files
- 💬 Natural language interaction with your data
- 🤖 Powered by Ollama's Gemma 3B model
- 📈 Live data preview functionality
- 💾 Persistent chat history during session

## Requirements

- Python 3.11+
- Ollama installed and running locally
- Required Python packages:

```txt
ollama==0.3.0
langchain==0.2.10
langchain-community==0.2.9
langchain-experimental==0.0.62
langchain-ollama==0.1.0
pandas==2.2.2
openpyxl==3.1.5
tabulate==0.9.0
streamlit==1.45.1
```

## Installation

1. Clone the repository:
```bash
git https://github.com/CSzzs/Dataframe-chatbot-with-Ollama
cd Dataframe-chatbot-with-Ollama
```

2. Create a virtual environment:
```bash
python -m venv DFchatbot
```

3. Activate the virtual environment:
- Windows:
```bash
DFchatbot\Scripts\activate
```
- Linux/Mac:
```bash
source DFchatbot/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure Ollama is running locally with the Gemma model installed

2. Start the Streamlit app:
```bash
streamlit run src/main.py
```

3. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

4. Upload your CSV or Excel file using the file uploader

5. Start asking questions about your data in natural language!

## How It Works

1. The application uses Streamlit for the web interface
2. Users can upload CSV or Excel files which are converted to pandas DataFrames
3. The LangChain framework creates a pandas DataFrame agent that can interpret natural language queries
4. Queries are processed using the Ollama Gemma model
5. Results are displayed in a chat-like interface with markdown formatting

## Limitations

- Currently supports only CSV and Excel file formats
- Requires local installation of Ollama
- Processing time depends on the size of the dataset and complexity of queries

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
