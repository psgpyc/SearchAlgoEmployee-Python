import sys

import psycopg2


import UserDetailsdb
import SearchBinaryPsql
import CsvInsertion
import PsqlSortQuick



try:
    conn = psycopg2.connect("host='127.0.0.1' dbname='usersdb' user='postgres' password='nepal123'")

except:
    raise Exception("error in credentials")
finally:
    c = conn.cursor()

if sys.argv[1] == "-i":
    UserDetailsdb.Usersclass.insert_records()


    UserDetailsdb.choice(1)


if sys.argv[1] == "-r" and sys.argv[2] == "-p" and sys.argv[4] == "-v" :

    UserDetailsdb.Usersclass.see_records(sys.argv[3],sys.argv[5])

if sys.argv[1] == "-d":

    UserDetailsdb.Usersclass.delete_records(sys.argv[2])


if sys.argv[1] == '-u' and sys.argv[2] == "-p" and sys.argv[4] == '-on' and sys.argv[6] == "-nn":
    UserDetailsdb.Usersclass.update_record(sys.argv[3],sys.argv[5],sys.argv[6])



if sys.argv[1] == "-t":
    UserDetailsdb.Usersclass.table_init(sys.argv[2])


if sys.argv[1] == "-search":
    print("Sorting.......")
    print("Searching............")
    SearchBinaryPsql.rundown(int(sys.argv[2]))

if sys.argv[1] == "-csv":
    CsvInsertion.insert_csv(sys.argv[2])

if sys.argv[1] == "-sort" and sys.argv[2] == "-p":
    PsqlSortQuick.see_records(sys.argv[3])



if sys.argv[1] == '--help':

    init_table = "-t <table name>"
    insert         = "-i"
    search         = "-r -p <Search Parameter> -v <value to be searched>"
    delete         = "-d <value(id)>"
    update         = "-u -p <Update Parameter> -on <old value> -nn <new value>"
    searching      = "-search <value for search(phone number)>"
    Sorting        = "-sort -p <parameter> <value>"
    insertion_csv  = "-csv <filename>"

    print("Welcome to help Section:")
    print("HERE ARE THE SYNTAX FOR RESPECTIVE OPERATIONS:")
    print("\n Table Creation : {} \n Insertion : {} \n Searching : {} \n Deletion : {} \n Update : {} \n Searching : {} \n Sorting : {} \n Csv Insertion: {}".format(init_table,insert,search,delete,update,searching,Sorting,insertion_csv))










