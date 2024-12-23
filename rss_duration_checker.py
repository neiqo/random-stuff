# The script will parse the RSS feed, count the number of <item> elements, 
# and calculate the duration between the oldest and newest item
# ------------------------------------------------------------

import feedparser
from dateutil import parser as date_parser

rss_url = "INSERTURL HERE" # Important: insert the url of the RSS feed here

feed = feedparser.parse(rss_url)

if feed.bozo:
    print("Failed to fetch or parse the RSS feed. Please check the URL.")
    exit()

items = feed.entries
num_items = len(items)

if num_items == 0:
    print("No items found in the RSS feed.")
    exit()

pub_dates = [date_parser.parse(item.published) for item in items]

oldest_date = min(pub_dates)
newest_date = max(pub_dates)
duration = newest_date - oldest_date

print(f"Number of items: {num_items}")
print(f"Oldest item date: {oldest_date}")
print(f"Newest item date: {newest_date}")
print(f"Duration between oldest and newest: {duration}")
