import requests
import base64

# Moz API credentials
MOZ_ACCESS_ID = 'mozscape-uj3GR66kdF'
MOZ_SECRET_KEY = 'PMElYpc97LkKEMkfVjUheWG55OwoFz39'

auth_string = f"{MOZ_ACCESS_ID}:{MOZ_SECRET_KEY}"
auth_header = base64.b64encode(auth_string.encode()).decode()

def get_moz_metrics(urls):
    api_url = f"https://lsapi.seomoz.com/v2/url_metrics"
    headers = {
        "Authorization": f"Basic {auth_header}"
    }
    data = {"targets": urls, "metrics": ["external_links", "page_authority", "domain_authority"]}
    response = requests.post(api_url, json=data, headers=headers)
    if response.status_code == 200:
        results = response.json().get('results')

        metrics = []
        for result in results:
            metrics.append({
                "da": result.get('domain_authority'),
                "pa": result.get('page_authority'),
                "url": result.get('page')
            })
        return metrics

    else:
        print("Error:", response.status_code, response.text)
        return None

