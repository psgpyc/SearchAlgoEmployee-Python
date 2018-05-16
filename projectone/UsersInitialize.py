'''
This is a class containing core code for implementing CRUD.

'''



import psycopg2

global c , conn

try:
    conn = psycopg2.connect("host='127.0.0.1' dbname='usersdb' user='postgres' password='nepal123'")

except:
    raise Exception("error in credentials")
finally:
    c = conn.cursor()






class UserInit:

    @staticmethod
    def initialize(col, value):
        c.execute("select * from userdetails where {} = '{}'".format(col, value))
        allrecords = c.fetchall()
        # print(allrecords)
        if len(allrecords) == 0:
            print("SORRY NO RECORD FOUND")
        # else:
        #     for i in allrecords:
        #         print(
        #             "NAME: {1}  \nEmail:{2}    \nPhone:{3}  \nBio:{4}   \nDOB:{5}    \nGender:{6}  \nAddress:{7}    \nLongitude:{8}   \nLatitude:{9} \nSocialMEdia:www.facebook.com/{10}".format(
        #                 i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        return allrecords

    @staticmethod
    def initialize_del(id):
        c.execute("select * from userdetails where id = '{0}'".format(id))
        allrecords = c.fetchall()
        if len(allrecords) == 0:
            print("SORRY !! NO RECORD FOUND")
        else:

            try:
                c.execute("delete from userdetails where id = '{0}'".format(id))

                print("successfully deleted !!")
                conn.commit()

            except:
                print("error")
                conn.rollback()

    @staticmethod
    def initialize_update(col, old, new):
        c.execute("select * from userdetails where {} = '{}'".format(col, old))
        allrecords = c.fetchall()
        if len(allrecords) == 0:
            print("SORRY NO RECORD FOUND")
        else:

            query = "update userdetails set {0}='{1}' where {0} = '{2}'".format(col,
                                                                                new,
                                                                                old)

            try:
                c.execute(query)
                print("sucessfully Updated !!!!")

            except:
                raise Exception("Error")
                # conn.rollback()

            conn.commit()







