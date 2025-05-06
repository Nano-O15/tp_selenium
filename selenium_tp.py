from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import csv
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Recherche sur Doctolib avec Selenium.")
    parser.add_argument("--query", type=str, required=True, help="Requête Médicale.")
    parser.add_argument("--max_results", type=int, default=10, help="Nombre Max de Résultats à Afficher.")
    # parser.add_argument("--start_date", type=str, required=True, help="Date de Début (format JJ/MM/AAAA).")
    # parser.add_argument("--end_date", type=str, required=True, help="Date de Fin (format JJ/MM/AAAA).")
    # parser.add_argument("--convention", type=str, choices=["1", "2", "nc"], help="Type d'Assurance.")
    # parser.add_argument("--consultation", type=str, choices=["visio", "sur_place"], help="Type de Consultation.")
    # parser.add_argument("--min_price", type=int, help="Prix Minimum (en euros).")
    # parser.add_argument("--max_price", type=int, help="Prix Maximum (en euros).")
    parser.add_argument("--place", type=str, required=True, help="Mot-clé pour le Filtre Géographique.")
    return parser.parse_args()

def get_names(driver, max_results, output_file="praticiens.csv"):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.p-16.box-border.flex.flex-col.gap-8.shrink-0.basis-\\[37\\%\\]')))
    
    cards = driver.find_elements(By.CSS_SELECTOR, 'div.p-16.box-border.flex.flex-col.gap-8.shrink-0.basis-\\[37\\%\\]')
    cards = cards[:max_results]

    data = []

    for card in cards:
        try:
            name = card.find_element(By.CSS_SELECTOR, "h2").text.strip()
        except:
            name = "Nom non trouvé"

        try:
            address_container = card.find_elements(By.CSS_SELECTOR, "div.flex.flex-wrap.gap-x-4")
            if address_container:
                address_parts = address_container[0].find_elements(By.TAG_NAME, "p")
                if len(address_parts) >= 2:
                    address = f"{address_parts[0].text.strip()}, {address_parts[1].text.strip()}"
                else:
                    address = "Adresse incomplète"
            else:
                address = "Adresse non trouvée"
        except:
            address = "Erreur récupération adresse"

        data.append((name, address))

    with open(output_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Nom du praticien", "Adresse"])
        for name, address in data:
            writer.writerow([name, address])


def search(query, max_results, place):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get("https://www.doctolib.fr/")

    try:
        wait = WebDriverWait(driver, 10)
        refuse_button = wait.until(EC.element_to_be_clickable((By.ID, "didomi-notice-disagree-button")))
        refuse_button.click()
    except:
        pass
    
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.searchbar-input.searchbar-query-input")))
    query_input = driver.find_element(By.CSS_SELECTOR, "input.searchbar-input.searchbar-query-input")
    query_input.clear()
    query_input.send_keys(query)
    wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "input.searchbar-input.searchbar-query-input"), query))
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.searchbar-result.searchbar-result-active")))
    query_result = driver.find_element(By.CSS_SELECTOR, "button.searchbar-result.searchbar-result-active")
    query_result.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.searchbar-input.searchbar-place-input")))
    place_input = driver.find_element(By.CSS_SELECTOR, "input.searchbar-input.searchbar-place-input")
    place_input.clear()
    place_input.send_keys(place)
    wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "input.searchbar-input.searchbar-place-input"), place))
    
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.searchbar-result.searchbar-result-active")))
    query_result = driver.find_element(By.CSS_SELECTOR, "button.searchbar-result.searchbar-result-active")
    query_result.click()

    try:
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-design-system='oxygen'][type='submit']")))
        search_button.click()
    except:
        pass

    get_names(driver, max_results)

def main():
    args = parse_args()
    search(args.query, args.max_results, args.place)

if __name__ == "__main__":
    main()