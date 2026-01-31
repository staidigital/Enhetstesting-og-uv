# Del 4: Testing av Exceptions og Parametriserte Tester

## Introduksjon

I denne delen skal vi lære to viktige konsepter i enhetstesting:
1. **Testing av exceptions** - hvordan verifisere at koden håndterer feil på riktig måte
2. **Parametriserte tester** - hvordan kjøre samme test med mange forskjellige verdier

## 1. Testing av Exceptions

### Hvorfor teste exceptions?

God kode håndterer feilsituasjoner på en kontrollert måte. Når noe går galt, skal programmet:
- Gi tydelige feilmeldinger
- Kaste riktig type exception
- Ikke krasje uventet

### Eksempel: Bankkonto

```python
class Bankkonto:
    def __init__(self, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo kan ikke være negativ")
        self.saldo = saldo
    
    def ta_ut(self, belop):
        if belop <= 0:
            raise ValueError("Beløp må være positivt")
        if belop > self.saldo:
            raise ValueError("Ikke nok penger på konto")
        self.saldo -= belop
        return self.saldo
```

### Teste exceptions med pytest

Pytest bruker `pytest.raises()` for å teste at exceptions blir kastet:

```python
import pytest

def test_negativ_startsaldo():
    # Forvent at ValueError kastes
    with pytest.raises(ValueError):
        Bankkonto(saldo=-100)

def test_ta_ut_for_mye():
    konto = Bankkonto(saldo=100)
    with pytest.raises(ValueError):
        konto.ta_ut(200)
```

### Teste feilmeldinger

Du kan også verifisere selve feilmeldingen:

```python
def test_feilmelding_ved_negativt_belop():
    konto = Bankkonto(saldo=100)
    with pytest.raises(ValueError, match="Beløp må være positivt"):
        konto.ta_ut(-50)
```

## 2. Parametriserte Tester

### Problemet

Ofte vil vi teste samme logikk med mange forskjellige verdier:

```python
def test_alderssjekk_13():
    assert er_gammel_nok(13, aldersgrense=13) == True

def test_alderssjekk_12():
    assert er_gammel_nok(12, aldersgrense=13) == False

def test_alderssjekk_14():
    assert er_gammel_nok(14, aldersgrense=13) == True
```

Dette blir mye repetisjon! 😫

### Løsningen: @pytest.mark.parametrize

```python
import pytest

@pytest.mark.parametrize("alder,aldersgrense,forventet", [
    (13, 13, True),   # Akkurat på grensen
    (14, 13, True),   # Over grensen
    (12, 13, False),  # Under grensen
    (18, 18, True),   # Voksen
    (17, 18, False),  # Nesten voksen
])
def test_alderssjekk(alder, aldersgrense, forventet):
    resultat = er_gammel_nok(alder, aldersgrense)
    assert resultat == forventet
```


### Navngi testcases

Du kan gi testcases lesbare navn:

```python
@pytest.mark.parametrize("alder,aldersgrense,forventet", [
    (13, 13, True),
    (12, 13, False),
], ids=["akkurat_gammel_nok", "for_ung"])
def test_alderssjekk(alder, aldersgrense, forventet):
    assert er_gammel_nok(alder, aldersgrense) == forventet
```

## 3. Kombinere Exceptions og Parametrisering

Du kan også parametrisere tester som forventer exceptions:

```python
@pytest.mark.parametrize("belop,feilmelding", [
    (-50, "Beløp må være positivt"),
    (0, "Beløp må være positivt"),
    (200, "Ikke nok penger på konto"),
])
def test_ugyldige_uttak(belop, feilmelding):
    konto = Bankkonto(saldo=100)
    with pytest.raises(ValueError, match=feilmelding):
        konto.ta_ut(belop)
```

## Oppgaver

### Oppgave 1: E-postvalidering

Lag en funksjon `er_gyldig_epost(epost)` som returnerer `True` hvis e-posten er gyldig, ellers `False`.

**Regler:**
- Må inneholde nøyaktig én `@`
- Må ha minst ett tegn før `@`
- Må ha minst ett tegn etter `@`
- Må inneholde minst ett `.` etter `@`

