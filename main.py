import re
import feedparser
import ssl
from langchain.llms import Ollama
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context

class colors:
    RESET = '\033[0m'
    BLUE = '\033[34m'
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_today_news(url):
    feed = feedparser.parse(url)

    if not feed.bozo:
        news_data = [(entry.title, entry.summary) for entry in feed.entries]
        return news_data
    else:
        print(f"Failed to retrieve data from {url}. Error: {feed.bozo_exception}")
        return None

def generate_summary(title, excerpt):
    prompt = '''
    The following is an article with a title. 
    Give me a brief and precise summary of this article.
    Ensure the summary gives sufficient information on the topic, especially if there are unique or surprising aspects, so that there's no need to read the full article.
    Be sure to give me the summary in French (if it's not in French, translate it into French without giving me the english version).
    Your answer should be in the form: \"Résumé de l'article: *your_summary*\"
    '''
    llm = Ollama(model="llama2")
    response = llm.predict(prompt + title + excerpt)
    return response

def main():
    sites = {
        'FeedBurner': "https://feeds.feedburner.com/Kulturegeek",
        'TomsGuide': "https://www.tomsguide.fr/feed/",
        'Frandroid': "https://www.frandroid.com/feed"
    }
    summaries = {}

    today = datetime.today().strftime('%d-%m-%Y')
    print(f"{colors.BOLD}Résumés de l'actualité du jour :", today )

    for media, url in sites.items():
        news_data = get_today_news(url)
        summaries[media] = []

        print(" ")
        print(f"{colors.UNDERLINE}Génération de résumés pour {media}...")
        if len(news_data) > 0:
            print(f"{colors.RESET}{colors.BLUE}Nombre d'articles trouvé : {len(news_data)}")
        else:
            print(f"{colors.FAIL}Aucun article trouvé pour {media}")

        print(" ")

        # Générer un résumé pour chaque article et afficher titre et résumé alternativement
        for i in range(0, len(news_data)):
            title, excerpt = news_data[i]
            print(f"{colors.RESET}Titre de l'article : {title}")

            try:
                article_summary = generate_summary(title, excerpt)
                summaries[media].append(article_summary)

                print(f"{colors.GREEN}{article_summary}")
            except Exception as e:
                print(
                    f"{colors.FAIL}Erreur lors de la génération du résumé pour l'article '{title}': {colors.UNDERLINE}{e}"
                )

            print(f"{colors.RESET}")
    print(f"{colors.BOLD}{colors.UNDERLINE}Fin des résumés de l'actualité du jour : {today}")

if __name__ == "__main__":
    main()
