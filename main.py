import pyttsx3
import PyPDF2

# Open the PDF file in binary mode
book = open('oop.pdf', 'rb')

# Use PdfReader instead of PdfFileReader
pdfReader = PyPDF2.PdfReader(book)

# Get the number of pages in the PDF
pages = len(pdfReader.pages)
print(f"The PDF has {pages} pages.")

# Initialize the pyttsx3 engine
speak = pyttsx3.init()

# Function to handle user input and validate page range
def get_valid_page_input(prompt, max_pages):
    while True:
        speak.say(prompt)
        speak.runAndWait()
        try:
            page_num = int(input(prompt))
            if 0 <= page_num < max_pages:
                return page_num
            else:
                print(f"Please enter a valid page number between 0 and {max_pages - 1}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Input start page number
start = get_valid_page_input('Enter the start page number:', pages)

# Input end page number
end = get_valid_page_input('Enter the end page number:', pages) + 1

# Iterate through the pages and read the text aloud
for i in range(start, end):
    page = pdfReader.pages[i]
    text = page.extract_text()
    if text:
        speak.say(text)
        speak.runAndWait()
    else:
        print(f"No text found on page {i + 1}")

# Close the PDF file
book.close()
