import psycopg2

conn = psycopg2.connect("host='127.0.0.1' dbname='usersdb' user='postgres' password='nepal123'")
cur = conn.cursor()




def see_records(parameter = "phone"):



    cur.execute("select {} from userdetails".format(parameter))
    new_l = cur.fetchall()

    arr = [list(i) for i in new_l]

    n = len(arr)
    print("sorting ........")

    def quicksort(a, start, end):
        if start < end:
            pindex = partition(a, start, end)
            quicksort(a, start, pindex - 1)
            quicksort(a, pindex + 1, end)

    def partition(a, start, end):
        pivot = a[end]
        pindex = start
        for i in range(start, end):
            if a[i] <= pivot:
                a[i], a[pindex] = a[pindex], a[i]
                pindex += 1

        a[pindex], a[end] = a[end], a[pindex]
        return pindex

    quicksort(arr, 0, n - 1)

    print("Sorted array is:")
    print(f"Total Length: {len(arr)}")
    print(list(arr))





if __name__ == '__main__':



    see_records("phone")


