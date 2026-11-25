# VaniDesk owner dashboard

One web page where the business owner sees the phone calls VaniDesk answered: what happened on each call, the appointments that came out of it, and the transcript.

The page is built the way the dashboard build guide (`vanidesk-dashboard-ui-guide.md`) teaches it: plain HTML with Tailwind classes, served by FastAPI through a Jinja2 template, with data from a SQLite database.

The calls you see are **sample data** for a made-up dental clinic. The live phone side (Twilio and Sarvam) is not part of this project yet.

## Run it on your laptop (Mac or Linux)

You need Python 3.11 or newer and an internet connection. Check your Python version first:

```bash
python3 --version
```

If it prints `Python 3.11` or a higher number, continue. If not, install a newer Python from [python.org/downloads](https://www.python.org/downloads/).

Open a terminal, go into this folder, and run these commands one at a time:

```bash
# 1. Go into the project folder (change the path to where the folder is on your laptop)
cd path/to/Vanidesk

# 2. Create a virtual environment: a private place for this project's packages
python3 -m venv .venv

# 3. Switch it on. Your prompt now starts with (.venv)
source .venv/bin/activate

# 4. Install the packages the app needs
pip install -r requirements.txt

# 5. Create your settings file from the example
cp .env.example .env

# 6. Put the sample calls into the database
python seed.py

# 7. Start the app
uvicorn app.main:app --reload
```

Step 6 prints `Added 12 calls and 13 appointments.` Step 7 prints a few lines ending with `Application startup complete.` and then waits. That is correct: the app is running.

Now open **http://localhost:8000/dashboard** in your browser.

To stop the app, click on the terminal and press `Ctrl+C`.

### The next time

You only need three of the steps:

```bash
cd path/to/Vanidesk
source .venv/bin/activate
uvicorn app.main:app --reload
```

## What you can do on the page

| Where | What it does |
| --- | --- |
| Sidebar: **Calls** | One call in full: checklist, appointments table, badge, chips, follow-up buttons. Under them, the ten newest calls. Click one to open it. |
| Sidebar: **Appointments** | Every appointment from every call, soonest first. **Open the call** jumps to the call it came from. |
| Sidebar: **Transcripts** | The full transcript of the selected call, in the caller's language, and a list to pick another call. |
| Sidebar: **Settings** | The business details. Read-only for now. |
| Button: **Read the full transcript** | Opens the Transcripts view for the selected call. |
| Buttons: **Call back**, **Resend the SMS** | Greyed out on purpose. They need the phone line, which is not connected yet. |

Two more addresses:

- http://localhost:8000/health answers `{"status":"ok"}`. It is a quick way to check the app is running.
- http://localhost:8000/docs is the page FastAPI builds by itself, listing every route.

## What is in this folder

```text
Vanidesk/
├── app/
│   ├── main.py          The routes: /health and /dashboard
│   ├── config.py        Reads settings from the .env file
│   ├── sample_data.py   The business details and the 12 sample calls
│   └── db/
│       ├── database.py  The connection to the SQLite database
│       └── models.py    The two tables: CallLog and Appointment
├── dashboard/
│   └── index.html       The whole page: HTML, Tailwind classes, a little JavaScript
├── seed.py              Puts the sample calls into the database
├── requirements.txt     The packages to install, with exact versions
├── .env.example         Example settings. Copy it to .env
└── .gitignore           Files Git should ignore
```

Running the app creates three more things, and Git ignores all of them: `.venv/` (the virtual environment), `.env` (your settings) and `vanidesk.db` (the database).

## Change the business or the sample calls

Everything made up is in one file: `app/sample_data.py`.

- `BUSINESS` at the top holds the name, phone, address, hours, services, languages and greeting. The sidebar and the Settings page read it. Change it, save, and refresh the page.
- `SAMPLE_CALLS` holds the 12 calls. These are copied into the database by `seed.py`, so after you change them, rebuild the database:

```bash
rm vanidesk.db
python seed.py
```

Running `python seed.py` on a database that already has calls changes nothing, so you cannot wipe your data by accident.

## Reading the code next to the guide

`dashboard/index.html` has a comment such as `<!-- Stage 3: the sidebar -->` at the start of each part, so you can find each stage of the guide in the finished page.

| Guide stage | Where to look |
| --- | --- |
| 0. Empty page | The skeleton of `dashboard/index.html`: `<head>`, `<title>`, `<body>` |
| 1. Tailwind and the background | The `<script>` line in `<head>` and the classes on `<body>` |
| 2. Card and two columns | The first `<div>`, the `<aside>` and the `<main>` |
| 3. Sidebar | Everything inside `<aside>` |
| 4. Header, checklist, footer | Inside `<section id="view-calls">`: the `<header>`, the `<ul>`, the `<footer>` |
| 5. Appointments table | The `<table>` inside `view-calls` |
| 6. Badge, chips, buttons | Right under that table |
| 7. Sidebar switches views | The four `<section class="view ...">` blocks, and the `<script>` at the bottom of the file |
| 8. FastAPI serves the page | `templates = ...` and the `dashboard` route in `app/main.py` |
| 9. Data comes from Python | `context={...}` in `app/main.py`, and every `{{ ... }}` and `{% ... %}` in `index.html` |
| 10. Real rows from SQLite | `app/db/models.py`, `seed.py`, and the `select(...)` queries in `app/main.py` |
| 11. Recent calls, picking one | `call_id` in `app/main.py`, and the `Recent calls` list in `index.html` |

### Where the code differs from the guide

The guide builds the smallest page that works. A few things here go one step further, so that nothing on the page is a dead end:

- **Follow-up buttons.** In the guide they do nothing. Here `Read the full transcript` opens the Transcripts view, and the other two are disabled (`disabled` attribute, grey colours) with a line that says why.
- **The view is kept in the address.** Clicking a sidebar button adds `#appointments` (or another view name) to the address. Refreshing the page keeps that view open, and the browser's Back button works. This is the last part of the `<script>`.
- **One extra column: `sms_sent`.** `CallLog` has a true/false column that says whether a text went out. The green badge and the small grey note under the table read it, instead of always saying "SMS sent".
- **The summary line is worked out in Python.** `make_summary_line` in `app/main.py` counts the appointments by status. A call with no appointments shows no table.
- **More sample data, in its own file.** The guide suggests two or three calls typed into `seed.py`. Here there are 12, kept in `app/sample_data.py`, and `seed.py` copies them into the database.
- **Settings shows the business details**, not "Coming in Milestone 6". The sidebar also shows the business name under "VaniDesk".
- **Small extras.** The Appointments table has an `Open the call` link, the Transcripts view has a list to pick another call, and `http://localhost:8000/` forwards to `/dashboard`.

## What is not built yet

- Answering real phone calls (Twilio and Sarvam). Every call on the page comes from `app/sample_data.py`.
- `Call back` and `Resend the SMS`.
- Changing the business details on the Settings page.
- A login. Anyone who can open the address can see the page, so run it only on your own laptop for now.

## If something goes wrong

- **`python3 -m venv .venv` fails on Ubuntu or Debian** with a message about `ensurepip`: run `sudo apt install python3-venv`, then try again.
- **`uvicorn: command not found`:** the virtual environment is not switched on. Run `source .venv/bin/activate`.
- **`TemplateNotFound: index.html`** or **`No module named 'app'`:** you started `uvicorn` from the wrong folder. Start it from the folder that contains both `app` and `dashboard`.
- **The page shows plain black text with no colours:** Tailwind is downloaded from the internet each time the page loads. Check your connection and refresh.
- **The page says `No calls yet`:** run `python seed.py` (step 6).
- **`Address already in use`:** something else is using port 8000. Start the app on another port with `uvicorn app.main:app --reload --port 8001` and open `http://localhost:8001/dashboard`.
- **The terminal shows `GET /favicon.ico ... 404 Not Found`:** this is harmless. The browser asked for a small tab icon and the page does not have one.
- **Anything else:** the real error message is in the terminal where `uvicorn` is running. Read the last line of it first.
