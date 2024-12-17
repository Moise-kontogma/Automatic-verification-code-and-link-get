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
Multi-account Email Management: If you have multiple Gmail accounts and want to monitor them for important verification codes, this script makes it easy to handle all of them in one place

Here's a step-by-step guide on how to set up and run the Python script, including the installation of necessary libraries:

### 1. Install Python
First, ensure you have Python installed. If not, download it from [python.org](https://www.python.org/downloads/) and install it. During the installation, make sure to check the option to **Add Python to PATH**.

### 2. Install Required Libraries

The script requires a few Python libraries. You can install them using `pip`. Follow these steps:

1. **Create a Project Folder**:
   - Create a folder for your project (e.g., `GmailVerificationScript`).

2. **Navigate to the Project Folder**:
   Open your terminal (Command Prompt or PowerShell in Windows, Terminal on macOS or Linux) and navigate to your project folder. Use the following command:

   ```bash
   cd path\to\your\project\folder
   ```

3. **Create a `requirements.txt` File**:
   Inside your project folder, create a file named `requirements.txt` with the following content:

   ```
   imaplib
   pyperclip
   keyboard
   langdetect
   ```

4. **Install the Libraries**:
   In the terminal, run the following command to install all the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all the libraries needed for the script.

### 3. Set Up Your Gmail Account for IMAP

To use this script, you need to enable IMAP access in your Gmail account and generate an application-specific password.

1. **Enable IMAP**:
   - Go to your Gmail account.
   - In the top right corner, click on the gear icon and go to **Settings**.
   - Click on the **Forwarding and POP/IMAP** tab.
   - Under the **IMAP Access** section, select **Enable IMAP** and click **Save Changes**.

2. **Generate an Application-Specific Password**:
   - Visit [Google's App Passwords page](https://myaccount.google.com/apppasswords).
   - If 2-Step Verification is not enabled, enable it first.
   - Under **Select app**, choose **Mail** and select **Windows Computer** (or another option that suits you).
   - Generate the password and note it down.

### 4. Configure the Script

1. **Modify the Script**:
   - Open the Python script in a text editor (e.g., Notepad or VS Code).
   - Replace the `EMAIL` and `PASSWORD` fields with your Gmail address and application-specific password:
     
     ```python
     EMAIL = "your_email@gmail.com"  # Your email
     PASSWORD = "your_app_password"  # Your generated app password
     ```

2. **Add Multiple Gmail Accounts (if needed)**:
   If you want to monitor multiple Gmail accounts, add the additional accounts under the `accounts` list in the script:

   ```python
   accounts = [
       {"email": "your_email1@gmail.com", "password": "app_password1"},
       {"email": "your_email2@gmail.com", "password": "app_password2"}
   ]
   ```

### 5. Running the Script

1. **Run the Script**:
   - Open a terminal or command prompt and navigate to your project folder.
   - Run the script using Python:

   ```bash
   python code.py
   ```

   The script will now monitor your Gmail accounts and wait for the specified keyboard shortcut (Ctrl + ') to check for verification codes and links.

### 6. Setting Up the Keyboard Shortcut

You can trigger the script to check for emails by pressing **Ctrl + '**. The script will check for new verification codes and confirmation links in the emails received within the last 10 minutes.

### 7. (Optional) Run the Script in the Background

If you'd like the script to keep running in the background, you can use `pythonw` (on Windows) to run it without opening a terminal window.

- **On Windows**, run:

   ```bash
   pythonw code.py
   ```

   This will allow the script to run in the background and only respond to keyboard events.

---

That's it! You've successfully set up the Python script to monitor Gmail accounts for verification codes and confirmation links. Let me know if you encounter any issues along the way!
