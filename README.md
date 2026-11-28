# Hello

Hello is an AI phone receptionist for US small businesses. This project has two parts:

- **The public website:** Home, How it works, Pricing, About, Contact / Book a demo, Log in and Sign up.
- **The owner dashboard:** one page where the business owner sees the phone calls that were answered: what happened on each call, the appointments that came out of it, and the transcript.

Both are plain HTML with Tailwind classes, served by FastAPI through Jinja2 templates, with data in a SQLite database. The dashboard is built the way the dashboard build guide teaches it.

Three things to know before you start:

- The calls in the dashboard are **sample data** for a made-up dental clinic. The live phone side (Twilio and Sarvam) is not part of this project yet, and the website says so on every page.
- The Log in and Sign up pages are **screens only**. Their buttons are switched off, and the dashboard opens without a login.
- Some text on the website is **placeholder text** that you must replace, such as the prices. See [Placeholder text you must replace](#placeholder-text-you-must-replace).

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

Now open **http://localhost:8000** in your browser. That is the home page of the website. The dashboard is at **http://localhost:8000/dashboard**.

To stop the app, click on the terminal and press `Ctrl+C`.

### The next time

You only need three of the steps:

```bash
cd path/to/Vanidesk
source .venv/bin/activate
uvicorn app.main:app --reload
```

### After you download newer code

New code can need a new package. The website, for example, needs `python-multipart` to read the contact form. So after each `git pull`, install the packages again before you start the app. It only installs what is missing:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## The pages of the website

Every page is one HTML file in the `website/` folder, and one short function (a "route") in `app/main.py` that shows it.

| Address | HTML file | Route in `app/main.py` | What is on it |
| --- | --- | --- | --- |
| `/` | `website/home.html` | `home` | What the product is, an example call, and the Book a demo button |
| `/how-it-works` | `website/how-it-works.html` | `how_it_works` | The five steps of a call, each marked Built or Planned, and the features |
| `/pricing` | `website/pricing.html` | `pricing` | Three placeholder plans. Prices are not decided |
| `/about` | `website/about.html` | `about` | Why the product exists and how far along it is |
| `/contact` | `website/contact.html` | `contact` shows the form, `contact_submit` saves it | The Book a demo form |
| `/login` | `website/login.html` | `login` | The login screen (look only) |
| `/signup` | `website/signup.html` | `signup` | The sign-up screen (look only) |
| `/dashboard` | `dashboard/index.html` | `dashboard` | The owner dashboard |

**The shared layout is `website/base.html`.** It holds the parts that are the same on every page: the header with the navigation, the menu button for phones, and the footer. Each page file starts with `{% extends "base.html" %}` and fills in two blocks: `title` (the text on the browser tab) and `content` (everything between the header and the footer). To add a link to the navigation, add one line to `nav_links` near the top of `base.html`.

The dashboard does not use `base.html`. It keeps its own layout with the sidebar, the way the guide builds it.

### The Book a demo form

When a visitor sends the form on `/contact`, the app checks it (a name and an email address that looks right) and saves it as one row in the `demo_requests` table of the database. No email is sent, and no page shows the requests yet. To read them, run this in the project folder:

```bash
sqlite3 -header -column receptionist.db "SELECT * FROM demo_requests;"
```

`sqlite3` comes with macOS. On Ubuntu or Debian, install it with `sudo apt install sqlite3`.

## Rename the product

The name is written in exactly one place in the code: `app_name` in `app/config.py`.

```python
app_name: str = "Hello"
```

Changing the name is that one setting. Change the line, save, and every page, every browser tab title, the header, the footer and the dashboard show the new name. In the HTML files the name is always written as `{{ app_name }}`, never typed out.

Two things are not renamed by that line:

- This README. Change the name here by hand (it is in the heading and the first sentence).
- The folder and the GitHub repository. They are still called `Vanidesk`, the first working name, which is why the run steps say `cd path/to/Vanidesk`. Nothing on a page shows that name.

The database file is called `receptionist.db` and the speaker in the sample transcripts is called `Receptionist`, so neither has to change when the product name does.

## Placeholder text you must replace

The website was written before the prices, the final wording and the product name were decided. Everything that was made up for now is marked with the word `PLACEHOLDER` in a comment next to it. To list every one of them:

```bash
grep -rn "PLACEHOLDER" website/
```

| Where | What is placeholder | What to do |
| --- | --- | --- |
| `website/pricing.html` | The three plans: the names `Plan A`, `Plan B`, `Plan C`, the price `$—`, and every line in each plan. The page shows an orange "Prices are not decided yet" notice and a `Placeholder` label on each plan. | Decide the real plans, change the `plans` list, then delete the notice and the labels. |
| `website/about.html` | The three paragraphs (Why it exists, What we are building, Where we are) are draft wording. | Rewrite them in your own words. There is no "who is behind it" part. Add one if you want. |
| `website/contact.html` | Two promises: "We will get in touch" and "We use your details only to reply to this request". | Keep them only if they are true. |
| `app/config.py` | The name `Hello`. It was picked "for now" and may change again. | See [Rename the product](#rename-the-product). |

The rest of the wording (the home page, the How it works page) is a first draft too, so read all of it. One rule for anything you write: keep it true. The site has no customer names, reviews, logos or numbers, because there are none yet. And when a part of the product gets built, update the two lists under "Where the product is today" in `website/home.html` and the labels in `website/how-it-works.html`.

## What you can do on the dashboard

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
│   ├── main.py          The routes: one for each website page, /health and /dashboard
│   ├── config.py        The settings: the product name, and what is read from the .env file
│   ├── sample_data.py   The business details and the 12 sample calls
│   └── db/
│       ├── database.py  The connection to the SQLite database
│       └── models.py    The three tables: CallLog, Appointment and DemoRequest
├── website/
│   ├── base.html        The shared layout: header, navigation, footer
│   ├── home.html        /
│   ├── how-it-works.html  /how-it-works
│   ├── pricing.html     /pricing
│   ├── about.html       /about
│   ├── contact.html     /contact (the Book a demo form)
│   ├── login.html       /login (look only)
│   └── signup.html      /signup (look only)
├── dashboard/
│   └── index.html       The whole dashboard: HTML, Tailwind classes, a little JavaScript
├── seed.py              Puts the sample calls into the database
├── requirements.txt     The packages to install, with exact versions
├── .env.example         Example settings. Copy it to .env
└── .gitignore           Files Git should ignore
```

Running the app creates three more things, and Git ignores all of them: `.venv/` (the virtual environment), `.env` (your settings) and `receptionist.db` (the database).

## Change the business or the sample calls

Everything made up is in one file: `app/sample_data.py`.

- `BUSINESS` at the top holds the name, phone, address, hours, services, languages and greeting. The sidebar and the Settings page read it. Change it, save, and refresh the page.
- `SAMPLE_CALLS` holds the 12 calls. These are copied into the database by `seed.py`, so after you change them, rebuild the database:

```bash
rm receptionist.db
python seed.py
```

Deleting `receptionist.db` also deletes the demo requests that were sent with the contact form, because they are in the same file.

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
- **Settings shows the business details**, not "Coming in Milestone 6". The sidebar also shows the business name under the product name.
- **Small extras.** The Appointments table has an `Open the call` link, the Transcripts view has a list to pick another call, and a link above the card goes back to the website.
- **The name is not typed into the page.** The guide types the product name into the `<title>` and the sidebar. Here both say `{{ app_name }}`, which `app/main.py` fills in from `app/config.py`. In the sample transcripts the speaker is called `Receptionist`, not the product name, for the same reason.

## What is not built yet

- Answering real phone calls (Twilio and Sarvam). Every call on the page comes from `app/sample_data.py`.
- `Call back` and `Resend the SMS`.
- Changing the business details on the Settings page.
- A login. The Log in and Sign up pages are screens only. Anyone who can open the address can see the dashboard, so run it only on your own laptop for now.
- A page that lists the demo requests, and an email when one arrives. They are only saved in the database.
- Protection against junk messages on the contact form. Add it before the website goes on the internet.
- A phone layout for the dashboard. The website pages fit a phone screen. The dashboard is made for a laptop screen.

## If something goes wrong

- **`python3 -m venv .venv` fails on Ubuntu or Debian** with a message about `ensurepip`: run `sudo apt install python3-venv`, then try again.
- **`uvicorn: command not found`:** the virtual environment is not switched on. Run `source .venv/bin/activate`.
- **`TemplateNotFound`** or **`No module named 'app'`:** you started `uvicorn` from the wrong folder. Start it from the folder that contains `app`, `website` and `dashboard`.
- **`Form data requires "python-multipart" to be installed`:** your virtual environment was made before the website was added. Run `pip install -r requirements.txt`, then start the app again.
- **The dashboard still shows an older product name in front of the transcript lines, or says `No calls yet` after you downloaded newer code:** your `.env` and your database were made by an older version, when the database file had another name. Run `cp .env.example .env`, then `python seed.py`. That makes a fresh database called `receptionist.db`. The older `.db` file in the folder is not used any more and can be deleted.
- **The page shows plain black text with no colours:** Tailwind is downloaded from the internet each time the page loads. Check your connection and refresh.
- **The page says `No calls yet`:** run `python seed.py` (step 6).
- **`Address already in use`:** something else is using port 8000. Start the app on another port with `uvicorn app.main:app --reload --port 8001` and open `http://localhost:8001/dashboard`.
- **The terminal shows `GET /favicon.ico ... 404 Not Found`:** this is harmless. It happens on addresses that have no tab icon of their own, such as `/health` and `/docs`.
- **Anything else:** the real error message is in the terminal where `uvicorn` is running. Read the last line of it first.
