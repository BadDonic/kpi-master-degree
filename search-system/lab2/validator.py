def validate_links(links):
    working_links = set()
    broken_links = set()
    https_links = set()
    non_https_links = set()

    for link in links:
        try:
            response = requests.head(link, timeout=5)
            if response.status_code < 400:
                working_links.add(link)
                if urlparse(link).scheme == 'https':
                    https_links.add(link)
                else:
                    non_https_links.add(link)
            else:
                broken_links.add(link)
        except (requests.RequestException, requests.ConnectionError):
            broken_links.add(link)

    return working_links, broken_links, https_links, non_https_links
