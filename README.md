# Random_text

## Ez egy Programozás Karrieres Gyakorló feladat

> Ez az egyszerű kis pythonban írt program azt a célt szolgálja, hogy megértsem, vagy megértessem a a filébe írást python nyelven. A program a felhasználótól bekér egy mondatot, azt rögzíti majd ezután véletlenül választ egy mondatott a data.txt filéből és azt kiírja a konzolra. Az alábbiakban részletesen ismertetem a program működését. (Kiegészítés: Az átláthatóság miatt a programban több helyen is a time metódussal várakoztatásra kerül a program)

### A program bekér a felhasználótól egy mondatot, amely string ként bekerül az „x” változóba.

![Szöveg bekérése](https://www.mrkocka.hu/github_img/01_Sz%c3%b6veg%20bek%c3%a9r%c3%a9se.jpg)

### Ezt követően a filemuvelet() nevű fügvény meghívásával a data.txt filébe kerül elmentésre a mondat.

> A felhasználó értesítést kap a művelet megkezéséről.

(img)
![megkezdodott](https://www.mrkocka.hu/github_img/02_megkezdodott.jpg)

> Valamint annak befejezéséről is

(img)
![befejezes](https://www.mrkocka.hu/github_img/03_befejez%c3%a9s.jpg)

### Ezt követően a program kiolvas egy random mondatot a data.txt filéből.

> A folyamat elkezdéséről értesíti a felhasználót (a véltelen választáshoz random metódust használtam):

(img)
![randomOlvasas](https://www.mrkocka.hu/github_img/04_randomOlvas%c3%a1s.jpg)

> Majd kiírja a választott értéket a konzolra.

(img)
![kiirtertek](https://www.mrkocka.hu/github_img/05_kiolvasott_mondat.jpg)

### A program futása itt leáll.
