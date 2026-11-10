from pathlib import Path
from typing import Any
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


def _read_api_key_from_file() -> str:
    key_file = Path(__file__).resolve().parent / "config" / "openAPI.txt"
    return key_file.read_text(encoding="utf-8")


def initialize_langchain_openai():
    open_ai_client = ChatOpenAI(
        model_name="gpt-4o-mini",
        openai_api_key=_read_api_key_from_file(),
        temperature=0.7,
        max_tokens=500,
    )
    return open_ai_client

def _get_prompt() -> PromptTemplate:
    return PromptTemplate.from_template(
        """
        You are an expert text summarizer,
        Summarize the following text in a {length} format.
        Instructions:
        1. Keep the summary concise and clear.
        2. identify the key points and main ideas.
        3. Avoid unnecessary details and repetition.
        4. keep the summary easy to understand.

        Text:
        {text}
        Summary:
        """
    )

def _get_output_parser() -> StrOutputParser:
    parser = StrOutputParser()
    return parser


def summarize_text(length: str, text: str) -> Any:
    prompt = _get_prompt()
    open_ai_client = initialize_langchain_openai()
    parser = _get_output_parser()

    summarizer_chain = prompt | open_ai_client | parser
    result = summarizer_chain.invoke({"text": text, "length": length})
    return result