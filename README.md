# Mystery Library

Mystery Library è una web app realizzata con Django che permette agli utenti di esplorare, acquistare e votare libri, gestire il proprio profilo e molto altro. L'applicazione include funzionalità di autenticazione, gestione profilo, shop, votazione libri e storico acquisti.

## Funzionalità principali

- **Registrazione e login/logout utenti**
- **Gestione profilo personale** (visualizzazione e modifica dati)
- **Profilo utente con storico acquisti**
- **Catalogo libri** con dettagli e possibilità di acquisto
- **Votazione libri**
- **Logout sicuro**

---
## Dipendenze principali

- Python 3.8+
- Django 5.x

## Installazione

### 1. Clona il repository

```bash
git clone <URL_DEL_REPO>
cd <cartella_del_progetto>
```

### 2. Crea e attiva un ambiente virtuale

**WINDOWS:**
```bash
python -m venv .venv
```
cmd
```bash
>>> venv\Scripts\activate
```
git bash
```bash
$ source .venv/Scripts/activate
```
**LINUX/MAC:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installa le dipendenze

```bash
pip install django
```

Installa il file `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Applica le migrazioni al database

```bash
cd django
python manage.py migrate
```

### 5. Crea un superuser (opzionale, per accedere all'admin)

```bash
python manage.py createsuperuser
```

### 6. Avvia il server di sviluppo

```bash
python manage.py runserver
```

---

## Utilizzo

- Accedi all'applicazione su [http://localhost:8000/](http://localhost:8000/)
- Registrati o effettua il login per accedere alle funzionalità riservate
- Naviga tra shop, profilo, vota i libri e gestisci il tuo account

---

## Struttura delle principali URL

- `/libreria/login/` — Login utente
- `/libreria/logout/` — Logout utente
- `/libreria/signup/` — Registrazione nuovo utente
- `/libreria/profilo/` — Profilo personale
- `/libreria/shop/` — Catalogo libri
- `/libreria/acquista/<id>` — Acquisto libro
- `/libreria/home/` — Home page

---

## Note importanti

- Assicurati che la cartella `static` e la cartella `media` esistano nella root del progetto per la gestione di file statici e media.
- Puoi accedere all'admin Django su `/admin/` con le credenziali del superuser.

---




