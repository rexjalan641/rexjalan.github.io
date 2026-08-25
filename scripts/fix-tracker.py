import csv

with open("portfolio-site/tracker-data.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

today = "2026-08-25"
out = []
log = []

for row in rows:
    if not row:
        continue
    rid = row[1] if len(row) > 1 else ""
    if rid == "E2":
        row[6] = "https://www.ferner-alsdorf.de/deutschland-bekommt-ein-ki-gesetz-buendelung-der-nationalen-ki-aufsicht-bei-der-bundesnetzagentur"
        row[7] = today
        log.append("E2: source replaced (dead TUV URL -> ferner-alsdorf.de)")
    elif rid == "P3":
        log.append("P3: removed (duplicate of L3)")
        continue
    elif rid in ("L8", "L5", "L6", "L7", "E1", "E3", "E4", "E5", "P4", "I1"):
        row[7] = today
        log.append(rid + ": last_checked refreshed")
    if rid == "I2":
        row[2] += "; EU ratified 15 May 2026 (per Treaty Office data)"
        log.append("I2: enriched with EU ratification note")
    if rid == "L8":
        row[4] = "In preparation (deadline now 2027-08-02)"
        log.append("L8: status wording softened per verifier")
    out.append(row)

with open("portfolio-site/tracker-data.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(out)

print("\n".join(log))
print("rows:", len(out) - 1)
