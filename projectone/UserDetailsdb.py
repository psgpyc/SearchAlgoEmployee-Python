import psycopg2
import sys
import generate_random
from UsersInitialize import UserInit as UI

HOSTNAME= '127.0.0.1'
USER = 'postgres'
PASS = 'nepal123'
DB = 'usersdb'
TABLE = 'userdetails'

try:
    conn = psycopg2.connect("host='127.0.0.1' dbname='usersdb' user='postgres' password='nepal123'")

except:
    raise Exception("error in credentials")
finally:
    c = conn.cursor()



class Usersclass(object):
       #method to initialize table in the database
    @staticmethod
    def table_init(details):

        try:
            c.execute(""" CREATE TABLE {0}(
                                           id serial primary key,
                                           name VARCHAR(100) NOT NULL,
                                           email VARCHAR(50) ,
                                           phone VARCHAR(15) ,
                                           bio  text not null,
                                           dob DATE NOT NULL DEFAULT CURRENT_DATE ,
                                           gender VARCHAR(30) NOT NULL,
                                           address VARCHAR(100),
                                           long numeric,
                                           lat numeric,
                                           SocialMedia text
                                           )""".format(details))

            conn.commit()
            print("table is created")

        except psycopg2.DatabaseError as e:
            print(f"DB ERROR !!!!:{e}")
            conn.rollback()

    #method to inser records in the database
    @staticmethod
    def insert_records(*self):
        try:
            c.execute(
                "INSERT INTO userdetails(name,email,phone,bio,dob,gender,address,long,lat,SocialMedia) VALUES('{0}','{1}', '{2}', '{3}' , '{4}', '{5}', '{6}', '{7}' ,'{8}', '{9}')".format(
                    self[0], self[1], self[2], self[3], self[4], self[5], self[6], self[7], self[8],
                    self[9]))
            conn.commit()
            print("successfully inserted via random generator(generator_random.py)!!")
        except Exception as error:
            print(error)
            conn.rollback()

    @staticmethod
    def see_records(col = None , val = None):

        if col == None and val == None:

           choices, user_dict = repeat()

           val = str(input("enter the search parameter of the user:"))
           print("--------------------------------------------------------------------------------------")

           if choices in user_dict.keys():

               UI.initialize(user_dict[choices], val)

        else:
            UI.initialize(col,val)




    @staticmethod

    def delete_records(id = None):

        if id == None:
            idd = int((input("input id to be deleted: ")))
            UI.initialize_del(idd)


        else:
            UI.initialize_del(id)


    @staticmethod

    def update_record(col = None , old = None , new = None):

        if col == None and old == None and new == None:
           choices, user_dict = repeat()
           old_name = input("Enter the {} to be replaced".format(user_dict[choices]))
           new_name = input("Enter the {} to be replaced with".format(user_dict[choices]))

           if choices in user_dict.keys():
               UI.initialize_update(user_dict[choices],old_name, new_name)


        else:
            UI.initialize_update(col , old ,new)

def validator(name, email, phone, bio, dob, gender, address, long, lat, img, media):
    if type(name) == str and len(name) != 0 and type(email) == str and len(email) > 0 and type(phone) == int and len(
            phone) == 10 and type(gender) == str and len(gender) == 1:
        return True


def repeat():
    print("CHOICES: "
          "\n1:name"
          " 2:email"
          " 3:phone"
          " 4:Bio"
          " 5:DOB"
          " 6:Gender"
          " 7:Address"
          " 8:Longitude"
          " 9:Latitude"
          " 11:Social Media")

    user_dict = {
        1: "name",
        2: "email",
        3: "phone",
        4: "bio",
        5: "dob",
        6: "gender",
        7: "address",
        8: "long",
        9: "lat",
        10: "SocialMedia"
    }

    choice = int(input("enter between 1 - 11 for searching with respective parameter"))
    return choice, user_dict


def choice(ch):
    if ch == 1:
        name, email = generate_random.generate_name_email()
        phone = generate_random.generate_phone()
        dob = generate_random.generate_dob()
        gender = generate_random.generate_gender()
        address = generate_random.generate_address()
        long, lat = generate_random.generate_longtude()
        img = 'https://www.redblobgames.com/img/red-blob-128.png'
        media = generate_random.generate_socialmedia()

        bio = "My name is {} and i live in {}. You can reach me at {} or through my social link account {}" \
              "".format(name, address, email, media)
        Usersclass.insert_records("paritosh sharma ghimire","paritosh.ghimire666@gmail.com",9802051714,"hey, how are you?","1994-10-31","M","satdobato","27.343454","85.78787877878","jhsdfgsdd","jdghjgdhjgdjd")
        # Usersclass.insert_records(name,email,phone,bio,dob,gender,address,long,lat,media)

    if ch == 2:
        Usersclass.see_records()

    if ch == 3:
        Usersclass.delete_records()

    if ch == 4:
        Usersclass.update_record()

    if ch == 5 :
        Usersclass.table_init("helloworld")

    print("Do you wish to continue:y/n")
    if input().lower() == 'y':
        ch = int(input("enter the choices for respective operations:"))

        choice(ch)

    else:
        print("have a good day heaha !!")


def main():
    print("CHOICES:"
          "\n1:INSERT DATA"
          "\n2:VIEW RECORD "
          "\n3:DELETE RECORD"
          "\n4:UPDATE RECORD"
          "\n5:CREATE TABLE"
          )
    ch = int(input("enter the choices for respective operations:"))

    choice(ch)


if __name__ == '__main__':
    main()


