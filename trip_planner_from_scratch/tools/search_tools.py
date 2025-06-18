import json
from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class SearchTools():
    @tool("Search the web")
    def search_internet(query):
        '''Useful to search the internet about a given
        topic and return relevant results.
        '''
        top_result_to_return=4
        url= "https://google.serper.dev/search"
        payload= json.dumps({"q": query})
        headers={
            "X-API-KEY": os.getenv("SERPER_API_KEY"),
            "Content-Type": "application/json",
        }
        response= requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "Sorry, I couldn't find any relevant results for your query."
        else:
            results= response.json()['organic']
            string=[]
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}","\n--------------------------------"
                    ]))
                except KeyError:
                    next
            return "\n\n".join(string)
