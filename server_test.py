import os
from dotenv import load_dotenv
import aiohttp
import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("SENDER_PASSWORD")
recipient_emails= os.getenv("RECIPIENT_EMAIL")
recipient_email = [email.strip() for email in recipient_emails.split(",")]
print(recipient_emails)


urls = os.getenv("URLS")
urls = [url.strip() for url in urls.split(",")]
print(urls)

async def send_mail(message=None,url=None ,sent =None):
    
    if recipient_emails:
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = str(recipient_email)
            if sent == True:
                msg['Subject'] = f"{url} - website down"
            else :
                msg['Subject'] = f"{url} - website now up"

            msg.attach(MIMEText(message, 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, msg.as_string())

            print(message)

        except Exception as e:
            print(f"An error occurred: {e}")

async def check(session, url):
    sent = False
    while True:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=120)) as res:
                message = f"Server at {url} is OK"
                print(message)
                if sent:
                    sent = False
                    await send_mail(f"Server at {url} is now up. Enjoy it", url ,sent)

        except (aiohttp.ClientConnectionError, aiohttp.ClientError, TimeoutError) as e:
            message = f"Server at {url} is down.Please Check  Error: {str(e)}"
            print(message)
            if not sent:
                sent = True
                await send_mail(message, url ,sent)
        
        except Exception as e:
            message = f"Server at {url} is down.Error: {str(e)}."
            print(message)
            if not sent:
                sent = True
                await send_mail(message, url,sent)
            

        await asyncio.sleep(60)

async def set_urls(urls):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(check(session, url) for url in urls))

asyncio.run(set_urls(urls))
