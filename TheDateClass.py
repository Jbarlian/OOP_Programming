class Date:

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def getDay(self):
        return int(self.__day)

    def getMonth(self):
        return int(self.__month)

    def getYear(self):
        return int(self.__year)

    def setDay(self, value):
        self.__day = value

    def setMonth(self, value):
        self.__month = value

    def setYear(self, value):
        self.__year = value

    def setDate(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def toString(self):
        if self.__day < 10:
            y = "0" + str(self.__day)
        else:
            y = str(self.__day)
        if self.__month < 10:
            x = "0" + str(self.__month)
        else:
            x = str(self.__month)

        print(y + "/" + x + "/" + str(self.__year))