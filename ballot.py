import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
from pprint import pprint


def get_ballot(address, zipcode):
    """
    Take in address and zipcode
    return People, and Propositions
    """

    quote_address = urllib.parse.quote(address)
    can_url = f"http://www.smartvoter.org/uvote4/uvote4.cgi?addr={quote_address}&zip={zipcode}"

    can = requests.get(can_url)

    soup = BeautifulSoup(can.content, 'html.parser')

    # Extract propositions and results

    # Extract state executive results
    table = soup.find('a', {'name': 'state_executive'}).find_parent('table')

    # Adjusting the extraction logic to ensure order is preserved as found in the HTML
    ordered_dict = {}

    # Find all p and ul tags after the anchor
    sections = table.find_all_next(['p', 'ul'])

    current_title = None
    for section in sections:
        if section.name == 'p' and section.find('b'):
            current_title = section.find('b').text
        elif section.name == 'ul' and current_title:
            list_items = [li.text.split('\n')[0].replace(" votes", "") for li in section.find_all('li') ]
            ordered_dict[current_title] = list_items
            current_title = None  # Reset for next section


    section_name = "Propositions"
    result = {}
    # Find the table containing the anchor tag for the section_name
    table = soup.find('a', {'name': section_name}).find_parent('table') if soup.find('a', {'name': section_name}) else None
    if table:
        dt_tags = table.find_all_next('dt')
        dd_tags = table.find_all_next('dd')

        section_data = {}
        for dt, dd in zip(dt_tags, dd_tags):
            title = dt.find('b').text if dt.find('b') else None
            description = dd.find('font').text.strip().replace("\n", "") if dd else None
            if title and description:
                section_data[title.replace("\n"," ")] = description

        result.update( section_data )

    return ordered_dict, result

if __name__ == "__main__":
    people, propositions = get_ballot("4109 West St", "94608")
    
    print("People")
    print(json.dumps(people, indent=4))

    print("Propositions")
    print(json.dumps(propositions, indent=4))