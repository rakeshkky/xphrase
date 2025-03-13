import requests
import argparse
import pyperclip
import pkg_resources

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:1b"

# User prompt for rephrasing
USER_PROMPT = """
Please take the following text and rephrase it, making only minimal changes to enhance clarity and effectiveness.
Retain the original structure of the text. Respond with only the rephrased text.
"""

def get_version():
    """
    Get the current version and timestamp.

    Returns:
        str: Version string
    """
    version = pkg_resources.get_distribution('xphrase').version
    return f"{version} {MODEL}"

def rephrase_text(input_text):
    """
    Rephrases the input text using the Ollama API.

    Args:
        input_text (str): The text to rephrase.

    Returns:
        str: The rephrased text.
    """
    payload = {
        "model": MODEL,
        "prompt": USER_PROMPT + f"\n\nText to rephrase: {input_text}",
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        raise Exception(f"Ollama API request failed with status code {response.status_code}: {response.text}")

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="XPhrase - AI-powered text rephrasing tool"
    )
    parser.add_argument(
        "-i", "--input",
        required=False,
        help="Input text to rephrase. If not provided, uses clipboard content"
    )
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version information"
    )
    return parser.parse_args()

def main():
    try:
        args = parse_args()
    except argparse.ArgumentError as e:
        print(e)
        return

    if args.version:
        print(get_version())
        return
    result = None
    using_clipboard = False

    try:
        # Get input text from argument or clipboard
        input_text = args.input

        if input_text is None:
            input_text = pyperclip.paste()
            if not input_text:
                raise Exception("No text found in clipboard")
            using_clipboard = True

        # Rephrase the text
        result = rephrase_text(input_text)

    except Exception as e:
        result = f"Error: {e}"

    # Handle output
    if using_clipboard:
        pyperclip.copy(result)
    else:
        print(result)

if __name__ == "__main__":
    main()
