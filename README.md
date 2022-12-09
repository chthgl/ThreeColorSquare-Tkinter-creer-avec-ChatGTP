# Carrés animés


Ce code utilise la bibliothèque Tkinter pour afficher des carrés qui bougent aléatoirement dans une fenêtre. Les carrés ont des couleurs aléatoires choisies parmi une liste de couleurs prédéfinies. Lorsqu'un carré entre en collision avec un autre carré, ils rebondissent l'un contre l'autre. Si les deux carrés ont la même couleur, ils deviennent noirs. Lorsque l'utilisateur clique sur un carré, sa couleur est choisie aléatoirement parmi les couleurs de la liste. Lorsque l'utilisateur déplace la souris sur un carré, sa couleur est également choisie aléatoirement.
## Pré-requis
Avant de pouvoir utiliser ce code, vous devez installer la bibliothèque Tkinter en utilisant pip: :


```

pip install tkinter

```

## Personnalisation


Le code utilise la bibliothèque Tkinter pour créer une fenêtre dans laquelle des carrés bougent aléatoirement. Les carrés ont des couleurs aléatoires choisies parmi une liste de couleurs prédéfinies, mais vous pouvez facilement modifier cette liste en modifiant la variable COLORS à la ligne 10:
```
COLORS = ["green", "yellow", "red"]```
```
Vous pouvez également modifier la taille des carrés en modifiant la variable SIZE à la ligne 6:

```
SIZE = 10
```

Lorsqu'un carré entre en collision avec un autre carré, ils rebondissent l'un contre l'autre. Si les deux carrés ont la même couleur, ils deviennent noirs. Vous pouvez désactiver ce comportement en commentant les lignes 44 à 46:f.write
```
if self.color == other_square.color:
    self.change_color("black
")
    other_square.change_color("black
")```

Lorsque l'utilisateur clique sur un carré, sa couleur est choisie aléatoirement parmi les couleurs de la liste. Vous pouvez désactiver ce comportement en commentant les lignes 28 à 31:
```
    def on_click(self, event):
        # Récupère les coordonnées de la souris lorsque l'événement "clic" est déclenché
        mouse_x = event.x
        mouse_y = event.y
        # Déclare clicked_square comme étant une variable globale
        global clicked_square
        # Initialise la variable clicked_square à None
        clicked_square = None
        # Pour chaque carré
        for square in squares:
            # Si la souris est à côté du carré (à une distance inférieure à la moitié de la taille du carré)
            if (abs(square.x - mouse_x) < SIZE and abs(square.y - mouse_y) < SIZE):
                # On stocke le carré dans une variable globale
                clicked_square = square
        if clicked_square is not None:
            clicked_square.change_color(choice(Square.COLORS)
```

Pour modifier les couleurs aléatoire aux clique vous pouvez modifier color ligne 10

```

COLORS = ["green", "yellow", "red", "blue", "purple", "orange"]```
```


## Auteur

Le code ci-dessus a été généré par un modèle de langage appelé GPT-3 (également connu sous le nom de chatGPT). Il s'agit d'un modèle de langage entraîné sur des milliards de textes pour prédire le texte suivant en fonction du texte donné en entrée. Le code généré par GPT-3 est donc un exemple de texte prédit par le modèle à partir d'une description générale du programme.

