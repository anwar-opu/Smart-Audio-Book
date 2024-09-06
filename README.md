# Smart Audio Book

The **Smart Audio Book** is a Python application designed to convert text from a PDF into spoken words. Using text-to-speech (TTS) technology, this tool reads aloud the contents of a PDF document, making it easier to consume text-based content on the go.

## Features
- Reads aloud the text content of a PDF document.
- Allows users to specify the range of pages to be read.
- Provides interactive prompts for user input.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anwar-opu/Smart-Audio-Book.git
2. Install the Required Libraries
   ```bash
   pip install pyttsx3 PyPDF2

## Usage
  1. Place your PDF file in the project directory. Rename it to oop.pdf or modify the code to match your file name.
  2. Run the script:
  ```bash
    python main.py
  ```
3. Follow the prompts:

  - Enter the start page number when prompted.
  - Enter the end page number when prompted.
  
The application will read aloud the text from the specified range of pages.

## Acknowledgments
- `pyttsx3` : For providing the text-to-speech functionality, which makes it possible to convert text from the PDF into spoken words.
- `PyPDF2` : For offering tools to extract text from PDF files, enabling the script to read and process document content.
