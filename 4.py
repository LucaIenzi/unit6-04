# made by luca ienzi
# made on dec 1
# made for ics3u
# ender your favert day and it will tell you if it is a day and what day of the week it is
from emumm import Enum

provence = Enum('ON','QC','AB','BC','MB','NB','NL','NT','NS','NU','NS','PE','SK','YT')

street = Enum('BLVD','CRES','DR','LANE','CRT')

class MailAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type , city_name, province_initials, postal_code,):
        
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province_initials = province_initials
        self.postal_code = postal_code
        self.province_initials = province_initials
        self.street_name = street_name

first_name = raw_input('enter your first name')
last_name = raw_input('enter your last name')
house_number = raw_input('enter your house number')
street_name = raw_input('enter your street name')
street_type_user= raw_input('enter your street type')
if street_type_user in street:
    street_type = street_type_user
else:
    print('you are an bilige idiot')
city_name = raw_input('enter your city name')
province_user = raw_input('enter your province initals')
if province_user in provence:
    province_inials = province_user
else:
    print('stop being the vivage idiot')
postal_code = raw_input('enter your postal code')

a_mailing_address = MailAddress(first_name,last_name,house_number,street_name,street_type,city_name,province_inials,postal_code)

print("\n" + a_mailing_address.first_name + " " + a_mailing_address.last_name + "\n" + a_mailing_address.house_number + " " + a_mailing_address.street_name + " " + a_mailing_address.street_type + "\n" + a_mailing_address.city_name + ", " + a_mailing_address.province_initials + " " + a_mailing_address.postal_code + "\n",)
