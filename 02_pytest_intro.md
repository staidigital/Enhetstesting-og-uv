## Din første test

Lag en ny fil med navn `kalkulator.py` og lag en funksjon for addisjon. 
`kalkulator.py`:
```python
def addisjon(a, b):
    return a + b
```

Lag deretter en `test_kalkulator.py`-fil, der vi skriver 2 tester for å sjekke om addisjon-funksjonen vår fungerer:

`test_kalkulator.py`:
```python
from kalkulator import addisjon

def test_addisjon():
    resultat = addisjon(2, 3)
    assert resultat == 5
    
def test_addisjon_negative_tall():
    resultat = addisjon(-1, -1)
    assert resultat == -2
```
For å kjøre testene våre, går vi til terminalen og skriver:

```bash
pytest test_kalkulator.py -v
```

### Oppgave
Lag funksjoner for subtraksjon, divisjon og multiplikasjon i `kalkulator.py` og skriv tilhørende tester for disse funksjonene. Gjerne legg inn noen feil, slik at du får se hva som skjer når ting går galt. 
**Utfordring:** Hva skjer hvis vi deler på null? Hvordan kan vi teste dette?

## Lage coverage-rapport
Om man ønsker en litt mer detaljert oversikt over testingen, kan vi bruke pytest-cov til å lage en html-fil med litt flere detaljer. 

```bash
pytest --cov=. --cov-report=html
```

