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

# input start page number
print('Enter the page number will you start')
speak.say('Enter the page number will you start')
speak.runAndWait()
start = int(input())
# input end page number
speak.say('Enter the page number you end')
speak.runAndWait()
print('Enter the page number you end')
end = int(input()) + 1

for i in range(start, end):
    page = pdfReader.pages[i]
    text = page.extract_text()
    # Speak the text
    speak.say(text)
    speak.runAndWait()

# Close the PDF file
book.close()
