# webscraping
Un repo contenant mes scripts de web scraping.

Susceptibles de fonctionner ou non , ne vous attendez pas à la moindre assistance technique de ma part.

# Contenu:
* jvc_topic_watcher.py
* insta_followers_scraper.py
# jvc_topic_watcher.py:
# Utilisation
 python3 jvc_topic_watcher.py 

Un script Python3 s'appuyant sur requests et bs4 pour récupérer les sujets de la première page du Forum Blabla 18-25 ans de Jeuxvideo.com.

> Parfaitement inutile donc absolument indispensable.

Utilise aussi pynput pour arrêter l'éxecution à l'appui de la touche q

Peut-être importé comme un module à la conditions que ses dépendances soient installées

# insta_followers_scraper.py:
# Utilisation
1)Remplacer mail et password dans la fonction main par les identifiants d'un compte instagram valide qui se connectera pour scraper les followers, changer l'user agent si nécessaire (variable uastring)

2)python3 insta_followers_scraper.py "page_a_scraper" 

Un script Python3 s'apppuyant sur Selenium pour récupérer la liste de follower d'un compte Instagram donné.

//TODO

* Ajouter le requirements.txt

* Ajouter la possibilité de récupérer plusieurs pages en même temps

* Implémenter le parsing d'arguments
