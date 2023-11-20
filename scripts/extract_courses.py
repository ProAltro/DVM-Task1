import csv, json, pdfplumber

table = []

# # Export PDF to Excel using Adobe Acrobat and then Save As CSV
# with open("media/timetable.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         table.append(row)


# Directly use the timetable pdf which contains all pages of courses
pdf = pdfplumber.open("media/timetable.pdf")
for i in pdf.pages:
    table.extend(i.extract_table())


def process_table(table):
    courses = []
    current_section = None
    current_instructors = None

    for row in table:
        if (
            row[0] == None
            or row[0].find("SEMESTER") != -1
            or row[0].startswith("COM")
            or row[3] == "L"
        ):
            continue

        if row[0].isnumeric():
            l = ["L", "P", "U"]
            credits = {
                l[j]: int(i) if i.isnumeric() else 0 for j, i in enumerate(row[3:6])
            }
            courses.append(
                {
                    "com cod": int(row[0]),
                    "id": row[1],
                    "title": row[2],
                    "credits": credits,
                    "sections": {"T": [], "P": [], "L": []},
                }
            )
            current_section = courses[-1]["sections"]

        if row[6]:
            courses[-1]["sections"][row[6][0]].append(
                {
                    "id": row[6],
                    "room": row[8] if not row[8].isnumeric() else int(row[8]),
                    "times": row[9],
                    "midsem": row[10],
                    "compre": row[11],
                    "instructors": [],
                }
            )
            current_instructors = current_section[row[6][0]][-1]["instructors"]

        if row[7]:
            current_instructors.append(row[7].title())

    return courses


if __name__ == "__main__":
    json.dump(process_table(table), open("media/timetable.json", "w"), indent=4)
