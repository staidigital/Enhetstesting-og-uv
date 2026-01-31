# Del 3: Mer pytest-grunnlag

## Testing av flere typer funksjoner

Nå som vi har testet enkle mattematiske operasjoner, skal vi se på andre typer funksjoner som er vanlige i hverdagsprogrammering.

### Tekstbehandling

Lag en ny fil `tekstfunksjoner.py`:

```python
def reverser_tekst(tekst):
    """Reverserer en tekststreng"""
    return tekst[::-1]

def tell_bokstaver(tekst):
    """Teller antall bokstaver (ignorerer mellomrom og tegnsetting)"""
    return sum(1 for char in tekst if char.isalpha())

def stor_forbokstav(tekst):
    """Gjør første bokstav stor"""
    return tekst.capitalize()

def fjern_mellomrom(tekst):
    """Fjerner alle mellomrom fra teksten"""
    return tekst.replace(" ", "")
```

Lag tilhørende testfil `test_tekstfunksjoner.py`:

```python
from tekstfunksjoner import reverser_tekst, tell_bokstaver, stor_forbokstav, fjern_mellomrom

def test_reverser_tekst():
    resultat = reverser_tekst("hei")
    assert resultat == "ieh"

def test_reverser_tekst_med_mellomrom():
    resultat = reverser_tekst("hei på deg")
    assert resultat == "ged åp ieh"

def test_tell_bokstaver():
    resultat = tell_bokstaver("hei på deg")
    assert resultat == 8  # h-e-i-p-å-d-e-g

def test_tell_bokstaver_med_tall():
    resultat = tell_bokstaver("abc123")
    assert resultat == 3  # kun a-b-c

def test_stor_forbokstav():
    resultat = stor_forbokstav("hei")
    assert resultat == "Hei"

def test_fjern_mellomrom():
    resultat = fjern_mellomrom("hei på deg")
    assert resultat == "heipådeg"
```

Kjør testene:
```bash
pytest test_tekstfunksjoner.py -v
```

### Oppgave 1
Legg til følgende funksjoner i `tekstfunksjoner.py` og skriv tester for dem:
- `tell_ord(tekst)` - teller antall ord (hint: bruk `.split()`)
- `er_palindrom(tekst)` - sjekker om en tekst er det samme forlengs og baklengs (ignorer store/små bokstaver)

---

## Testing av lister

Lag en ny fil `liste_funksjoner.py`:

```python
def finn_storste(tall_liste):
    """Finner det største tallet i en liste"""
    return max(tall_liste)

def finn_minste(tall_liste):
    """Finner det minste tallet i en liste"""
    return min(tall_liste)

def summer_liste(tall_liste):
    """Summerer alle tall i en liste"""
    return sum(tall_liste)

def gjennomsnitt(tall_liste):
    """Beregner gjennomsnittet av tallene i listen"""
    return sum(tall_liste) / len(tall_liste)

def filtrer_partall(tall_liste):
    """Returnerer bare partallene fra listen"""
    return [tall for tall in tall_liste if tall % 2 == 0]
```

Lag `test_liste_funksjoner.py`:

```python
from liste_funksjoner import finn_storste, finn_minste, summer_liste, gjennomsnitt, filtrer_partall

def test_finn_storste():
    resultat = finn_storste([1, 5, 3, 9, 2])
    assert resultat == 9

def test_finn_storste_negative_tall():
    resultat = finn_storste([-5, -1, -10, -3])
    assert resultat == -1

def test_finn_minste():
    resultat = finn_minste([1, 5, 3, 9, 2])
    assert resultat == 1

def test_summer_liste():
    resultat = summer_liste([1, 2, 3, 4, 5])
    assert resultat == 15

def test_gjennomsnitt():
    resultat = gjennomsnitt([2, 4, 6, 8])
    assert resultat == 5.0

def test_filtrer_partall():
    resultat = filtrer_partall([1, 2, 3, 4, 5, 6])
    assert resultat == [2, 4, 6]

def test_filtrer_partall_ingen_partall():
    resultat = filtrer_partall([1, 3, 5, 7])
    assert resultat == []
```

### Oppgave 2
Legg til følgende funksjoner og skriv tester:
- `tell_oddetall(tall_liste)` - teller hvor mange oddetall det er i listen
- `doble_verdier(tall_liste)` - returnerer en ny liste der alle verdier er doblet
- `fjern_duplikater(liste)` - returnerer listen uten duplikater

---

## Testing av betingelser og boolean-funksjoner

Lag en fil `validering.py`:

```python
def er_partall(tall):
    """Sjekker om et tall er partall"""
    return tall % 2 == 0

def er_positivt(tall):
    """Sjekker om et tall er positivt"""
    return tall > 0

def er_i_intervall(tall, min_verdi, max_verdi):
    """Sjekker om et tall er mellom min og max"""
    return min_verdi <= tall <= max_verdi

def er_gyldig_alder(alder):
    """Sjekker om alder er mellom 0 og 150"""
    return 0 <= alder <= 150
```

Lag `test_validering.py`:

