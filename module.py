import smtplib
import pandas as pd
from datetime import datetime
import random

# Global variables for email credentials
SENDER_EMAIL = ""
SENDER_PASSWORD = ""


class LetterMaker:
    # Constructor method to initialize the LetterMaker class
    def __init__(self) -> None:
        # Choose a random letter template
        self.unedited_txt = self.choose_letter()
        # Check if today is someone's birthday and get their name and email
        self.aniversariant_info = self.check_aniversariant()

        if self.aniversariant_info:
            self.aniversariant_name, self.receiver_email = self.aniversariant_info
            self.ready_to_send_txt = self.process_file()
        else:
            self.aniversariant_name, self.receiver_email = None, None

        # SMTP server details for sending emails
        self.smtp_server = "smtp.gmail.com"
        self.port = 587  # Standard port for TLS connection

    # Selects a random letter template from 1 to 3
    def choose_letter(self):
        template_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        try:
            # Open and read the chosen template file
            with open(template_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            # Raise an error if the template file does not exist
            raise FileNotFoundError(f"File not found: {template_path}")

    # Replaces [NAME] placeholder in the template with the recipient's name
    def process_file(self):
        return self.unedited_txt.replace("[NAME]", self.aniversariant_name)

    # Checks if today matches any birthday from the CSV file and returns the name and email
    def check_aniversariant(self):
        today = datetime.today()  # Get today's date
        df = pd.read_csv("birthdays.csv")  # Load the CSV with birthday data
        # Filter rows where the day and month match today's date
        aniversariant = df[(df["day"] == today.day) & (df["month"] == today.month)]
        if not aniversariant.empty:
            # Return the name and email of the first matching entry
            name = aniversariant.iloc[0]["name"]
            email = aniversariant.iloc[0]["email"]
            return name, email
        return None  # Return None if no matching birthday is found

    # Sends an email with the personalized birthday message
    def send_email(self):
        if not self.aniversariant_name or not self.receiver_email:
            # Print a message if there is no birthday today
            print("No birthday today.")
            return

        # Compose the email with subject and personalized content
        message = f"Subject: Feliz Aniversário!\n\n{self.ready_to_send_txt}"
        try:
            # Establish a connection to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.set_debuglevel(2)  # Enable debug mode to see SMTP interaction
                server.starttls()  # Secure the connection with TLS
                # Login to the SMTP server with the provided global credentials
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                # Send the email, encoded in UTF-8 to support special characters
                server.sendmail(
                    SENDER_EMAIL, self.receiver_email, message.encode("utf-8")
                )
                print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            # Handle authentication errors
            print("Authentication error. Check your credentials.")
        except Exception as e:
            # Handle any other exceptions during email sending
            print(f"Failed to send email: {e}")


# Main script entry point
if __name__ == "__main__":
    try:
        # Create an instance of the LetterMaker class
        letter_maker = LetterMaker()
        # Attempt to send the birthday email
        letter_maker.send_email()
    except Exception as e:
        # Print any errors that occur during execution
        print(f"Error: {e}")
