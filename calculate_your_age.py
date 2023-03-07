def calcAge(year, month, date):
    import datetime

    today = datetime.datetime.now().date()
    dob = datetime.date(year, month, date)
    age = int((today-dob).days / 365.25)
    print(age)


if __name__ == "__main__":
    calcAge(1986, 9, 19)
