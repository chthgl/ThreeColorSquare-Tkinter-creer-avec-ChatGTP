# Carr�s anim�s

Ce code utilise la biblioth�que Tkinter pour afficher des carr�s qui bougent al�atoirement dans une fen�tre. Les carr�s ont des couleurs al�atoires choisies parmi une liste de couleurs pr�d�finies. Lorsqu'un carr� entre en collision avec un autre carr�, ils rebondissent l'un contre l'autre. Si les deux carr�s ont la m�me couleur, ils deviennent noirs. Lorsque l'utilisateur clique sur un carr�, sa couleur est choisie al�atoirement parmi les couleurs de la liste. Lorsque l'utilisateur d�place la souris sur un carr�, sa couleur est �galement choisie al�atoirement.## Pr�-requisAvant de pouvoir utiliser ce code, vous devez installer la biblioth�que Tkinter en utilisant pip: :

```
pip install tkinter
```

## Personnalisation

Le code utilise la biblioth�que Tkinter pour cr�er une fen�tre dans laquelle des carr�s bougent al�atoirement. Les carr�s ont des couleurs al�atoires choisies parmi une liste de couleurs pr�d�finies, mais vous pouvez facilement modifier cette liste en modifiant la variable COLORS � la ligne 10:```
COLORS = ["green", "yellow", "red"]```
Vous pouvez �galement modifier la taille des carr�s en modifiant la variable SIZE � la ligne 6:```
SIZE = 10```
Lorsqu'un carr� entre en collision avec un autre carr�, ils rebondissent l'un contre l'autre. Si les deux carr�s ont la m�me couleur, ils deviennent noirs. Vous pouvez d�sactiver ce comportement en commentant les lignes 44 � 46:f.write```
if self.color == other_square.color:
    self.change_color("black")
    other_square.change_color("black")```
Lorsque l'utilisateur clique sur un carr�, sa couleur est choisie al�atoirement parmi les couleurs de la liste. Vous pouvez d�sactiver ce comportement en commentant les lignes 28 � 31:```
    def on_click(self, event):
        # R�cup�re les coordonn�es de la souris lorsque l'�v�nement "clic" est d�clench�
        mouse_x = event.x
        mouse_y = event.y
        # D�clare clicked_square comme �tant une variable globale
        global clicked_square
        # Initialise la variable clicked_square � None
        clicked_square = None
        # Pour chaque carr�
        for square in squares:
            # Si la souris est � c�t� du carr� (� une distance inf�rieure � la moiti� de la taille du carr�)
            if (abs(square.x - mouse_x) < SIZE and abs(square.y - mouse_y) < SIZE):
                # On stocke le carr� dans une variable globale
                clicked_square = square
        if clicked_square is not None:
            clicked_square.change_color(choice(Square.COLORS)
        ```
Pour modifier les couleurs al�atoire aux clique vous pouvez modifier color ligne 10
```
COLORS = ["green", "yellow", "red", "blue", "purple", "orange"]```


## Auteur

Le code ci-dessus a �t� g�n�r� par un mod�le de langage appel� GPT-3 (�galement connu sous le nom de chatGPT). Il s'agit d'un mod�le de langage entra�n� sur des milliards de textes pour pr�dire le texte suivant en fonction du texte donn� en entr�e. Le code g�n�r� par GPT-3 est donc un exemple de texte pr�dit par le mod�le � partir d'une description g�n�rale du programme.

