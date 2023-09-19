from datetime import datetime

currentTime = datetime.now();

seconds = currentTime.timestamp()

separated = "{:,.4f}".format(seconds)
notation = "{:.2e}".format(seconds)

print(f"Seconds since January 1, 1970: {separated} or {notation} in scientific notation")

month = currentTime.strftime("%B")
date = currentTime.strftime("%d")
year = currentTime.strftime("%Y")
print(month, date, year, sep=" ");