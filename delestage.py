import requests
from bs4 import BeautifulSoup

def openornot():
    # Send an HTTP request to the website and retrieve the HTML source code
    html = requests.get("https://www.univ-tours.fr/delestage-1").text

    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")

    # Find all the elements on the page that contain information about the building's status
    building_status_elements = soup.find_all("tr")

    list_for_building = []

    # Loop through the elements and extract the text from each one
    for element in building_status_elements:
        if "Open" in element.text or "Blois" in element.text:
            continue
        string = None
        building_status_text = element.text
        
        # Check if the building is open or closed
        if "Faculté des Sciences et Techniques" in building_status_text:
            string = "Le bâtiment : Faculté des Sciences et Techniques"
        elif "Ecole Polytechnique Universitaire (Département Mécanique / Electronique)" in building_status_text:
            string = "Le bâtiment : Ecole Polytechnique Universitaire (Département Mécanique / Electronique)"
        elif "Ecole Polytechnique Universitaire (Département Informatique)" in building_status_text:
            string = "Le bâtiment : Ecole Polytechnique Universitaire (Département Informatique)"
        elif "Ecole Polytechnique Universitaire (Département Aménagement et environnement)" in building_status_text:
            string = "Le bâtiment : Ecole Polytechnique Universitaire (Département Aménagement et environnement)"
        if string != None:
            if "Ouvert" in building_status_text:
                string += " est ouvert."
            else:
                string += " est potentiellement fermé, veuillez vérifier sur le site de l'université."
            list_for_building.append(string)

    return list_for_building

if __name__ == "__main__":
    print(openornot())
