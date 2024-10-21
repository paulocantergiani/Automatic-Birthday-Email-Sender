from module import LetterMaker

# Ensures the code only runs when the script is executed directly, not imported.
if __name__ == "__main__":
    letter = LetterMaker()
    letter.send_email()  # Initiates the email sending process.
