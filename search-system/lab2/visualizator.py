import matplotlib.pyplot as plt

def plot_authority_chart(data):
    urls = [item['url'] for item in data]
    da_values = [item['da'] for item in data]
    pa_values = [item['pa'] for item in data]

    plt.figure(figsize=(12, 6))
    x = range(len(urls))

    plt.bar(x, pa_values, width=0.4, label="Page Authority (PA)", align='center', alpha=0.7)
    plt.bar(x, da_values, width=0.4, label="Domain Authority (DA)", align='edge', alpha=0.7)

    plt.xticks(x, urls, rotation=45, ha="right")
    plt.xlabel("URLs")
    plt.ylabel("Authority Score")
    plt.title("Comparison of Domain Authority (DA) and Page Authority (PA)")
    plt.legend()
    plt.tight_layout()
    plt.show()
