from TheDateClass import Date


def main():

    calendar = Date(10, 10, 2017)

    while True:

        x = input("[1]Set Day\t"
                  "[5]Show Day\n"
                  "[2]Set Month"
                  "[6]Show Month\n"
                  "[3]Set Year\t"
                  "[7]Show Year\n"
                  "[4]Set Date\t"
                  "[8]Show Date\n")

        if x == "1":
            day = int(input("Set Day: "))
            if day in range(1,32):
                calendar.setDay(day)

        elif x == "2":
            month = int(input("Set Month: "))
            if month in range(1,13):
                calendar.setMonth(month)

        elif x == "3":
            year = int(input("Set Year: "))
            if year in range(1900,9999):
                calendar.setYear(year)

        elif x == "4":
            day = (int(input("Set Day: ")))
            month = (int(input("Set Month: ")))
            year = (int(input("Set Year: ")))
            calendar.setDate(day, month, year)

        elif x == "5":
            print("Day:", calendar.getDay())

        elif x == "6":
            print("Month:", calendar.getMonth())

        elif x == "7":
            print("Year:", calendar.getYear())

        elif x == "8":
            calendar.toString()

        else:
            break


main()