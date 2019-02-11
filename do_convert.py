from datetime import datetime
import pprint

def convert_to_ampm(twenty_four_hour_time: str) -> str:
	return datetime.strptime(twenty_four_hour_time, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
	ignore = data.readline()
	flights = {}
	for line in data:
		k, v = line.strip().split(',')
		flights[k] = v

pprint.pprint(flights)
print()

fts = {convert_to_ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(fts)
print()

when = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when)
print()