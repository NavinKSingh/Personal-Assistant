import requests 
from output1 import output
from connection import check_internet_connection   
 
def get_news():
    if check_internet_connection():
        query_params = {
            "source": "bbc-news",
            "sortBy": "top",
            "apiKey": "47f89e07463141d9ac953d9b36ad310a"
            }
        main_url = " https://newsapi.org/v1/articles"
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        article = open_bbc_page["articles"]
        results = []
        for ar in article:
            results.append(ar["title"])
        for i in range(len(results)):
            output(str(i + 1)+" "+results[i])
        return "These are the top news stories of today, sir."
    else:
        return "Check internet connection"
