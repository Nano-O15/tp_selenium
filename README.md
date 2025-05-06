Voici un README adapté pour le code que vous avez fourni :
# TP Scraping - Selenium

## Description

Le TP consiste en un script de scraping permettant de rechercher des praticiens médicaux sur le site Doctolib, en fonction d'une requête médicale et d'un filtre géographique. Le script utilise Selenium pour automatiser la navigation sur le site, effectuer la recherche, et récupérer les informations des praticiens (nom et adresse) en fonction des résultats de recherche. Les données collectées sont ensuite stockées dans un fichier CSV.

Les fonctionnalités incluent la possibilité de :

* Rechercher des praticiens par spécialité médicale et localisation géographique
* Extraire le nom et l'adresse des praticiens depuis les résultats de recherche
* Exporter les données dans un fichier CSV

## Fonctionnalités principales

* **Recherche par spécialité médicale et lieu géographique** : Recherche avancée pour trouver des praticiens en fonction de critères médicaux et géographiques.
* **Extraction des informations** : Récupération automatique du nom et de l'adresse des praticiens.
* **Export CSV** : Sauvegarde des données collectées dans un fichier CSV pour un usage ultérieur.
* **Personnalisation de la recherche** : Limitation du nombre de résultats et possibilité d'affiner la recherche avec un mot-clé géographique.

## Technologies utilisées

* **Python 3** : Langage principal pour le script de scraping.
* **Selenium** : Automatisation de la navigation sur le site Doctolib.
* **WebDriver** : Utilisation de Firefox pour l'exécution des tâches automatisées.
* **GeckoDriverManager** : Gestion automatique du driver Firefox.
* **CSV** : Format utilisé pour exporter les données collectées.
* **Argparse** : Gestion des arguments en ligne de commande.

## Installation

### Prérequis

* **Python 3.6+** : Assurez-vous d'avoir Python installé sur votre machine.
* **Firefox** : Le navigateur Firefox doit être installé, car le script utilise le WebDriver Firefox.
* **Selenium WebDriver** : Le script utilise le WebDriver de Selenium pour interagir avec le navigateur.

### Étapes d'installation

1. **Cloner le dépôt** :

   ```bash
   git clone <url-du-depot>
   cd tp_selenium
   ```

2. **Installer les dépendances Python** :

   ```bash
   pip3 install selenium webdriver-manager
   ```

## Utilisation

Le script s'exécute en ligne de commande avec plusieurs options :

1. **Exécution du script de recherche** :

   ```bash
   python3 selenium_tp.py --query "<requete_medicale>" --place "<ville>" --max_results <nombre_de_resultats>
   ```

   * **--query** : Spécifiez la spécialité médicale que vous souhaitez rechercher (ex. "dentiste", "médecin généraliste").
   * **--place** : Indiquez le mot-clé géographique pour affiner la recherche (ex. "Paris").
   * **--max\_results** : Limite le nombre de résultats à afficher dans le fichier CSV (par défaut à 10).

2. **Exemple d'exécution** :

   ```bash
   python3 selenium_tp.py --query "dentiste" --place "Paris" --max_results 20
   ```

   Cette commande recherchera les dentistes à Paris et extraira les 20 premiers résultats.

3. **Fichier de sortie** :
   Les résultats seront enregistrés dans un fichier CSV intitulé `praticiens.csv` dans le même répertoire que le script. 
   Ce fichier contient les colonnes suivantes :
  
   * **Nom du praticien** : Le nom du praticien médical.
   * **Adresse** : L'adresse du praticien.