import requests
import math

class my_airports():

	def __init__(self, lat, lat_range, lon, lon_range):
		self.lon = lon
		self.lat = lat
		self.lon_range = lon_range
		self.lat_range = lat_range
		self.stack = []
		self.distances = []

	def define_range(self):

		self.minlon = self.lon - lon_range
		self.maxlon = self.lon + lon_range

		self.minlat = self.lat - lat_range
		self.maxlat = self.lat + lat_range

	def get_data(self):
		self.url = 'https://mikerhodes.cloudant.com/airportdb/_design/view1/_search/geo?q=lon:['+str(self.minlon)+'%20TO%20'+str(self.maxlon)+']%20AND%20lat:['+str(self.minlat)+'%20TO%20'+str(self.maxlat)+']'
		self.r = requests.get(self.url)
		self.a = self.r.json()

	def calculate_distance(self):
		for t in self.a['rows']:
			dist = math.sqrt(((t['fields']['lat']-self.lat)*(t['fields']['lat']-self.lat))+((t['fields']['lon']-self.lon)*(t['fields']['lon']-self.lon)))
			city = str(t['fields']['name'])
			distance = dist
			x = {}
			x[distance] = city
			self.distances.append(distance)
			self.stack.append(x)

	def print_results(self):

		print(" ")
		print("There are "+str(self.a['total_rows'])+" airports in the given range")
		if self.a['total_rows'] > 25:
			print("Here are the first 25 of them")
		print("")
		#print(self.url)
		#print(self.stack)
		z = sorted(self.distances)
		#print(z)
		
		q = 1
		for i in z:
			for j in self.stack:
				if i in j:
					print(str(q)+". "+j[i])
					del j[i]
					#self.stack.pop(0)
					#print(self.stack)
					q += 1

		print("")


while True:
    try:
        latitude = float(raw_input("Enter latitude co-ordinate >> "))
    except ValueError:
        print("\tInput has to be a Floating number\n")
		
    else:
        break

while True:
    try:
        lat_range = float(raw_input("Enter latitude range (+/-) >> "))
    except ValueError:
        print("\tInput has to be a Floating number\n")
		
    else:
        break

while True:
    try:
        longitude = float(raw_input("Entere longitude co-ordinate >> "))
    except ValueError:
        print("\tInput has to be a Floating number\n")
		
    else:
        break

while True:
    try:
        lon_range = float(raw_input("Enter longitude range (+/-) >> "))
    except ValueError:
        print("\tInput has to be a Float\n")
		
    else:
        break


me = my_airports(latitude,lat_range,longitude,lon_range)

me.define_range()
me.get_data()
me.calculate_distance()
me.print_results()




