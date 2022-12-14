## Viikko 3

- Käyttäjä voi luoda tilin ja kirjautua sisään antamalla käyttäjänimen ja salasanan
- Lisätty User-luokka joka mallintaa käyttäjätiliä
- Lisätty UserDatabase-luokka joka toimii tietokannan hallintaluokkana, tässävaiheessa pitää datan vasta listassa
- Lisätty UserManager-luokka joka mahdollistaa uuden käyttäjätunnuksen luonnin sekä sisäänkirjautumisen
- Lisäksi lisätty consoleIO-luokka sekä PasswordManagerApp-luokka jotka yhdessä ovat vastuussa käyttöliittymästä, joka on tässävaiheessa vielä terminaali, mutta joka muutetaan visuaaliseksi myöhemmillä viikoilla
- Testattu, että UserManager-luokassa voi luoda käyttäjätunnuksen ja kirjautua sisään

## Viikko 4

- UserManager uudelleennimetty UserService luokaksi ja toiminnallisuus salasana/app kombinaation lisäämiseen, poistoon ja listaamiseen lisätty
- UserDatabase poistettu koska siitä tuli turha
- UserRepository luokka lisätty joka sisältää funktioita SQLite tietokannan lukemiseen ja tallentamiseen
- PasswordRepository luokka lisätty joka sisältää funktioita SQLite tietokannan lukemiseen ja tallentamiseen
- User luokka eriytetty omaan tiedostoon Entities kansioon
- Password luokka luotu joka sisältää salasanan luoman käyttäjätunnuksen, sovelluksen, sekä salasanan
- Database connection ja initialization tiedostot luotu jotka auttavat yhdistämään ja alustamaan/luomaan SQLite tietokannan
- PasswordManagerApp luokkaan lisätty uusi näkymä käyttäjälle ja status sisäänkirjautumisesta joka mahdollistaa käyttäjän kokemuksen eriyttämisen koti sekä kirjautumis-näkymiin
- Testi lisätty että samalla käyttäjänimellä ei voi tehdä kahta käyttäjätiliä
- Testi lisätty että väärällä salasanalla ei voi kirjautua
- Testi lisätty että UserRepository löytää kaikkien käyttäjien tiedot

## Viikko 5

- UI luokka luotu tkinter käyttöliittymää toteuttamaan
- LoginView ja CreateAccountView luokat luotu
- PasswordsView ja PasswordListView luokat luotu
- Visuaalinen käyttöliittymä toteutettu sisäänkirjautumiselle
- Visuaalinen käyttöliittymä toteutettu käyttäjän luomiselle
- Visuaalinen käyttöliittymä toteutettu salasanan luomiselle sekä poistamiselle
- UserService luokkaan toteutettu get_current_user ja logout metodit
- Testi lisätty että käyttäjä voi lisätä salasanan
- Testi lisätty että käyttäjä voi poistaa salasanan

## Viikko 6

- TKInter käyttöliittymään lisätty custom theme ttkthemes pakettia hyödyntäen
- käyttöliittymään lisätty Error notifikaatio jos salasana/käyttäjänimi väärin
- käyttöliittymään lisätty Error notifikaatio jos käyttäjätunnuksen luonnissa nimi tai salasana input tyhjiä
- käyttöliittymään lisätty Error notifikaatio jos käyttäjätunnuksen luonnissa nimi on jo varattu
- käyttöliittymään lisätty Error notifikaatio jos salasanan lisäyksessä app tai salasana input tyhjiä
- PasswordsView luokkaan luotu metodi _handle_generate_password joka autogeneroi 16 characterin random salasanan
- PasswordListView luokkaan luotu metodi _copy_to_clipboard_handler joka kopioi halutun salasanan clipboardiin
- Testi lisätty että salasanojen hakeminen tietyllä käyttäjällä palauttaa kaikki käyttäjän salasanat
- Testi lisätty että UserService palauttaa sisäänkirjautuneen käyttäjän tiedot metodilla get_current_user
- Arkkitehtuuri dokumentaation kirjoittaminen aloitettu
- Docstring dokumentaatio lisätty 90% luokista ja metodeista
- Käyttöohje kirjoitettu

## Loppupalautus

- Käyttäjien master-passwordit eli salasanat joilla he kirjautuvat sovellukseen encryptattu bcrypt kirjastolla
- Lisätty metodi update_password PasswordRepository luokkaan (jonkin sovelluksen) salasanan vaihtamiseen käyttäen sqliten UPDATE komentoa
- Lisätty luokka EncryptionService joka toteuttaa bcrypt kirjatoa käyttäen salasanojen encryptoinnin
- Eriytetty käyttäjien ja käyttäjän salasanojen hallinnointi UserService ja PasswordService luokkiin (ennen UserService vastasi molemmista)
- PasswordService luokkaan siirretty UserService luokasta kuuluvat metodit ja lisätty change_password salasanan muuttamiseen
- UserService luokan authenticate ja create_account metodeja muutettu toteuttamaan encryptaus ja encryptatun salasanana tallentaminen tietokantaan
- Bugi korjattu missä käyttäjä voi lisätä samalle sovelluksen nimelle (esim Google) kaksi eri salasanaa, toteutettu varmistamalla että sovelluksen nimi on uniikki tietokannassa kun lisätään uutta salasanaa käyttäjän toimesta
- Toteutettu PasswordListView luokkaan muutoksia joka mahdollistaa salasanojen muuttamisen luonnin jälkeen 
- Lisätty toiminnallisuus että käyttäjätunnuksen luonnissa käyttäjä kirjataan automaattisesti sisään, eli sovellus ei vaadi tunnuksen luonnin jälkeen sisäänkirjautumista
