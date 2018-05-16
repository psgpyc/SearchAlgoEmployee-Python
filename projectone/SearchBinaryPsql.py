import psycopg2

global c , conn

try:
    conn = psycopg2.connect("host='127.0.0.1' dbname='usersdb' user='postgres' password='nepal123'")

except:
    raise Exception("error in credentials")
finally:
    c = conn.cursor()

def rundown(m):
    print(".........working............")

    c.execute("select phone from userdetails")
    x = list(c.fetchall())

    y = [int(i[0]) for i in x]

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

    quicksort(y, 0, len(y) - 1)

    def binarySearch(arr, low, high, x):

        if high >= low:

            mid = low + (high - low) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return binarySearch(arr, low, mid - 1, x)

            else:
                return binarySearch(arr, mid + 1, high, x)

        else:
            return -1

    # m= int(input("Enter the phone number for searching:"))

    result = binarySearch(y,0,len(y) - 1,m)


    if result != -1:
        print("\nCongratulations Your Search is Mapped as per the Element {}.".format(m))
        print("\n\nThe Details of the User are:")
        (c.execute("select * from userdetails where {0} = '{1}'".format("phone",m)))
        nn = c.fetchall()
        for i in nn[0]:
            print(i)



    else:
        print("Element is not present in array")


if __name__ == '__main__':
    rundown(1223)