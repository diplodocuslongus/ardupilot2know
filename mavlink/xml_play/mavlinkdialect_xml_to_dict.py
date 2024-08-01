import xmltodict
import pprint
import json

with open('common.xml') as fd:
    mavdialect = xmltodict.parse(fd.read(), process_namespaces=True)

#print(mavdialect)
#print(mavdialect['mavlink']['enums'])
#print('\n\n')
print(mavdialect['mavlink']['enums']['enum'])
#print(mavdialect['enum']['entry'])
print('\n\n')
print('\n\n')
#for section in mavdialect['mavlink']['enums']['enum']['entry']:
for section in mavdialect['mavlink']['enums']['enum']:
    section_name = section.get('@name')
    #entry_section = section.get('@entry')
    if section_name == 'MAV_AUTOPILOT':
        print(section_name)
for section in mavdialect['mavlink']['enums']['enum']:
    section_name = section.get('@name')
    #entry_section = section.get('@entry')
    if section_name == 'MAV_TYPE':
        print(section_name)
        for ssection in section['entry']:
            try:
                ssection_name = ssection.get('@name')
            #entry_section = section.get('@entry')
                print(f'here: {ssection_name}')
            except:
                print("couldn't read")
poet
for section in mavdialect['mavlink']['enums']['enum']:
    for ssection in section['entry']:
        try:
            ssection_name = ssection.get('@name')
        #entry_section = section.get('@entry')
            print(f'here: {ssection_name}')
        except:
            print("couldn't read")
#print(my_dict['enum']['entry']['name'])
#print(my_dict['enum']['id'])
#print(my_dict['audience']['id']['@what'])

