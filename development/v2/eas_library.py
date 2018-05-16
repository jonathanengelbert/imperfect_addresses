import csv
import re


with open('eas.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('eas_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        address_library = {rows[0].lower():rows[1].lower() for rows in reader}

value = "383 crestmont"


match = re.findall(r"\save\b|blvd\b|cir\b|dr\b|expy\b|hwy\b|hill\b|ln\b|park"
                   r"\b|pl\b|plz\b|pier\b|\brd\b|stps\b|\sst\b|sq\b|ter\b"
                   r"|tunl\b|way\b", value)


print(len(address_library.keys()))

for address, address_type in address_library.items():
        if not match:
            if value in address:
                value = value + " " + address_type


print(value)


# for address, address_type in address_library.items():
#     print(address + " " + address_type)

