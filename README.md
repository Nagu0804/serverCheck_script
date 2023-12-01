# Website Monitoring Script

## Overview

This script monitors the status of specified websites and sends email notifications when a website goes down or comes back up. It uses asynchronous Python (asyncio) along with aiohttp for making asynchronous HTTP requests and smtplib for sending emails.

## Prerequisites

- Python 3.x installed
- Install required dependencies using `pip install -r requirements.txt`
- Configure environment variables in a `.env` file:
  - SMTP_SERVER: Your SMTP server address
  - SMTP_PORT: Your SMTP server port
  - SENDER_EMAIL: Your email address (sender)
  - SENDER_PASSWORD: Your email password
  - RECIPIENT_EMAIL: Comma-separated list of recipient email addresses
  - URLS: Comma-separated list of URLs to monitor

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/website-monitoring-script.git
   cd serverCheck_script
   ```

2. Install dependencies:
    ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file and configure the required environment variables.

4. Configuration:
    Edit the .env file to configure the following environment variables:

    SMTP_SERVER: Your SMTP server address.
    SMTP_PORT: Your SMTP server port.
    SENDER_EMAIL: Your email address (sender).
    SENDER_PASSWORD: Your email password.
    RECIPIENT_EMAIL: Comma-separated list of recipient email addresses.
    URLS: Comma-separated list of URLs to monitor.

5. Example .env File
env
Copy code
    ```bash
    SMTP_SERVER=smtp.example.com
    SMTP_PORT=587
    SENDER_EMAIL=your-email@example.com
    SENDER_PASSWORD=your-email-password
    RECIPIENT_EMAIL=recipient1@example.com,recipient2@example.com
    URLS=https://example1.com,https://example2.com
    ```

6. Run the script:
    ```bash
    python monitor.py
    ```