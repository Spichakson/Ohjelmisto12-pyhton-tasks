pelin nimi: Kotkan most wanted
Artem Spichak

Peliidea: työnhaku tai työttömänä olo


## 4.9.2026

Tein kaikki moodulin 5 tehtävät, opiskelin while-käyttämisen ja muokin peliprojektintehtävää

## 9.9.26
Olen tehnyt 3 osan projektista. Lisäsin muutama funkiota ja listaa. Nyt hahmotan minun pelinideaa paremmpi. Se on työnhaku ta työttömyys.
Nyt ohjelmassa voi:
- Tallentaa käyttäjän tiedot(nimi, ikä ja alkuraha) ja aloita pelin funktion kautta.
- Navigoida päävalikossa
- Katsella työpaikkojen listaa
- Valita 4 työpaikka



# finaali

# Kotkan Most Wanted

**Kotkan Most Wanted** on suomenkielinen tekstipohjainen seikkailupeli. 

Pelin tavoitteena on auttaa päähahmoa keräämään tarvittavat rahat ja pakenemaan Kotkasta 3 päivän kuluessa. Pelaajan tulee hallita resurssejaan (raha, moraali, aika) ja suorittaa erilaisia toimintoja eri sijainneissa.

---

## Projektin rakenne (Modules & Files)

Projekti on jaettu selkeisiin moduuleihin ja tiedostoihin hyvien ohjelmointikäytäntöjen mukaisesti:

* **`main.py`** — Pelin pääaloitustiedosto (Entry point). Käynnistää pelimaailman alustuksen, päävalikon ja pelisilmukan.
* **`functions.py`** — Sisältää pelimekaniikan, tiedostojen käsittelyn (tallennus/lataus, tekstitiedostojen luku), päävalikon sekä pelin pääsilmukan (`game_loop`).
* **`modules.py`** — Sisältää olio-ohjelmoinnin (OOP) luokat (`Player`, `Room`, `Item`).
* **`intro.txt`** — Pelin alustusteksti ja tarinan johdanto.
* **`instructions.txt`** — Pelin ohjeet ja säännöt pelaajalle.
* **`savegame.json`** — Automaattisesti luotava JSON-tiedosto pelitilanteen tallentamista varten.

---

## Olio-ohjelmointi (Object-Oriented Structure)

Peli käyttää olio-ohjelmointia (OOP) pelimaailman entiteettien mallintamiseen:

### 1. `Player` (Pelaaja)
* **Ominaisuudet (Properties):** 
  * `name` (nimi), `money` (rahat), `morale` (moraali, 0-100)
  * `day` (päivä, max 3)
  * `location` (nykyinen `Room`-olio)
  * `inventory` (lista `Item`-olioista)
  * `has_eaten` (boolean-lippu: rajoittaa syömisen 1 kertaan päivässä)
* **Toiminnot (Methods):** `move()`, `collect_item()`, `use_item()`, `eat()`, `sleep()`, `work()`, `buy_ticket()`, `player_info()`.

### 2. `Room` (Sijainti / Huone)
* **Ominaisuudet (Properties):** 
  * `name` (nimi), `info` (kuvaus)
  * `items` (lista huoneessa olevista `Item`-olioista)
  * `exits` (sanakirja mahdollisista kulkusuunnista muihin huoneisiin)
  * `actions` (lista toiminnallisista komennoista tässä huoneessa)
* **Toiminnot (Methods):** `add_item()`, `remove_item()`.

### 3. `Item` (Esine)
* **Ominaisuudet (Properties):** 
  * `name` (nimi), `weight` (paino)
  * `item_type` (tyyppi: esim. `food`, `key`)
  * `morale_bonus` (moraalibonus syötäville esineille)

---

## Tiedostojen käsittely (File Handling)

Projektissa on toteutettu tiedostojen luku ja kirjoitus:

1. **Tekstitiedostojen luku (`intro.txt` & `instructions.txt`):**
   * Pelin alussa `show_intro_and_instructions()`-funktio lukee johdantotekstit erillisistä `.txt`-tiedostoista ja näyttää ne pelaajalle.
2. **Pelin tallennus ja lataus (`savegame.json`):**
   * Pelaaja voi tallentaa pelitilanteensa valitsemalla komennon `Tallenna peli`.
   * Tallennus muuntaa pelaajan tilan (nimi, rahat, moraali, päivä, sijainti ja reppusisältö) `JSON`-muotoon ja tallentaa sen tiedostoon `savegame.json`.
   * Päävalikosta valitsemalla `2 - Lataa peli` peli palauttaa tallennetun tilanteen ja pelaaja voi jatkaa siitä, mihin jäi.

---

## Pelimekaniikka ja säännöt

* **Aikaraja:** Pelaajalla on 3 päivää aikaa hankkia lentolippu.
* **Moraali:** Jos moraali laskee alle 20, peli päättyy häviöön.
* **Syöminen:** Voit syödä vain **kerran päivässä** (moraali nousee). Syömisrajoitus nollautuu, kun pelaaja nukkuu (`nukkua`).
* **Voitto:** Voitat pelin ostamalla lentolipun kaupasta (`Kauppa`), kun sinulla on riittävästi rahaa.

---

##  Käynnistys ja pelaaminen

1. Varmista, että tietokoneellesi on asennettu Python 3.
2. Suorita pääohjelma komennolla:
   ```bash
   python main.py