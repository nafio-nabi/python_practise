company = {"Name": "Netflix", "Stock Name": "NFLX", "Stock Price": 410.17}
print(type(company))
print(company)

print()

for item, value in company.items():
    print(f"{item}: {value}")

print()

print(company["Name"])
print(company["Stock Name"])
print(company["Stock Price"])