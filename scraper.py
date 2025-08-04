import pandas as pd
from datetime import datetime

# Simulated scraped data (replace with real scraping logic)
data = [
    {"Product": "Note Sorting Machine", "State": "Maharashtra", "Tender Date": datetime.today().strftime("%Y-%m-%d"), "Department": "Finance"},
    {"Product": "Currency Counting Machine", "State": "Karnataka", "Tender Date": datetime.today().strftime("%Y-%m-%d"), "Department": "Treasury"},
    {"Product": "Fake Note Detector", "State": "Delhi", "Tender Date": datetime.today().strftime("%Y-%m-%d"), "Department": "Police"}
]

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
print("✅ Tender data saved to data.csv")