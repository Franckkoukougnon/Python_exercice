import phonenumbers

from phone_number import number

from phonenumbers import geocoder

from phonenumbers import carrier

ch_num = phonenumbers.parse(number, "CH")

service_nmber = phonenumbers.parse(number,"RO")
print(geocoder.description_for_number(ch_num, "fr"))
print("votre numero "+ number +" est un numero de "+ geocoder.description_for_number(ch_num, "fr"))
print("votre numero est de l'opérateur "+ carrier.name_for_number(service_nmber, "fr"))
#print(carrier.name_for_number(service_nmber, "en"))