```python
from validering import er_partall, er_positivt, er_i_intervall, er_gyldig_alder

def test_er_partall_sant():
    assert er_partall(4) == True

def test_er_partall_usant():
    assert er_partall(5) == False

def test_er_partall_null():
    assert er_partall(0) == True

def test_er_positivt_sant():
    assert er_positivt(5) == True

def test_er_positivt_usant():
    assert er_positivt(-5) == False

def test_er_positivt_null():
    assert er_positivt(0) == False

def test_er_i_intervall_inne():
    assert er_i_intervall(5, 1, 10) == True

def test_er_i_intervall_grense():
    assert er_i_intervall(1, 1, 10) == True
    assert er_i_intervall(10, 1, 10) == True

def test_er_i_intervall_utenfor():
    assert er_i_intervall(11, 1, 10) == False

def test_er_gyldig_alder():
    assert er_gyldig_alder(25) == True
    assert er_gyldig_alder(0) == True
    assert er_gyldig_alder(150) == True
    assert er_gyldig_alder(-1) == False
    assert er_gyldig_alder(151) == False
```

### Oppgave 3
Lag funksjoner som validerer:
- `er_gyldig_karakter(karakter)` - sjekker om karakteren er mellom 1 og 6
- `er_voksen(alder)` - sjekker om alder er 18 eller over
- `er_skuddaar(aar)` - sjekker om et år er skuddår (delelig med 4, men ikke 100, med mindre også delelig med 400)

---

## Testing av funksjoner som bruker andre funksjoner

La oss lage funksjoner som bygger på hverandre:

`temperatur.py`:
```python
def celsius_til_fahrenheit(celsius):
    """Konverterer Celsius til Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_til_celsius(fahrenheit):
    """Konverterer Fahrenheit til Celsius"""
    return (fahrenheit - 32) * 5/9

def er_frysepunkt(celsius):
    """Sjekker om temperaturen er ved eller under frysepunktet"""
    return celsius <= 0

def temperatur_beskrivelse(celsius):
    """Gir en beskrivelse av temperaturen"""
    if celsius < 0:
        return "Kaldt"
    elif celsius < 15:
        return "Kjølig"
    elif celsius < 25:
        return "Behagelig"
    else:
        return "Varmt"
```

`test_temperatur.py`:
```python
from temperatur import celsius_til_fahrenheit, fahrenheit_til_celsius, er_frysepunkt, temperatur_beskrivelse

def test_celsius_til_fahrenheit_null():
    resultat = celsius_til_fahrenheit(0)
    assert resultat == 32

def test_celsius_til_fahrenheit_kokepunkt():
    resultat = celsius_til_fahrenheit(100)
    assert resultat == 212

def test_fahrenheit_til_celsius():
    resultat = fahrenheit_til_celsius(32)
    assert resultat == 0

def test_rundtur_konvertering():
    """Tester at vi får samme verdi ved å konvertere frem og tilbake"""
    original = 20
    fahrenheit = celsius_til_fahrenheit(original)
    tilbake = fahrenheit_til_celsius(fahrenheit)
    assert abs(tilbake - original) < 0.01  # Tillater små avrundingsfeil

def test_er_frysepunkt_null():
    assert er_frysepunkt(0) == True

def test_er_frysepunkt_under():
    assert er_frysepunkt(-5) == True

def test_er_frysepunkt_over():
    assert er_frysepunkt(5) == False

def test_temperatur_beskrivelse():
    assert temperatur_beskrivelse(-5) == "Kaldt"
    assert temperatur_beskrivelse(10) == "Kjølig"
    assert temperatur_beskrivelse(20) == "Behagelig"
    assert temperatur_beskrivelse(30) == "Varmt"
```

### Oppgave 4
Lag et lite konverteringssystem for lengdemål:
- `meter_til_km(meter)`
- `km_til_meter(km)`
- `meter_til_miles(meter)` (1 mile = 1609.34 meter)
- `er_lang_distanse(meter)` - returnerer True hvis over 5 km

---

## Testing av edge cases (grensetilfeller)

Det er viktig å teste spesielle tilfeller som kan skape problemer:

`test_edge_cases.py`:
```python
from kalkulator import divisjon, addisjon
from liste_funksjoner import gjennomsnitt, finn_storste

def test_divisjon_med_desimaler():
    """Tester divisjon som gir desimaltall"""
    resultat = divisjon(7, 3)
    assert abs(resultat - 2.333) < 0.01  # Sjekker med toleranse

def test_addisjon_store_tall():
    """Tester med veldig store tall"""
    resultat = addisjon(999999999, 1)
    assert resultat == 1000000000

def test_tom_liste_gir_feil():
    """Hva skjer med en tom liste?"""
    try:
        gjennomsnitt([])
        assert False, "Skulle ha kastet en feil!"
    except:
        assert True  # Vi forventer en feil

def test_liste_med_ett_element():
    resultat = finn_storste([42])
    assert resultat == 42
```

### Oppgave 5
Test følgende edge cases for funksjonene dine:
- Hva skjer med tomme strenger i tekstfunksjonene?
- Hva skjer med tomme lister?
- Hva skjer med veldig store eller veldig små tall?
- Test funksjoner med negative tall der det gir mening

---

## Kjør alle testene

Nå som du har mange testfiler, kan du kjøre alle sammen:

```bash
pytest -v
```

Eller kjøre en spesifikk fil:
```bash
pytest test_tekstfunksjoner.py -v
```

Se coverage for alt:
```bash
pytest --cov=. --cov-report=html
```
