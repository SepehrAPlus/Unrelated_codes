import csv;

target_header = "URI Scheme";

with open("uri-schemes-1.csv", "r") as f1:
	reader = csv.reader(f1)
	for row in reader:
		print(F"'{row[0]}',")
