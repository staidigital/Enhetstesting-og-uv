## Steg 1: Installere uv 

Åpne Terminal:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Verifiser installasjonen:**
```bash
uv --version
```
Du skal se noe som: `uv 0.x.x`

## Steg 2: Opprette prosjektmappe (5 min)

### Opprett en mappe for TDD-prosjektet
```bash
# Naviger til der du vil ha prosjektet (f.eks. Dokumenter)
cd ~/Dokumenter  # macOS/Linux
cd C:\Users\DittNavn\Dokumenter  # Windows

# Opprett prosjektmappe
mkdir tdd-pytest-prosjekt
cd tdd-pytest-prosjekt
```

### Sjekk at du er i riktig mappe
```bash
pwd  # macOS/Linux
cd   # Windows
```

---

## Steg 3: Opprette virtuelt miljø med uv (5 min)

### Opprett miljøet
```bash
uv venv
```

Dette oppretter en `.venv`-mappe i prosjektet ditt med et isolert Python-miljø.

### Aktiver det virtuelle miljøet

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

### Hvordan vet du at det fungerer?
Når miljøet er aktivert, skal du se `(.venv)` foran kommandolinjen din:
```
(.venv) bruker@maskin:~/tdd-pytest-prosjekt$
```

---

## Steg 4: Installere pytest med uv (5 min)

Nå som vi har et virtuelt miljø, kan vi installere pytest:

```bash
uv pip install pytest pytest-cov
```

**Hva installerte vi?**
- `pytest` → Testrammeverket vi skal bruke
- `pytest-cov` → Verktøy for å måle test coverage

### Verifiser installasjonen
```bash
pytest --version
```

Du skal se noe som: `pytest 8.x.x`

---

### Frivillig: lag enklere alias for venv
Synes du det er litt klønete å aktivere ditt virtuelle miljø? Vel, la oss lage noen aliaser som gjør dette enklere. Ved å kjøre koden under i terminalen setter vi _venv_ til å være kommando for å starte det virtuelle miljøet og _voff_ for å avslutte det; men du kan selvfølgelig kalle det hva enn du vil. Ups! Dette tar utgangspunktet i at du bruker __zsh__. 

```bash
echo "alias venv='source .venv/bin/activate'" >> ~/.zshrc && echo "alias voff='deactivate'" >> ~/.zshrc && tail -2 ~/.zshrc
```
Som bør gi deg følgende output:
```bash
alias venv='source .venv/bin/activate'
alias voff='deactivate'
```
For å aktivere de nye aliasene dine, må du kjører 
```bash
source ~/.zshrc
```
