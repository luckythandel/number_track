import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import sys

print("Enter your phonenumber with country code: ")

number = sys.argv[1]
if len(number) < 1:
        print ("No Number")
        exit()

else:
        x = phonenumbers.parse(number)

        print (x)
        print ("Carrier: " +carrier.name_for_number(x, 'en'))
        print ("Location: " +geocoder.description_for_number(x, 'en'))
