from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v


pprint.pprint(flights)
print()

flights2={}
for key,value in flights.items():
    flights2[convert2ampm(key)] = value.title()

pprint.pprint(flights2)
#
# more_flights = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
# pprint.pprint(more_flights)

print(flights2.values())
dests = set(flights2.values())
print(dests)


west = []
for k,v in flights2.items():
    if v == 'West End':
        west.append(k)
print(west)

west2 = [k for k, v in flights2.items() if v == 'West End']
print(west2)

# flights5 = {}
# for location in dests:
#     flights5[location] = [k for k, v in flights2.items() if v == location]
# print(flights5)

flights6 = {location: [k for k, v in flights2.items() if v == location] for location in dests}
pprint.pprint(flights6)