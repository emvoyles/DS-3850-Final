# NYT News Newsletter Generator 🗞️

This project automatically fetches the most popular articles from The New York Times and emails them as a daily newsletter to a recipient using SMTP email services.

## 🔧 Features

- Pulls the top 5 most popular articles from the NYT Most Popular API
- Generates a plain-text newsletter from article titles, abstracts, and URLs
- Sends the newsletter to a specified recipient via email
- Uses environment variables for secure API key and email credential storage

## 📦 Requirements

- Python 3.7+
- NYT Developer API key
- Email account that supports SMTP (tested with iCloud and Gmail)
- `.env` file with your credentials

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/DS-3850-Final.git
   cd DS-3850-Final
