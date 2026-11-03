# allotment-pins

Pinterest pin images for **The Allotment Planner** by StarValley Gardens (Etsy shop: starvalleygroup.etsy.com).
Images only. The paid PDF products are never stored here.

## Layout
- `pins/` – published pin images (1000 × 1500 JPEG, 2:3)
- `assets/sheets/` – web-resolution page previews used inside pins
- `assets/profile.jpg` – Pinterest profile photo
- `tools/make_pins.py` + `tools/shoot.js` – pin generator
- `posted.md` – log of every pin posted (check before making new ones, never repeat a headline)

## Making pins
```
python3 tools/make_pins.py spec.json WORKDIR      # spec: [[slug, "TITLE\nLINE 2", "Subtitle", ["SheetName", ...]], ...]
node tools/shoot.js WORKDIR pins/
```
Sheet names: Cover, Main (plot plan), CropRotation, SowingCalendar, MonthlyJobs, PlotVisit, Succession,
SeedInventory, PestLog, FruitPerennials, HarvestLog, PlotCosts, Notes, SeedPackets.
One sheet = single large page; two or three = fanned stack (front sheet last).
Headlines: two short uppercase lines, max ~16 characters per line. Subtitle: one line, under ~55 characters.

## Style
Cream #F3EEE2 background, Marcellus serif, dark text #2F2B26, sage #C3C9A5 bottom band with
"PRINTABLE PDF · A4 & US LETTER · INSTANT DOWNLOAD". British English throughout (sow, courgettes, sweetcorn, matt, colour).

## Etsy listings (pin links)
| Product | Price | Link |
|---|---|---|
| UK Sowing Calendar (1 page) | £2.50 | https://www.etsy.com/listing/4607810809 |
| Plot Starter Pack (plot plan, crop rotation, sowing calendar, seed inventory, harvest log) | £4.50 | https://www.etsy.com/listing/4607832692 |
| Complete Allotment Planner (13 pages) | £8.95 | https://www.etsy.com/listing/4607832986 |
| Allotment Year Bundle (Complete + seed packets/tags + Garden Planner) | £13.50 | https://www.etsy.com/listing/4607812005 |

## Pinterest boards (account StarValleyGardens)
- Allotment Planner Printables
- UK Sowing Calendar & Veg Growing
- Gifts for Gardeners & Allotment Holders
