import requests
import re
import json
import os

#capacity for classes
#Neil Albert

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
	"LCTL": "Less Commonly Taught Languages",
	"RUSS": "Russian",
	"SOAN": "Sociology and Anthropology",
	"ROLA": "Romance Languages and Literatures",
	"MARS": "Medieval and Renaissance Studies"
}

#returns all classes/students or does that for some specific year
def access_data(classes=False, students=False, year=None):
	directory = "Database/"
	complete_dict={}
	if year==None:
		for filename in sorted(os.listdir(directory)):
			test_reading = json.loads(open("Database/"+filename, "r").read())
			
			counting_dict = {}
			for x in department_dict:
				counting_dict[x]=0

			if classes:
				for x in test_reading['data']:
					counting_dict[x["subject"]]+=1
			elif students:
				for x in test_reading['data']:
					counting_dict[x["subject"]]+=int(x['enrollment'])

			complete_dict[test_reading['data'][0]['term']]=counting_dict.items()
			#print(test_reading['data'][0]['termDesc']+"\n")
			#print(sorted(counting_dict.items(), key=lambda x: x[1], reverse=True))
	else:
		test_reading = json.loads(open("Database/"+year+".json", "r").read())
		counting_dict = {}
		for x in department_dict:
			counting_dict[x]=0

		if classes:
			for x in test_reading['data']:
				counting_dict[x["subject"]]+=1
		elif students:
			for x in test_reading['data']:
				counting_dict[x["subject"]]+=int(x['enrollment'])
		
		return complete_dict

	return complete_dict


