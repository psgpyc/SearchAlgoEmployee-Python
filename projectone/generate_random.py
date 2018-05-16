import random
import string
from geopy.geocoders import Nominatim


VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))

NUM = "".join(set(string.digits)-set('98'))
global cou
cou = 0


def generate_name_email(length=int(random.choice('3456789'))):
    first = ""
    last = ""

    for i in range(length):
        if i % 2 == 0:
            first += random.choice(CONSONANTS)
            last += random.choice('CONSONANTS')
        else:
            first += random.choice(VOWELS)
            last += random.choice(VOWELS)

    en = random.choice(string.digits)

    name = "{} {}".format(first, last)
    email = first + "." + last + en + "@email.com"

    return name.title() , email.lower()


# def generate_email():
#     fname, lname = generate_name().lower().split(" ")
#     en = random.choice(string.digits)
#     email = fname + "." + lname + en + "@email.com"
#
#     return email
#

def generate_phone(length=10):
    phone = '98'
    for i in range(8):
        phone += random.choice(NUM)

    return phone


def generate_address():
    dummy_address = ["Birtamode", "Baneshowr", "lagankhel", "satdobato", "kalanki", "gongabu", "harisiddi",
                     "kumaripati", "Godawari", "new road", "kings way", "jadibutti", "panauti", "pokhara",
                     "biratnagar", "syabrubeshi","Mahakali","Nepalgunj","Santinagar"]

    return random.choice(dummy_address)


# def generate_bio():
#     bio = "my name is {}, and i live in {}.you can reach me on {}.".format(generate_name(), generate_address(),
#                                                                            generate_email())
#
#     return bio


def generate_gender():
    gen = random.choice('MF')
    return gen


def generate_dob():
    day = random.randint(1, 32)
    month = random.randint(1, 13)
    year = random.randint(2035, 2060)
    dob = str(year) + "-" + str(month) + "-" + str(day)

    return dob

def generate_longtude():
    geolocator = Nominatim()
    location = geolocator.geocode(generate_address())
        #print((location.latitude, location.longitude))

    latitude = location.latitude
    longtiude = location.longitude

    lon_lat = (latitude,longtiude)

    return latitude , longtiude
    print(generate_address())



def generate_socialmedia():
    name,email = generate_name_email()
    fname,lname = name.split(" ")
    media = "www.facebook.com/{}".format(fname+lname).lower()

    return media







def main():
    pass



if __name__ == "__main__":
    main()

