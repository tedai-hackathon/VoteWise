import wikipediaapi
import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path


def get_wiki_text(wiki_url):


    wiki_wiki = wikipediaapi.Wikipedia('PythonRequests', 'en')

    # Parse the page title from the URL
    page_title = wiki_url.split("/")[-1]

    # Fetch the Wikipedia page
    page = wiki_wiki.page(page_title)

    # Check if the page exists
    if page.exists():
        # Print the text content of the page
        return page.text
    else:
        return ""
    
def get_bp_text(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if response.status_code == 200:    
        # Find the element with id "content"
        content_element = soup.find(id="content")
        
        # Check if the "content" element was found
        if content_element:
            
            # Print or process the content_html as needed
            return content_element.get_text()
            
        else:
            print(f"Failed to find content id on '{wiki_url}'.")
            return ""
    else:
        print(f"Failed to fetch the page '{wiki_url}'.")
        return ""

if __name__ == "__main__":
    w = get_wiki_text("https://en.wikipedia.org/wiki/Loren_Taylor")
    #print(w)
    m = get_bp_text("https://ballotpedia.org/Loren_Taylor")
 
    # Define the path to the file
    file_path = Path("data.json")

    # Read the file and load its JSON content
    with file_path.open('r', encoding='utf-8') as f:
        data = json.load(f)

    # Add text for people
    for person, person_data in data["People"].items():
        print(person)
        if data["People"][person].get("bp_url"):
            data["People"][person]["bp_text"] = get_bp_text(data["People"][person].get("bp_url"))

        if data["People"][person].get("wiki_url"):
            data["People"][person]["wiki_text"] = get_wiki_text(data["People"][person].get("wiki_url")) 

    for prop, prop_data in data["Propositions"].items():
        print(prop)
        if data["Propositions"][prop].get("bp_url"):
            data["Propositions"][prop]["bp_text"] = get_bp_text(data["Propositions"][prop].get("bp_url"))

        if data["Propositions"][prop].get("wiki_url"):
            data["Propositions"][prop]["wiki_text"] = get_wiki_text(data["Propositions"][prop].get("wiki_url")) 

    output_file_path = Path("data-enrich.json")
    with output_file_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
