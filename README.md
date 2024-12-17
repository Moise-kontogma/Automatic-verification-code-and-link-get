Description: This project is a Python script designed to monitor multiple Gmail accounts for incoming verification codes and confirmation links in emails received within the last 10 minutes. The script is capable of detecting the language of the email content and can perform actions like copying the code to the clipboard or opening the confirmation link in a browser. The user can trigger the script to check for these codes and links by pressing a specific keyboard shortcut (Ctrl + ').

Key Features:

Multi-account Support: The script supports multiple Gmail accounts, allowing you to check for codes and links across several email addresses.
Real-time Monitoring: It monitors emails received in the last 10 minutes and looks for specific patterns such as 6-digit verification codes or URLs.
Automatic Actions:
Copy Codes to Clipboard: If a verification code is found, it will automatically copy it to the clipboard.
Open Links in Browser: If a confirmation link is detected, it will be opened in the default web browser.
Language Detection: The script can detect the language of the email and adapt the search for codes based on the language. It currently supports multiple languages including English, French, German, etc.
Keyboard Trigger: The user can trigger the script to check for new emails by pressing Ctrl + ' on their keyboard.
Secure Authentication: It uses Gmail’s IMAP protocol and supports application-specific passwords for secure login.
Technologies Used:

Python: The script is written in Python and leverages libraries for interacting with Gmail, detecting keypresses, and handling email content.
IMAP (Internet Message Access Protocol): For connecting and retrieving emails from Gmail accounts.
Keyboard Input Detection: Using the keyboard library to detect when the user presses the trigger combination.
Web Browser: The script can open URLs in the default web browser.
Pyperclip: For copying verification codes to the clipboard.
Langdetect: To automatically detect the language of email content to adjust the search for codes accordingly.
How It Works:

The script connects to Gmail accounts using IMAP with application-specific passwords for authentication.
It checks for new emails received in the last 10 minutes.
The script looks for verification codes (6-digit numbers) and confirmation links in the email content.
When the user presses Ctrl + ', the script searches for matching patterns in emails from all connected accounts.
If a code is found, it is copied to the clipboard. If a confirmation link is found, it is opened in the browser.
Use Cases:

Automating Verification Processes: This script is ideal for automating the process of receiving and using verification codes or clicking confirmation links for online registrations, sign-ins, or other processes that require verification emails.
Multi-account Email Management: If you have multiple Gmail accounts and want to monitor them for important verification codes, this script makes it easy to handle all of them in one place.
