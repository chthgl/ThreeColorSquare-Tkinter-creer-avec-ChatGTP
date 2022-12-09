# coding: utf-8
# ouvre le fichier en mode écriture
f = open("README.txt", "w")

# écrit le texte du fichier README dans le fichier
f.write("# Carrés animés\n\n")
f.write("Ce programme utilise la bibliothèque Tkinter pour créer une fenêtre contenant des carrés animés. Les carrés bougent aléatoirement sur la fenêtre et changent de couleur en fonction de leur collision.\n\n")
f.write("## Comment l'utiliser\n\n")
f.write("Pour utiliser ce programme, vous devez avoir Python et la bibliothèque Tkinter installés sur votre ordinateur. Une fois que ces prérequis sont satisfaits, vous pouvez exécuter le programme en utilisant la commande suivante dans votre terminal :\n\n")
f.write("```\n")
f.write("python squares.py\n")
f.write("```\n\n")
f.write("## Personnalisation\n\n")
f.write("Vous pouvez personnaliser certaines caractéristiques du programme en modifiant les valeurs des variables suivantes dans le code :\n\n")
f.write("- `SIZE` : détermine la taille des carrés en pixels\n")
f.write("- `SPEED` : détermine la vitesse de mouvement des carrés en millisecondes\n")
f.write("- `COLORS` : détermine les couleurs des carrés générés aléatoirement (les carrés bleu, violet et orange ont des couleurs fixes)\n\n")
f.write("## Auteur\n\n")
f.write("Le code ci-dessus a été généré par un modèle de langage appelé GPT-3 (également connu sous le nom de chatGPT). Il s'agit d'un modèle de langage entraîné sur des milliards de textes pour prédire le texte suivant en fonction du texte donné en entrée. Le code généré par GPT-3 est donc un exemple de texte prédit par le modèle à partir d'une description générale du programme.\n\n")

# ferme le fichier
f.close()
