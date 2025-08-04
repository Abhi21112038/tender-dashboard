import pandas as pd
import smtplib
from email.mime.text import MIMEText

# Load data
df = pd.read_csv("data.csv")

summary = df.groupby("State")["Product"].count().reset_index().sort_values(by="Product", ascending=False)
top_products = df["Product"].value_counts().head(3)

email_body = f"""
Hello,

Here is your weekly tender summary:

Top Regions by Tender Count:
{summary.to_string(index=False)}

Top Products in Demand:
{top_products.to_string()}

Regards,
Tender Tracker Bot
"""

msg = MIMEText(email_body)
msg["Subject"] = "Weekly Tender Summary"
msg["From"] = "your.email@gmail.com"
msg["To"] = "css@imsworld.in"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("your.email@gmail.com", "your-app-password")
    server.send_message(msg)

print("✅ Weekly summary email sent.")