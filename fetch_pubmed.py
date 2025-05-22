import requests
import xmltodict
import pandas as pd

def fetch_pubmed_articles(query, max_results=5):
    """
    Fetch articles from PubMed based on a search query.

    Parameters:
    query (str): The search term to fetch relevant PubMed articles.
    max_results (int): The maximum number of articles to fetch.

    Returns:
    None: Saves the articles' titles and abstracts into a CSV file.
    """
    search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={query}&retmax={max_results}&retmode=json"
    search_response = requests.get(search_url)

    if search_response.status_code != 200:
        print("❌ Error fetching PubMed search results")
        return

    search_data = search_response.json()
    article_ids = search_data.get("esearchresult", {}).get("idlist", [])

    if not article_ids:
        print("❌ No articles found for the given query.")
        return

    ids = ",".join(article_ids)
    fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={ids}&retmode=xml"
    fetch_response = requests.get(fetch_url)

    if fetch_response.status_code != 200:
        print("❌ Error fetching PubMed article details")
        return

    try:
        articles = xmltodict.parse(fetch_response.content)["PubmedArticleSet"]["PubmedArticle"]
    except KeyError:
        print("❌ Error parsing article data")
        return

    titles, abstracts = [], []
    for article in articles:
        title = article["MedlineCitation"]["Article"]["ArticleTitle"]
        abstract = article["MedlineCitation"]["Article"].get("Abstract", {}).get("AbstractText", "No abstract available")

        # If abstract is a list, join multiple paragraphs into one string
        if isinstance(abstract, list):
            abstract = " ".join(abstract)

        titles.append(title)
        abstracts.append(abstract)

    df = pd.DataFrame({"Title": titles, "Abstract": abstracts})
    df.to_csv("pubmed_data.csv", index=False)
    print("✅ Data saved successfully!")

# Example usage
if __name__ == "__main__":
    fetch_pubmed_articles("diabetes", max_results=5)