**Oppgave:**
1. Implementer funksjonen `er_gyldig_epost()`
2. Skriv parametriserte tester som tester minst 8 forskjellige e-postadresser (både gyldige og ugyldige)

**Tips til testcases:**
- `test@example.com` (gyldig)
- `test@example` (ugyldig - mangler punktum)
- `@example.com` (ugyldig - mangler brukernavn)
- `testexample.com` (ugyldig - mangler @)
- osv.

### Oppgave 2: Passordvalidering

Lag en funksjon `valider_passord(passord)` som kaster `ValueError` hvis passordet ikke er sterkt nok.

**Regler:**
- Minimum 8 tegn
- Må inneholde minst én stor bokstav
- Må inneholde minst ett tall
- Hvis noen regel brytes, kast `ValueError` med beskrivende melding

**Oppgave:**
1. Implementer funksjonen `valider_passord()`
2. Skriv tester som sjekker at riktige exceptions kastes for:
   - For kort passord → "Passord må være minst 8 tegn"
   - Mangler stor bokstav → "Passord må inneholde stor bokstav"
   - Mangler tall → "Passord må inneholde minst ett tall"
   - Gyldig passord → ingen exception

**Tips:** Bruk parametriserte tester for å teste mange ugyldige passord!

### Oppgave 3: Temperaturkonvertering

Lag en funksjon `celsius_til_fahrenheit(celsius)` som konverterer fra Celsius til Fahrenheit.

**Formel:** F = C × 9/5 + 32

**Spesialkrav:**
- Kast `ValueError` hvis temperaturen er under absolutt nullpunkt (-273.15°C)
- Feilmelding: "Temperatur kan ikke være under absolutt nullpunkt"

**Oppgave:**
1. Implementer funksjonen
2. Skriv parametriserte tester for minst 5 gyldige temperaturer
3. Skriv tester for ugyldige temperaturer (under absolutt nullpunkt)

**Testcases å inkludere:**
- 0°C = 32°F
- 100°C = 212°F
- -40°C = -40°F (de møtes!)
- 37°C = 98.6°F (kroppstemperatur)
- -273.15°C (akkurat på grensen)
- -300°C (ugyldig)

### Oppgave 4: Alderskategori (Ekstra utfordring)

Lag en funksjon `finn_alderskategori(alder)` som returnerer alderskategori basert på alder:

**Kategorier:**
- 0-12: "Barn"
- 13-17: "Ungdom"
- 18-66: "Voksen"
- 67+: "Pensjonist"

**Unntak:**
- Negativ alder → kast `ValueError` med melding "Alder kan ikke være negativ"
- Alder over 150 → kast `ValueError` med melding "Ugyldig alder"

**Oppgave:**
1. Implementer funksjonen
2. Skriv parametriserte tester som dekker:
   - Minst én verdi i hver kategori
   - Grenseverdier (akkurat på overgangene)
   - Ugyldige verdier (negative og for høye)

## Tips til Testing

### 1. Test grenseverdier
Når du tester, husk å teste:
- Verdier akkurat på grensen
- Verdier rett over grensen
- Verdier rett under grensen

### 2. Bruk beskrivende navn på testcases
```python
@pytest.mark.parametrize("alder,forventet", [
    (12, "Barn"),
    (13, "Ungdom"),
], ids=["siste_barneaar", "forste_ungdomsaar"])
```

### 3. Test én ting om gangen
Hver test skal teste én spesifikk ting. Ikke bland testing av exceptions og normale verdier i samme test.

### 4. Bruk `match` for å verifisere feilmeldinger
```python
with pytest.raises(ValueError, match="spesifikk feilmelding"):
    # kode som skal feile
```

## Kjøre Testene

```bash
# Kjør alle tester
pytest

# Kjør med verbose output (viser hver testcase)
pytest -v

# Kjør kun tester i en spesifikk fil
pytest test_oppgave1.py

# Kjør kun tester som matcher et navn
pytest -k "epost"
```

