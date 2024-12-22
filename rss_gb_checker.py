# This script is used to skim through an rss feed and find the GB size of each item
# and collect the total GB of the rss feed
# -------------------------------------------------------------------------

import feedparser
import re

rss_url = 'INSERTURLHERE' # Important: insert the url of the RSS feed here
feed = feedparser.parse(rss_url)

# find common word pattern to find the file size in GB (e.g 2.3 GB)
size_pattern = re.compile(r'(\d+\.\d+) GB')

# init total size
total_size = 0

# Loop through the entries and sum up the file sizes
for entry in feed.entries:
    # find the size in the description
    match = size_pattern.search(entry.description)
    if match:
        size_gb = float(match.group(1)) 
        total_size += size_gb  # Add the size to the total

print(f'Total size of all items: {total_size:.2f} GB')
