import json
from fhir.model import Patient, HumanName, Identifier, CodeableConcept, Coding, uri, Address
from fhir.resources.organization import Organization

with open('data.json', 'r') as dt:
    data = json.load(dt)


p = Patient(id=data['pid']['patient_identifier_list']['id_number']['st'])
name = HumanName()
p.address = [Address(line = [data['pid']['patient_address']['street_address']['street_or_mailing_address']]), Address(city = data['pid']['patient_address']['city']['st'], postalCode = data['pid']['patient_address']['zip_or_postal_code']['st'], state = data['pid']['patient_address']['state_or_province']['st']  )]

name.suffix = [data['pid']['patient_name']['suffix_e_g_jr_or_iii']['st']]

name.use = 'official'
name.given = [data['pid']['patient_name']['given_name']['st']]
name.family = data['pid']['patient_name']['family_name']['surname']
p.birthDate = data['pid']['date_time_of_birth']['time']['dtm']
p.gender = data['pid']['administrative_sex']['is']['is']
p.name = [name]
y = p.dumps('json')
print(p.dumps('json'))
with open('data2.json', 'w') as tf:
	x = json.dump(y, tf, indent = 2)
