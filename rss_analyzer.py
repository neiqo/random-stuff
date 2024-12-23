# This script is used to analyze an rss feed, showing the
# number of items, oldest item date, newest item date, the duration between the oldest and newest item, and the total size of all items (gb)
# (This script is combined with rss_duration_checker.py and rss_gb_checker.py )
# ------------------------------------------------------------

import feedparser
import re
from dateutil import parser as date_parser

rss_url = 'INSERTURLHERE' # Important: insert the url of the RSS feed here

feed = feedparser.parse(rss_url)

if feed.bozo:
    print("Failed to fetch or parse the RSS feed. Please check the URL.")
    exit()

items = feed.entries
num_items = len(items)

if num_items == 0:
    print("No items found in the RSS feed.")
    exit()


size_pattern = re.compile(r'(\d+\.\d+) GB')
total_size = 0

# Loop through the entries and sum up the file sizes
for entry in feed.entries:
    # find the size in the description
    match = size_pattern.search(entry.description)
    if match:
        size_gb = float(match.group(1)) 
        total_size += size_gb  # Add the size to the total


pub_dates = [date_parser.parse(item.published) for item in items]

oldest_date = min(pub_dates)
newest_date = max(pub_dates)
duration = newest_date - oldest_date

print(f"Number of items: {num_items}")
print(f"Oldest item date: {oldest_date}")
print(f"Newest item date: {newest_date}")
print(f"Duration between oldest and newest: {duration}")

print(f'Total size of all items: {total_size:.2f} GB')
