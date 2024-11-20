def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = set()
    for anchor in soup.find_all('a', href=True):
        href = anchor['href']
        if href.startswith('javascript:') or href.startswith('#') or not href.strip():
            continue
        full_url = urljoin(url, href)
        links.add(full_url)
    return links

def filter_links(links, base_url):
    internal_links = set()
    external_links = set()
    base_domain = urlparse(base_url).netloc
    for link in links:
        domain = urlparse(link).netloc
        if domain == base_domain:
            internal_links.add(link)
        else:
            external_links.add(link)
    return internal_links, external_links
