import os
from urllib.parse import urlparse

# Define the input and output files
input_file = 'urls.txt'
output_file = 'unique_domains.txt'

# Function to extract domain from a URL
def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

# Read URLs from the input file and extract unique domains
unique_domains = set()
if os.path.exists(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            url = line.strip()
            if url:
                domain = extract_domain(url)
                unique_domains.add(domain)

# Write unique domains to the output file
with open(output_file, 'w') as file:
    for domain in unique_domains:
        file.write(domain + '\n')

print(f"Extracted {len(unique_domains)} unique domains from {input_file} and saved them to {output_file}.")
