import requests
import re
import json
import oldDB as db

#check capacity of classes

department_dict = {
	"ALST": "Africana and Latin American Studies",
	"ANTH": "Anthropology",
	"ARTS": "Art and Art History",
	"AHUM": "Arts and Humanities",
	"ASIA": "Asian Studies",
	"ASTR": "Astronomy",
	"BIOL": "Biology",
	"CHEM": "Chemistry",
	"CHIN": "Chinese",
	"CLAS": "The Classics",
	"COSC": "Computer Science",
	"ECON": "Economics",
	"EDUC": "Educational Studies",
	"ENGL": "English",
	"ENST": "Environmental Studies",
	"FMST": "Film and Media Studies",
	"FREN": "French",
	"GEOG": "Geography",
	"GEOL": "Geology",
	"GERM": "German",
	"GREK": "Greek",
	"HEBR": "Hebrew",
	"HIST": "History",
	"ITAL": "Italian",
	"JAPN": "Japanese",
	"JWST": "Jewish Studies",
	"LATN": "Latin",
	"LGBT": "Lesbian, Gay, Bisexual, Transgender, and Queer Studies",
	"CORE": "CORE studies",
	"LING": "Linguistics",
	"MATH": "Mathematics",
	"ARAB": "Middle Eastern and Islamic Studies (Language)",
	"MIST": "Middle Eastern and Islamic Studies",
	"MUSE": "Museum Studies",
	"MUSI": "Music",
	"NAST": "Native American Studies",
	"NASC": "Natural Science",
	"NEUR": "Neuroscience",
	"PCON": "Peace and Conflict Studies",
	"PHIL": "Philosophy",
	"PHYS": "Physics",
	"POSC": "Political Science",
	"PSYC": "Psychology",
	"RELG": "Religion",
	"REST": "Russian and Eurasian Studies",
	"SOSC": "Social Sciences",
	"SOCI": "Sociology",
	"SPAN": "Spanish",
	"THEA": "Theater",
	"UNST": "University Studies",
	"WMST": "Women’s Studies",
	"WRIT": "Writing and Rhetoric",
	"FSEM": "First year seminar",
	"HUMN": "Test",
	"LCTL": "Less Commonly Taught Languages"
}

semester_links = open("colgate_links.csv", "r").read()
semester_links = semester_links.split(";")

#printing classes for each semester through Fall 2015 to Spring 2021

for link in range(len(semester_links)):
	page = requests.get(semester_links[link])
	result_dict = json.loads(page.text)
	counting_dict = {}

	for x in department_dict:
		counting_dict[x]=0

	for x in result_dict:
		counting_dict[x["DISPLAY_KEY"][:4]]+=1

	counting_dict["Year"]=int(result_dict[0]["TERM_CODE"][:4])
	counting_dict["Semester"]=int(result_dict[0]["TERM_CODE"][-1])

	print("Year: %s, %s semester" % (result_dict[0]["TERM_CODE"][:4], result_dict[0]["TERM_CODE"][-1]))
	print(sorted(counting_dict.items(), key=lambda x: x[1], reverse=True))
	print()






