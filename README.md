# Podešavanje lokalnog radnog okruženja

-   Upaliti powershell koristeći `WIN + R` i kucajući `powershell`
-   Navigirati na disk D: kucajući `D:`
-   Kreirati direktorijum sa vašim imenom i prezimenom kucajući
    `mkdir pera-peric`
-   Ući u dati repozitorijum kucajući `cd pera-peric`
-   Klonirati repozitorijum

```powershell
git clone <url-repozitorijuma>
```

-   Ući u repozitorijum kucajući `cd primer-pismenog`
-   Izvršiti sledeće komande

```powershell
pip install virtualenv
python -m virtualenv env
Set-ExecutionPolicy Unrestricted -Scope Process
env/Scripts/activate
pip install -r requirements.txt
flask --app oglasi run --debug
```

Trebalo bi da, nakon izvršavanja prethodnih komandi, se upali flask server na
portu `5000`.

# Zadaci

## 1. Registracija

Napisati unutar auth blueprint-a view za registraciju. Korisnik treba da unese:

1. Korisnicko ime
2. Email
3. Lozinku
4. Ponovljenu lozinku

Svi ovi podaci se salju kroz formu. Svaki od ovih podataka je neophodan. Server
treba proveriti da li se lozinka i ponovljena lozinka poklapaju. Ukoliko ne,
mora se prikazati greska korisniku. Nakon uspesne regisracije, treba korisnika
preusmeriti na login.

## 2. Sesija

Omoguciti da server prepoznaje klijenta koji je ulogovan koriscenjem sesija.
Sesija se kreira kada se korisnik uloguje, i brise kada se korisnik izloguje.
Pamti se samo user id u sesiji. Kada je korisnik ulogovan potrebno je prikazati
njegovo ime u gornjem desnom uglu i Logout link. Kada korisnik nije ulogovan,
prikazati Login i Register linkove.

## 3. Oglasi

Napraviti template-ove za kreiranje i izmenu oglasa. Oglas moze kreirati samo
ulogovani korisnik preko linka koji je samo njemu vidljiv na pocetnoj strani.
Oglas moze izmeniti samo korisnik koji je vlasnik oglasa. Nakon uspesnog
kreiranja oglasa, preusmerava se na view za taj oglas. Takodje i za uspesnu
izmenu oglasa.

## 4. User

Napraviti blueprint user. Napraviti template za pregled jednog korisnika. U tom
template-u prikazati sve oglase datog korisnika pocevsi od najskorijih nalik
`oglas/index.html` template-u. Njemu se moze pristupiti samo klikom na ime koje
je prikazano ulogovanom korisniku na vrhu stranice.
