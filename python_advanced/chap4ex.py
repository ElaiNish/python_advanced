def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return ' '.join(words[word] for word in sentence.split())


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):#לימדו אותנו חוק בחטיבה שאם מספר לא מתחלק עד השורש שלו הוא מספר ראשוני
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    primes = (num for num in range(n + 1, 100*n) if is_prime(num))
    return next(primes)


def parse_ranges(ranges_string):
    ranges = (r.split('-') for r in ranges_string.split(','))


    numbers = (num for start, stop in ranges for num in range(int(start), int(stop) + 1))

    return numbers


def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def gen_secs():
    sec = 0
    while True:
        yield sec
        sec = (sec + 1) % 60

def gen_minutes():
    min = 0
    while True:
        yield min
        min = (min + 1) % 60

def gen_hours():
    hour = 0
    while True:
        yield hour
        hour = (hour + 1) % 24

def gen_days(month, leap_year=True):
    days_in_month = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 1
    while True:
        yield day
        day = day + 1 if day < days_in_month[month-1] else 1

def gen_months():
    month = 1
    while True:
        yield month
        month = (month + 1) % 13
        if month == 0: month = 1

def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1

def gen_time():
    gseconds = gen_secs()
    gminutes = gen_minutes()
    ghours = gen_hours()

    while True:
        sec = next(gseconds)
        if sec == 0:
            min = next(gminutes)
            if min == 0:
                hour = next(ghours)
            else:
                hour = hour
        else:
            min = min
            hour = hour
        yield (hour, min, sec)

def gen_date():
    gtime = gen_time()
    gdays = gen_days(1)
    gmonths = gen_months()
    gyears = gen_years()

    year = next(gyears)
    month = next(gmonths)
    day = next(gdays)
    hour, min, sec = next(gtime)

    while True:
        yield "{:02d}/{:02d}/{:04d} {:02d}:{:02d}:{:02d}".format(day, month, year, hour, min, sec)
        hour, min, sec = next(gtime)
        if sec == 0 and min == 0 and hour == 0:
            day = next(gdays)
            if day == 1:
                month = next(gmonths)
                if month == 1:
                    year = next(gyears)
        gdays = gen_days(month, year%4==0 and (year%100!=0 or year%400==0))





def main():
    # print(translate("el gato esta en la casa"))

    # print(first_prime_over(1000000))

    # print(list(parse_ranges("1-2,4-4,8-10")))
    # print(list(parse_ranges("0-0,4-8,20-21,43-45")))

    # fibo_gen = get_fibo()
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))
    # print(next(fibo_gen))

    date_gen=gen_date()
    for i in range(1, 10000000):
        date = next(date_gen)
        if i % 1000000 == 0:
            print(date)  



    return 0


if __name__ == '__main__':
    main()


