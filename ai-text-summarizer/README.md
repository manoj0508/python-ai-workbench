# AI Text Summarizer

A Streamlit app that summarizes text with the OpenAI API through LangChain.

## Project structure

```text
ai-text-summarizer/
├── app.py                   # Streamlit interface for entering text and viewing summaries
├── summarizer.py            # API key loading, prompt creation, and summary chain
├── config/
│   ├── .gitkeep             # Keeps the config directory in Git
│   └── openAPI.txt          # Create locally; contains your private OpenAI API key
├── requirements.txt         # Python dependencies
└── README.md                # Project instructions
```

## Requirements

- Python 3
- An OpenAI API key

## Setup and run

Run these commands from the `ai-text-summarizer` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create `config/openAPI.txt` and put your OpenAI API key in it. This key file is ignored by Git; keep the key private and do not share it.

Start the app:

```bash
python -m streamlit run app.py
```

Streamlit prints a local URL in the terminal; open it in your browser to use the app.

## App features

- Paste text into the app to summarize.
- Choose a Short, Medium, or Long summary.
- Generate a summary using the OpenAI `gpt-4o-mini` model.
- View the generated summary in the app. Generation errors are shown in the UI and logged to the console.

## Functions

### `summarizer.py`

- `_read_api_key_from_file()`: reads the API key from `config/openAPI.txt`.
- `initialize_langchain_openai()`: creates a LangChain `ChatOpenAI` client configured for `gpt-4o-mini`.
- `_get_prompt()`: builds the LangChain prompt template with the summary instructions and text/length inputs.
- `_get_output_parser()`: creates a `StrOutputParser` to return the model response as text.
- `summarize_text(length, text)`: builds and invokes the prompt/model/parser chain, returning the summary text.

### `app.py`

The Streamlit script renders the text input and length selector, validates that text was entered, calls `summarize_text`, and displays the result. It also shows a spinner while generating and logs exceptions when generation fails.