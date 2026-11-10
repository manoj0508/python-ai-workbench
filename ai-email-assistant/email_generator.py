from openai import OpenAI
from pathlib import Path


def _read_api_key_from_file() -> str:
    key_file = Path(__file__).resolve().parent / "config" / "openAPI.txt"
    return key_file.read_text(encoding="utf-8")


def _get_prompt(purpose, tone, recipient, sender_name=None, length="Medium")-> str:
    if sender_name is None or sender_name.strip() == "":
        sender_name = 'Manoj K'
    prompt = f"""
        You are an expert email writer.
        Generate email.
        Purpose: {purpose}
        Tone: {tone}
        Recipient: {recipient}
        Email length: {length}
        Regards:{sender_name}
        Rules: 
        1. Generate subject line 
        2. Write professional email 
        3. Match the requested email length: Short (about 50 words), Medium (about 100 words), or Long (about 200 words)
        4. Output in clean format
        """
    return prompt


def generate_email(purpose, tone, recipient, sender_name, length="Medium")-> str:
    open_ai_client = OpenAI(api_key=_read_api_key_from_file())
    prompt = _get_prompt(purpose, tone, recipient, sender_name, length)
    response = open_ai_client.chat.completions.create(model="gpt-4o-mini", 
                                messages=[{"role":"system","content":"You generate emails."},
                                          {"role": "user", "content": prompt}])
    return response.choices[0].message.content