import urllib.parse

up = urllib.parse.urlparse
def is_string_a_possible_link(a:str)->bool:
	parsed = up(a)
	scheme,netloc = parsed[0:2]
	return (scheme!="")+(netloc!="") > 1
	