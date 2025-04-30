import requests
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Load environment variables
load_dotenv(dotenv_path=".env")

NYT_API_KEY = os.getenv("NYT_API_KEY")
NYT_MOST_POPULAR_URL = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json"

print(f"NYT API Key: {NYT_API_KEY}")  # Check if the key is loaded correctly

def fetch_most_popular_articles(limit=5):
    params = {"api-key": NYT_API_KEY}
    response = requests.get(NYT_MOST_POPULAR_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"NYT API error: {response.status_code} - {response.text}")

    data = response.json()
    articles = data.get("results", [])[:limit]

    extracted_articles = []
    for article in articles:
        extracted_articles.append({
            "title": article["title"],
            "url": article["url"],
            "abstract": article["abstract"]
        })

    return extracted_articles

def generate_newsletter():
    articles = fetch_most_popular_articles(limit=5)
    
    # Format the articles into a readable newsletter body
    newsletter_body = "Here are the top 5 most popular articles from The New York Times:\n\n"
    for article in articles:
        newsletter_body += f"Title: {article['title']}\n"
        newsletter_body += f"Abstract: {article['abstract']}\n"
        newsletter_body += f"URL: {article['url']}\n\n"

    return newsletter_body

def send_email(subject, body, recipient_email):
    sender_email = "evoyles24@icloud.com"  
    sender_password = "gleq-ddyd-njgv-cabk"  # App-specific password from Apple ID

    smtp_server = "smtp.mail.me.com"
    smtp_port = 465  # SSL port for iCloud

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email using SMTP_SSL (not SMTP with starttls)
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient_email}!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


def main():
    # Generate the newsletter content
    newsletter_content = generate_newsletter()
    
    # Send the newsletter via email
    subject = "Your Daily NYT News Summary"
    recipient_email = "evoyles24@gmail.com"  # The email of the recipient
    send_email(subject, newsletter_content, recipient_email)

if __name__ == "__main__":
    main()
