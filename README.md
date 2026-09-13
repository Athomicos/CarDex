# CarDex
#### Video Demo: <URL HERE ONCE UPLOADED TO YOUTUBE>
 
#### Description:
 
CarDex is a web app for cataloguing real cars you've spotted in person — on the street, at meetups, or car shows. You register an account and build your own personal collection, one sighting at a time.
 
## How it works
 
1. **Sign up and log in.** Basic username/password authentication, with hashed passwords (via Werkzeug) and server-side, filesystem-backed sessions.
2. **Add a sighting.** Pick the car's brand, model, and specific version through a cascading selector (brand → model → version), backed by a catalog of 100+ real cars spanning hot hatches, JDM icons, modern performance cars, and everyday classics. Versions you already own are automatically excluded from the list — but a higher-performance version of a model you already have (e.g. a base Golf vs. a Golf GTI) still counts as a separate, addable entry.
3. **Specs, auto-filled.** Selecting a version instantly pulls its horsepower, engine, top speed, and production years from the catalog — no manual entry needed.
4. **Attach a photo** (optional but recommended). One photo per sighting; it's automatically resized and orientation-corrected before being stored.
5. **Log where and when.** A free-text location field, with the sighting timestamped automatically.
6. **Browse your collection.** Every sighting appears as a clickable card with its photo. Click through for the full spec sheet plus your photo, location, and date.
7. **Search and filter.** Narrow your collection down by brand, model, or version.
## Tech stack
 
- **Backend:** Flask + SQLite (via CS50's SQL library)
- **Auth:** Werkzeug password hashing, filesystem-backed sessions
- **Images:** Pillow (resizing, EXIF orientation correction)
- **Frontend:** Bootstrap 5, vanilla JS (fetch-based cascading selects)
## File structure
 
- **app.py** — All application routes: authentication (register/login/logout), the `add_car` route (GET renders the form, POST saves a sighting), the AJAX endpoints `/models/<brand>` and `/versions/<brand>/<model>` that populate the cascading selects, `/collection` to list a user's sightings, and `/car/<id>` for a single car's detail page.
- **helpers.py** — Shared helper functions, including `apology()` and the queries used to fetch a user's collection.
- **schema.sql** — Defines the database tables: the car catalog (brand, model, version, production years, horsepower, engine, top speed), the users table, and the sightings table, which enforces a `UNIQUE(user_id, car_id)` constraint so the same version can't be added twice.
- **catalog_seed.sql** — The hand-curated catalog data used to populate the database on setup.
- **scripts/scrape_catalog.py** — An early attempt to populate the catalog automatically; kept in the repo as a record of that approach, even though it was ultimately abandoned (see Catalog section below).
- **templates/** — Jinja templates: `layout.html` (shared base), `login.html` / `register.html`, `add_car.html` (the sighting form), `collection.html` (the collection grid), and `car_detail.html` (a single sighting's full detail).
- **static/** — `css/style.css` for custom styles on top of Bootstrap, `js/script.js` for the cascading-select logic and form validation, and `uploads/` where sighting photos are stored.
## Catalog
 
The catalog was built and curated by hand rather than scraped — an initial scraping attempt was blocked by the source site, so the car data (brand, model, version, years, horsepower, engine, top speed) was entered and verified manually instead.
 
## Design decisions
 
A few choices here weren't obvious upfront, and I picked between real alternatives:
 
**Cascading selects instead of a multi-step form.** Brand, model, and version are three `<select>` elements on a single page, populated dynamically via `fetch()`, rather than a multi-page wizard. A wizard would need to persist intermediate state across requests, which added complexity that a single-insert form didn't need.
 
**Free-text location instead of geolocation.** I considered browser geolocation with reverse geocoding, or pulling coordinates from the uploaded photo's EXIF data, but ruled out both: EXIF location data isn't always present or accurate, and both options were scope creep relative to the app's actual goal. A free-text field does the job with far less risk of silently failing.
 
**One photo per sighting, not several.** The catalog design could have supported multiple photos per sighting via a separate join table, but a single photo column on the sightings row was simpler and matched how the feature is actually used — nobody needs a gallery for a single car spotted once.
 
**Exclusion by version, not by model.** When adding a sighting, already-owned *versions* are hidden from the dropdown, but other versions of a model you already own still show up. This was a deliberate choice: a base Golf and a Golf GTI are meaningfully different cars worth logging separately, even though they share a model name.
 
**Duplicates enforced at the database layer.** Rather than checking for an existing sighting before inserting a new one, the app inserts directly and relies on the `UNIQUE(user_id, car_id)` constraint to reject duplicates via an `IntegrityError`. This avoids a race condition that a check-then-insert approach would be exposed to.
 
## Testing
 
The app was tested manually end-to-end on a real mobile device (registration, login, photo upload, browsing the collection), and with `curl` to simulate manual, non-browser requests — checking duplicate-sighting attempts, expired sessions, and inconsistent brand/model/version combinations submitted directly to the form's POST route.
 
## Known limitations
 
The catalog, while broad, was built by hand and isn't as exhaustive as a full market database. The location field is free text and isn't validated or geocoded against any external source.
