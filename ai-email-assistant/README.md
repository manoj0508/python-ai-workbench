# AI Email Assistant

A Streamlit app that generates professional emails with the OpenAI API.

## Project structure

```text
ai-email-assistant/
├── app.py                   # Streamlit interface and session-only email history
├── email_generator.py       # API key loading, prompt creation, and email generation
├── config/
│   └── openAPI.txt          # OpenAI API key (keep private; do not commit)
├── requirements.txt         # Python dependencies
└── README.md                # Project instructions
```

## Requirements

- Python 3.9 or newer
- An OpenAI API key

## Setup and run

Run these commands from the `ai-email-assistant` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Put your OpenAI API key in `config/openAPI.txt`. Keep the key private and do not commit or share it.

Start the app:

```bash
python -m streamlit run app.py
```

Streamlit prints a local URL in the terminal; open it in your browser to use the app.

## App features

- Enter the purpose of the email and select a tone, recipient, and length.
- Optionally provide a sender name. If it is blank, the generator uses `Manoj K`.
- Generate an email with a subject line and a professional format.
- Browse emails generated during the current Streamlit session. History is session-only and clears when the session ends.
- Download the latest generated email as `generated_email.txt`.

## Functions

### `email_generator.py`

- `_read_api_key_from_file()`: reads the API key from `config/openAPI.txt`.
- `_get_prompt(purpose, tone, recipient, sender_name=None, length="Medium")`: creates the prompt with the requested email details and approximate length guidance (Short: 50 words, Medium: 100 words, Long: 200 words).
- `generate_email(purpose, tone, recipient, sender_name, length="Medium")`: sends the prompt to the OpenAI `gpt-4o-mini` model and returns the generated email text.

### `app.py`

The Streamlit script builds the user interface, validates that a purpose was entered, calls `generate_email`, displays and stores generated emails in session state, and provides the download button.
