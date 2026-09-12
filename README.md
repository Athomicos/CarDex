# CarDex

A web app for cataloguing real cars you've spotted in person — on the street, at meetups, or car shows. Register an account and build your own personal collection, one sighting at a time.

## How it works

1. **Sign up and log in.** Basic username/password authentication, with hashed passwords and server-side sessions.
2. **Add a sighting.** Pick the car's brand, model, and specific version through a cascading selector (brand → model → version), backed by a catalog of 100+ real cars spanning hot hatches, JDM icons, modern performance cars, and everyday classics. Versions you already own are automatically excluded from the list — but a higher-performance version of a model you already have (e.g. a base Golf vs. a Golf GTI) still counts as a separate, addable entry.
3. **Specs, auto-filled.** Selecting a version instantly pulls its horsepower, engine, top speed, and production years from the catalog — no manual entry needed.
4. **Attach a photo (optional but recommended).** One photo per sighting; it's automatically resized and orientation-corrected before being stored.
5. **Log where and when.** A free-text location field, with the sighting timestamped automatically.
6. **Browse your collection.** Every sighting appears as a clickable card with its photo. Click through for the full spec sheet plus your photo, location, and date.
7. **Search and filter.** Narrow your collection down by brand, model, or version.

## Tech stack

- **Backend:** Flask + SQLite (via CS50's SQL library)
- **Auth:** Werkzeug password hashing, filesystem-backed sessions
- **Images:** Pillow (resizing, EXIF orientation correction)
- **Frontend:** Bootstrap 5, vanilla JS (fetch-based cascading selects)

## Catalog

The catalog was built and curated by hand rather than scraped — an initial scraping attempt was blocked by the source site, so the car data (brand, model, version, years, horsepower, engine, top speed) was entered and verified manually instead.

<!--
Optional section — only keep this if the PWA (manifest.json + service worker) actually ships.
Delete it otherwise; claiming installability you didn't build undermines the rest of the README.

## Installable as an app
CarDex can be installed to your phone's home screen and opens full-screen, like a native app.
-->