import PyPDF2
import pyttsx3

def pdf_to_speech(pdf_path):
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)

        # Extract text from each page and concatenate it
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the speech rate (optional)
    # engine.setProperty('rate', 150)  # Adjust the value as needed

    # Convert the text to speech
    engine.say(text)
    engine.runAndWait()

# Provide the path to your PDF file
pdf_file = 'Untitled document (2).pdf'

# Convert the PDF to speech
pdf_to_speech(pdf_file)
