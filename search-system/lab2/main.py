import requests
import json
import pandas as pd
import tools
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from data_collector import get_all_links, filter_links
from validator import validate_links
from metrics import get_moz_metrics
from visualizator import plot_authority_chart


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import matplotlib.pyplot as plt
from collections import Counter

def get_links(url):
    """
    Extracts internal and external links from a webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        tuple: A tuple containing two lists - internal links and external links.
    """
    internal_links = set()
    external_links = set()

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        base_url = "{0.scheme}://{0.netloc}".format(urlparse(url))

        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(base_url, href)
            if urlparse(full_url).netloc == urlparse(url).netloc:
                internal_links.add(full_url)
            else:
                external_links.add(full_url)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

    return list(internal_links), list(external_links)

def check_status_codes(links):
    """
    Checks the HTTP status code for each link.

    Args:
        links (list): List of URLs to check.

    Returns:
        dict: A dictionary where keys are URLs and values are status codes.
    """
    statuses = {}
    for link in links:
        try:
            response = requests.head(link, allow_redirects=True, timeout=5)
            statuses[link] = response.status_code
        except requests.exceptions.RequestException:
            statuses[link] = "Error"
    return statuses

def create_table(link_statuses, table_name):
    df = pd.DataFrame(link_statuses.items(), columns=["Link", "Status Code"])
    print(f"\n{table_name}:")
    print(df)

    df.to_csv(f"{table_name}.csv", index=False)
    print(f"Table saved as {table_name}.csv")


def main(url):
    """
    Main function to extract links, check status codes, and display tables.

    Args:
        url (str): The URL of the website to analyze.
    """
    print(f"Fetching links from {url}...")
    internal_links, external_links = get_links(url)

    print(f"\nFound {len(internal_links)} internal links and {len(external_links)} external links.")
    print("\nChecking status codes for internal links...")
    internal_statuses = check_status_codes(internal_links)
    print("Checking status codes for external links...")
    external_statuses = check_status_codes(external_links)

    # Display tables
    print("\nDisplaying tables for internal and external links...")
    create_table(internal_statuses, "Internal Links and Status Codes")
    create_table(external_statuses, "External Links and Status Codes")



# main(site_url)


# url = ['https://www.wix.com/', 'https://example.com/']
urls = ["https://ua.korrespondent.net/", 'https://example.com/', 'https://www.wix.com/']
metrics = get_moz_metrics(urls)
plot_authority_chart(metrics)

# all_links = get_all_links(url)
# internal_links, external_links = filter_links(all_links, url)
#
# print("Внутрішні посилання:")
# for link in internal_links:
#     print(link)
#
# print("\nЗовнішні посилання:")
# for link in external_links:
#     print(link)
#
# working_internal, broken_internal, https_internal, non_https_internal = validate_links(internal_links)
# print("Working Internal Links:", working_internal)
# print("Broken Internal Links:", broken_internal)
# print("HTTPS Internal Links:", https_internal)
# print("Non-HTTPS Internal Links:", non_https_internal)
#
# print("\n--- External Links ---")
# working_external, broken_external, https_external, non_https_external = validate_links(external_links)
# print("Working External Links:", working_external)
# print("Broken External Links:", broken_external)
# print("HTTPS External Links:", https_external)
# print("Non-HTTPS External Links:", non_https_external)
