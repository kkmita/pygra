Sokoban - implementacja gry na PADPy 2017/2018
============================================

Repozytorium `pygra` zawiera moją implementację gry z gatunku 'Sokoban'
napisaną w języku Python z użyciem pakiety `pygame`

### Zasady gry:

Gracz musi za pomocą ruchów {lewo, prawo, dół, góra} przesunąć niebieskie skrzynki
w na podłodze wyznaczone przez odpowiednie oznaczenia.

Gracz może przesunąć skrzynkę w dowolnym kierunku tylko wtedy, gdy żaden obiekt nie blokuje
takiego przesunięcia (także: inna skrzynka)

### Używane klawisze:

  * `↑` - ruch w górę
  * `↓` - ruch w dół
  * `←` - ruch w lewo
  * `→` - ruch w prawo
  * `r` - reset gry, tj. wyjście z gry do menu wyboru poziomów


### Jak zacząć grę:

Należy uruchomić plik `gamegui.py`.

Na początku dostępny jest jedynie pierwszy z ośmiu poziomów gry.
<br> Kolejne poziomy są sukcesywnie odblokowywane przez gracza po ukończeniu poprzedniego.
<br> Aby ułatwić sobie jednak zabawę, w głównym menu gry możemy wejść w opcje *Zmień uczciwość*
i kliknięciem klawisza `Enter` po nakierowaniu na odpowiednią opcję - odblokować wszystkie dostępne
poziomy.

### Znużony, nie potrafisz przejść etapu?

Na tej stronie znajdziesz rozwiązania innych graczy poszczególnych etapów.<br>
http://ysokoban.atspace.eu/sdb/dskinnersas1.html<br>
Są to (licząc od 3 etapu w mojej grze) kolejno poziomy:<br>
1, 2, 6, 9, 11, 15

### Grafiki oraz konstrukcje poziomów zostały zaczerpnięte z poniższych źródeł:

**mapy**
<br>
Autor: David W. Skinner
Źródło: http://www.onlinespiele-sammlung.de/sokoban/sokobangames/skinner/s1.txt
Licencja: brak, tj. autor umieścił zezwolenie na wykorzystanie jego pomysłow pod warunkiem credits:
<br> "These sets may be freely distributed provided they remain properly credited."

**grafika**
Autor: Kenney Vleugels
Źródło: https://kenney.nl/assets/sokoban
Licencja: Creative Commons Zero, CC0


English version
=========================
Repo `pygra` contains my implementation of Sokoban-type game
written in Python and its module `pygame`.

### Rules:

Player must move the blue boxes onto tiles signed with appropiate signs
usign {left, right, up, down} moves.

Player can move the box only if the tile that the box is about to be on
is not occupied by any other object (that is another box too)

### Keys:

  * `↑` - up
  * `↓` - down
  * `←` - left
  * `→` - right
  * `r` - reset of the level - level menu
  
  
### How to start:

Start the `gamegui.py` programme.

At the beginning, only the first level is available. You must
pass subsequent levels to unblock the next ones.
<br> If you cannot do that (or you are impatient), you can unblock
all the levels with the *Zmien uczciwosc* option in main menu.

### Looking for solution of level?

You will find solutions to levels: from 3 to 8 on the site:
<br>http://ysokoban.atspace.eu/sdb/dskinnersas1.html
<br> The number (1, 2, 6, 9, 11, 15) are relevant for such
levels in my game: (3, 4, 5, 6, 7, 8)


### Credits for graphics and levels

**maps**
<br>
Author: David W. Skinner
Source: http://www.onlinespiele-sammlung.de/sokoban/sokobangames/skinner/s1.txt
Licence: author allowed for using his ideas if credits are given:
<br> "These sets may be freely distributed provided they remain properly credited."

**graphics**
Author: Kenney Vleugels
Source: https://kenney.nl/assets/sokoban
Licence: Creative Commons Zero, CC0

