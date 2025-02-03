# XPhrase

XPhrase is a command-line tool that uses AI to enhance and rephrase text while maintaining its original meaning and tone. It leverages the Ollama API to provide professional-grade text improvements, including grammar fixes, clarity enhancements, and better readability.

## Features

- AI-powered text rephrasing and improvement
- Grammar and spelling correction
- Seamless clipboard integration
- Command-line interface
- Works with Ollama's local LLM models

## Prerequisites

- Python 3.13 or higher
- Poetry (Python package manager)
- Ollama server running locally (with llama3.2 model)

## Configuration

Ensure Ollama is running locally with the following configuration:
- API endpoint: http://localhost:11434/api/generate
- Model: llama3.2

```bash
ollama run llama3.2
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rakeshkky/xphrase.git
cd xphrase
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Usage

XPhrase can be used in two ways:

1. With clipboard content:
```bash
poetry run xphrase
```
This will take text from your clipboard, rephrase it, and put the result back in your clipboard.

2. With direct input:
```bash
poetry run xphrase -i "Text to rephrase"
```
This will print the rephrased text to stdout.

To check the version:
```bash
poetry run xphrase -v
```
