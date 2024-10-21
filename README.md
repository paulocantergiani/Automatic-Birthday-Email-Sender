
# Automatic Birthday Wisher 🎉

This project is an **Automatic Birthday Wisher** built in Python. It reads birthdays from a CSV file and sends personalized birthday emails to the recipients on their special day. 

## Features
- Randomly selects one of the pre-defined email templates.
- Reads birthday data from a CSV file.
- Sends personalized birthday emails using **SMTP** (with Gmail as the email provider).
- Handles authentication errors and missing data gracefully.

## Project Structure
```
├── birthdays.csv           # CSV file with birthday information
├── letter_templates/       # Folder containing email templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── main.py                 # Main Python script
├── module.py               # Python File with the Classes
└── README.md               # Project documentation (this file)
```

## CSV File Format
The `birthdays.csv` file should follow this format:

```csv
name,email,year,month,day
John,john@example.com,1985,1,5
Alice,alice@example.com,1990,3,15
...
```

## Email Templates
Each email template should contain a placeholder `[NAME]` where the recipient's name will be inserted. Example:

```
Dear [NAME],

Wishing you the happiest birthday ever! May your day be filled with joy and laughter.

Best wishes,
[Your Name]
```

## Prerequisites
- Python 3.x installed on your machine.
- A Gmail account to send emails (less secure apps access must be enabled).

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/automatic-birthday-wisher.git
   cd automatic-birthday-wisher
   ```

2. Install dependencies (if any):
   ```bash
   pip install pandas
   ```

3. Set up your **Gmail** credentials in the `main.py` file:
   ```python
   SENDER_EMAIL = "your-email@gmail.com"
   SENDER_PASSWORD = "your-app-password"
   ```

4. Add your birthday data to the `birthdays.csv` file.

## Running the Project
Run the Python script to automatically send birthday emails:
```bash
python main.py
```

## Troubleshooting
- **SMTPAuthenticationError:** Ensure your Gmail account has "less secure apps" access enabled or use an **App Password**.
- **FileNotFoundError:** Make sure the email templates and `birthdays.csv` file are correctly placed in the project directory.

## Contributing
Feel free to open an issue or submit a pull request if you have any improvements or suggestions.