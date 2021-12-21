from Menu import menu
from Menu2 import menu2
from Menu3 import menu3
import math

run = True
data = []
ni = []
centers = []
cumulative_numbers = []
start_interval = []
end_interval = []


def load_data():
    global data
    try:
        file = open('Data.txt', "r")
        for line in file:
            for elem in line.split():
                data.append(int(elem))
        file.close()
    except:
        print('Zły format danych')
    data.sort()
    if len(data) > 0:
        return True


# szereg rozdzielczy przedziałowy
# ilosc przedzialow
def number_of_intervals(db, make=False):
    num = math.sqrt(len(db))
    num = math.ceil(num)
    if make:
        print('k = pierwiastek(N) \nk = pierwiastek(%s) = %s' % (len(db), num))
    return num


# rozpietosc przedzialu
def length_of_intervals(db, make=False):
    h = (db[-1] - db[0]) // number_of_intervals(data)
    h += 1
    if make:
        print('h = N / k \nh = (%s - %s) / %s = %s' % (db[-1], db[0], number_of_intervals(data), h))
    return h


# przedzialy (ni), liczebnosci skumulowane, poczatek, koniec i srodek przedzialow
def intervals_func(db):
    global ni
    global centers
    global end_interval
    global start_interval
    global cumulative_numbers
    h = length_of_intervals(data)
    k = number_of_intervals(data)
    first = 1
    start = min(db)
    count = 0
    cum_numbers = 0
    while first < k + 1:
        for elem in db:
            if elem >= start:
                if elem < (start + h):
                    count += 1
        center = (start + (start + h)) / 2
        centers.append(center)
        ni.append(count)
        start_interval.append(start)
        end_interval.append(start + h)
        cum_numbers += count
        cumulative_numbers.append(cum_numbers)
        first += 1
        start += h
        count = 0


# ni * srodek
def sum5():
    global ni
    global centers
    data5 = []
    for i in range(len(ni)):
        new = ni[i] * centers[i]
        data5.append(new)
    return round(sum(data5), 3)


# srodek - srednia
def sum_n1():
    data_n1 = []
    for i in centers:
        new = i - arithmetic_mean(data, False, False)
        data_n1.append(new)
    return sum(data_n1)


# (srodek - srednia)^2 * ni
def sum_n2():
    data_n2 = []
    for i in range(len(centers)):
        new = centers[i] - arithmetic_mean(data, False, False)
        new **= 2
        new *= ni[i]
        data_n2.append(new)
    return sum(data_n2)


# (srodek - srednia)^3 * ni
def sum_n3():
    data_n3 = []
    for i in range(len(centers)):
        new = centers[i] - arithmetic_mean(data, False, False)
        new **= 3
        new *= ni[i]
        data_n3.append(new)
    return sum(data_n3)


# (srodek - srednia)^4 * ni
def sum_n4():
    data_n4 = []
    for i in range(len(centers)):
        new = centers[i] - arithmetic_mean(data, False, False)
        new **= 4
        new *= ni[i]
        data_n4.append(new)
    return sum(data_n4)


def arithmetic_mean(db, make=False, individual=True):
    if individual:
        suma = sum(db)
        mean = suma / len(db)
        mean = round(mean, 3)
        if make:
            print('xśr = E(xi) / N \nxśr = %s / %s = %s' % (suma, len(db), mean))
            print('\nInterpretacja:\n Średnia dla badanej zbiorowości wynosi %s' % mean)
    else:
        mean = sum5() / len(db)
        if make:
            print('xśr = E(ni * środek) / N \nxśr = %s / %s = %s' % (sum5(), len(db), mean))
            print('\nInterpretacja:\n Średnia dla badanej zbiorowości wynosi %s' % mean)
    return mean


# sumy
# (xi - xśr)^2
def sum2(db):
    data2 = []
    for i in db:
        new = i - arithmetic_mean(data)
        new = new ** 2
        data2.append(new)
    return sum(data2)


# (xi - xśr)^3
def sum3(db):
    data3 = []
    for i in db:
        new = i - arithmetic_mean(data)
        new = new ** 3
        data3.append(new)
    return sum(data3)


# (xi - xśr)^4
def sum4(db):
    data4 = []
    for i in db:
        new = i - arithmetic_mean(data)
        new = new ** 4
        data4.append(new)
    return sum(data4)


def variance(db, make=False, individual=True):
    if individual:
        mi2 = sum2(data) / len(db)
        mi2 = round(mi2, 3)
        if make:
            print('mi2 = E(xi - xśr)^2 / N\nmi2 = %s / %s = %s' % (sum2(data), len(db), mi2))
            print('\nInterpretacja:\n <BRAK INTERPRETACJI>')
    else:
        mi2 = sum_n2() / len(db)
        mi2 = round(mi2, 3)
        if make:
            print('mi2 = E(środek - xśr)^2 * ni / N\nmi2 = %s / %s = %s' % (sum_n2(), len(db), mi2))
            print('\nInterpretacja:\n <BRAK INTERPRETACJI>')
    return mi2


def standard_deviation(make=False, individual=True):
    if individual:
        s_dev = math.sqrt(variance(data))
        s_dev = round(s_dev, 3)
        if make:
            print('S(x) = pierwiastek(mi2)\nS(x) = pierwiastek(%s) = %s' % (variance(data), s_dev))
            print('\nInterpretacja:\n Średnio wartości różnia się od średniej o %s' % s_dev)
    else:
        s_dev = math.sqrt(variance(data, False, False))
        s_dev = round(s_dev, 3)
        if make:
            print('S(x) = pierwiastek(mi2)\nS(x) = pierwiastek(%s) = %s' % (variance(data, False, False), s_dev))
            print('\nInterpretacja:\n Średnio wartości różnia się od średniej o %s' % s_dev)
    return s_dev


def ratio_of_variation(make=False, individual=True):
    if individual:
        variation = (standard_deviation() / arithmetic_mean(data)) * 100
        variation = round(variation, 3)
        if make:
            print('V(x) = (S(x) / xśr) * 100 \nV(x) = (%s / %s) * 100 = %s ' % (standard_deviation(), arithmetic_mean(data), variation),
                  '%')
            print('\nInterpretacja:\n Odchylenie standardowe stanowi ', variation, '% średniej')
    else:
        variation = standard_deviation(False, False) / arithmetic_mean(data, False, False) * 100
        variation = round(variation, 3)
        if make:
            print('V(x) = S(x) / xśr \nV(x) = (%s / %s) * 100 = %s' % (standard_deviation(False, False), arithmetic_mean(data, False, False), variation), '%"')
            print('\nInterpretacja:\n Odchylenie standardowe stanowi ', variation, '% średniej')
    return variation


def third_central_moment(db, make=False, individual=True):
    if individual:
        mi3 = sum3(data) / len(db)
        mi3 = round(mi3, 3)
        if make:
            print('mi3 = E(xi - xśr)^3 / N \nmi3 = %s / %s = %s ' % (sum3(data), len(db), mi3))
    else:
        mi3 = sum_n3() / len(db)
        mi3 = round(mi3, 3)
        if make:
            print('mi3 = E(środek - xśr)^3 * ni / N \nmi3 = %s / %s = %s' % (sum_n3(), len(db), mi3))
    return mi3


def asymmetry_func(value):
    # prawostronny
    if (third_central_moment(data)) > 0:
        if abs(value) < 0.3:
            return 1
        elif abs(value) < 0.6:
            return 2
        elif abs(value) < 1:
            return 3
    # lewostronny
    elif (third_central_moment(data)) < 0:
        if abs(value) < 0.3:
            return 4
        elif abs(value) < 0.6:
            return 5
        elif abs(value) < 1:
            return 6
    else:
        return 7


def ratio_of_asymmetry(make=False, individual=True):
    if individual:
        asymmetry = (third_central_moment(data)) / (standard_deviation() ** 3)
        asymmetry = round(asymmetry, 3)
        if make:
            print('A = mi3 / S^3 \nA = %s / %s = %s' % (
            third_central_moment(data), round((standard_deviation() ** 3), 3), asymmetry))
            # prawostronny
            if asymmetry_func(asymmetry) == 1:
                print('\nInterpretacja:\n Słaba asymetria prawostronna')
            elif asymmetry_func(asymmetry) == 2:
                print('\nInterpretacja:\n Umiarkowana asymetria prawostronna')
            elif asymmetry_func(asymmetry) == 3:
                print('\nInterpretacja:\n Silna asymetria prawostronna')
            # lewostronny
            elif asymmetry_func(asymmetry) == 4:
                print('\nInterpretacja:\n Słaba asymetria lewostronna')
            elif asymmetry_func(asymmetry) == 5:
                print('\nInterpretacja:\n Umiarkowana asymetria lewostronna')
            elif asymmetry_func(asymmetry) == 6:
                print('\nInterpretacja:\n Silna asymetria lewostronna')
            # symetria
            elif asymmetry_func(asymmetry) == 7:
                print('\nInterpretacja:\n Rozkład symetryczny')
            else:
                print('Błąd w obliczeniach!')
    else:
        asymmetry = (third_central_moment(data, False, False) / (standard_deviation(False, False) ** 3))
        asymmetry = round(asymmetry, 3)
        if make:
            print('A = mi3 / S^3 \nA = %s / %s = %s' % (
            third_central_moment(data, False, False), (standard_deviation(False, False) ** 3), asymmetry))
            # prawostronny
            if asymmetry_func(asymmetry) == 1:
                print('\nInterpretacja:\n Słaba asymetria prawostronna')
            elif asymmetry_func(asymmetry) == 2:
                print('\nInterpretacja:\n Umiarkowana asymetria prawostronna')
            elif asymmetry_func(asymmetry) == 3:
                print('\nInterpretacja:\n Silna asymetria prawostronna')
            # lewostronny
            elif asymmetry_func(asymmetry) == 4:
                print('\nInterpretacja:\n Słaba asymetria lewostronna')
            elif asymmetry_func(asymmetry) == 5:
                print('\nInterpretacja:\n Umiarkowana asymetria lewostronna')
            elif asymmetry_func(asymmetry) == 6:
                print('\nInterpretacja:\n Silna asymetria lewostronna')
            # symetria
            elif asymmetry_func(asymmetry) == 7:
                print('\nInterpretacja:\n Rozkład symetryczny')
            else:
                print('Błąd w obliczeniach!')
    return asymmetry


def fourth_central_moment(db, make=False, individual=True):
    if individual:
        mi4 = sum4(data) / len(db)
        mi4 = round(mi4, 3)
        if make:
            print('mi4 = E(xi - xśr)^4 / N \nmi4 = %s / %s = %s' % (sum4(data), len(db), mi4))
    else:
        mi4 = sum_n4() / len(db)
        mi4 = round(mi4, 3)
        if make:
            print('mi4 = E(środek - xśr)^4 * ni / N \nmi4 = %s / %s = %s' % (sum_n4(), len(db), mi4))
    return mi4


def concentratrion(value):
    if value == 3:
        return 1
    elif value > 3:
        return 2
    else:
        return 3


def ratio_of_concentration(make=False, individual=True):
    if individual:
        concen = fourth_central_moment(data) / standard_deviation() ** 4
        concen = round(concen, 3)
        if make:
            print('k = mi4 / S^4 \nk = %s / %s = %s' % (fourth_central_moment(data), (standard_deviation() ** 4), concen))
            if concentratrion(concen) == 1:
                print('\nInterpretacja:\n Rozkład normalny')
            elif concentratrion(concen) == 2:
                print('\nInterpretacja:\n Rozkład wysmukły')
            else:
                print('\nInterpretacja:\n Rozkład spłaszczony')
    else:
        concen = fourth_central_moment(data, False, False) / (standard_deviation(False, False) ** 4)
        concen = round(concen, 3)
        if make:
            print('k = mi4 / S^4 \nk = %s / %s = %s' % (fourth_central_moment(data, False, False), (standard_deviation(False, False) ** 4), concen))
            if concentratrion(concen) == 1:
                print('\nInterpretacja:\n Rozkład normalny')
            elif concentratrion(concen) == 2:
                print('\nInterpretacja:\n Rozkład wysmukły')
            else:
                print('\nInterpretacja:\n Rozkład spłaszczony')
    return concen


def median(db, make=False, individual=True):
    if individual:
        # parzysty zbior
        if len(db) % 2 == 0:
            middle = len(db) // 2
            q2 = (db[middle - 1] + db[middle])
            q2 = q2 / 2
            if make:
                print('Me = 1/2 (x(N/2) + x(N/2 + 1) \nMe = (%s + %s) / 2 = %s' % (
                db[middle - 1], db[middle], q2))
                print('\nInterpretacja:\n 50% badanej zbiorowości osiaga ', q2,
                      ' i mniej, 50% badanej zbiorowości osiąga ', q2, ' i wiecej')
        # nieparzysty zbior
        else:
            middle = len(db) / 2
            middle = math.ceil(middle)
            q2 = db[middle - 1]
            if make:
                print('Me = x((N + 1) / 2) ', '\nMe = ', db[middle - 1])
                print('\nInterpretacja:\n 50% badanej zbiorowości osiaga ', q2,
                      ' i mniej, 50% badanej zbiorowości osiąga ', q2, ' i wiecej')
    else:
        middle = len(db) // 2
        for i in cumulative_numbers:
            if i > middle:
                index = cumulative_numbers.index(i)
                break
        q2 = start_interval[index] + (len(db) / 2 - cumulative_numbers[index - 1]) * (length_of_intervals(data) / ni[index])
        q2 = round(q2, 3)
        if make:
            print('Me = %s + (%s / 2 - %s) * %s = %s' % (
            start_interval[index], len(db), cumulative_numbers[index - 1], length_of_intervals(data) / ni[index], q2))
            print('\nInterpretacja:\n 50% badanej zbiorowości osiaga ', q2,
                      ' i mniej, 50% badanej zbiorowości osiąga ', q2, ' i wiecej')
    return q2


def quartile1(db, make=False, individual=True):
    if individual:
        # parzysty zbior
        if len(db) % 2 == 0:
            middle = len(db) // 4
            q1 = (db[middle - 1] + db[middle]) / 2
            if make:
                print('Q1 = 1/2 (x(N/4) + x(N/4 + 1) \nQ1 = (%s + %s) / 2 = %s' % (
                db[middle - 1], db[middle], q1))
                print('\nInterpretacja:\n 25% badanej zbiorowości osiaga ', q1,
                      ' i mniej, 75% badanej zbiorowości osiąga ', q1, ' i wiecej')
        # nieparzysty zbior
        else:
            middle = (len(db) / 4)
            middle = math.ceil(middle)
            q1 = db[middle - 1]
            if make:
                print('Q1 = x((N + 1) / 4) ', '\nQ1 = ', db[middle - 1])
                print('\nInterpretacja:\n 25% badanej zbiorowości osiaga ', q1,
                      ' i mniej, 75% badanej zbiorowości osiąga ', q1, ' i wiecej')
    else:
        middle = len(db) // 4
        for i in cumulative_numbers:
            if i > middle:
                index = cumulative_numbers.index(i)
                break
        q1 = start_interval[index] + (len(db) / 4 - cumulative_numbers[index - 1]) * (length_of_intervals(data) / ni[index])
        q1 = round(q1, 3)
        if make:
            print('Q1 = %s + (%s / 4 - %s) * %s = %s' % (
            start_interval[index], len(db), cumulative_numbers[index - 1], length_of_intervals(data) / ni[index], q1))
            print('\nInterpretacja:\n 25% badanej zbiorowości osiaga ', q1,
                      ' i mniej, 75% badanej zbiorowości osiąga ', q1, ' i wiecej')
    return q1


def quartile3(db, make=False, individual=True):
    if individual:
        # parzysty zbior
        if len(db) % 2 == 0:
            middle = len(db) * 0.75
            middle = int(middle)
            q3 = (db[middle - 1] + db[middle]) / 2
            if make:
                print('Q3 = 1/2 x(N * 3/4) + x(N * 3/4 + 1) \nQ3 = (%s + %s) / 2 = %s' % (
                db[middle - 1], db[middle], q3))
                print('\nInterpretacja:\n 75% badanej zbiorowości osiaga ', q3,
                      ' i mniej, 25% badanej zbiorowości osiąga ', q3, ' i wiecej')
        # nieparzysty zbior
        else:
            middle = (len(db) * 0.75)
            middle = math.ceil(middle)
            q3 = db[middle - 1]
            if make:
                print('Q3 = x((N + 1) * 3/4) ', '\nQ3 = ', db[middle - 1])
                print('\nInterpretacja:\n 75% badanej zbiorowości osiaga ', q3,
                      ' i mniej, 25% badanej zbiorowości osiąga ', q3, ' i wiecej')
    else:
        middle = len(db) * 0.75
        middle = int(middle)
        for i in cumulative_numbers:
            if i > middle:
                index = cumulative_numbers.index(i)
                break
        q3 = start_interval[index] + (middle - cumulative_numbers[index - 1]) * (length_of_intervals(data) / ni[index])
        q3 = round(q3, 3)
        if make:
            print('Q1 = %s + (%s / 4 - %s) * %s = %s' % (
            start_interval[index], len(db), cumulative_numbers[index - 1], length_of_intervals(data) / ni[index], q3))
            print('\nInterpretacja:\n 75% badanej zbiorowości osiaga ', q3,
                      ' i mniej, 25% badanej zbiorowości osiąga ', q3, ' i wiecej')
    return q3


def decile1(db, make=False, individual=True):
    if individual:
        # parzysty zbior
        if len(db) % 2 == 0:
            middle = len(db) // 10
            d1 = (db[middle - 1] + db[middle]) / 2
            if make:
                print('D1 = 1/2 x(N/10) + x(N/10 + 1) \nD1 = (%s + %s) / 2 = %s' % (
                db[middle - 1], db[middle], d1))
                print('\nInterpretacja:\n 10% badanej zbiorowości osiaga ', d1,
                      ' i mniej, 90% badanej zbiorowości osiąga ', d1, ' i wiecej')
        # nieparzysty zbior
        else:
            middle = (len(db) / 10)
            middle = math.ceil(middle)
            d1 = db[middle - 1]
            if make:
                print('D1 = x((N + 1) / 10) ', '\nD1 = ', db[middle - 1])
                print('\nInterpretacja:\n 10% badanej zbiorowości osiaga ', d1,
                      ' i mniej, 90% badanej zbiorowości osiąga ', d1, ' i wiecej')
    else:
        middle = len(db) // 10
        for i in cumulative_numbers:
            if i > middle:
                index = cumulative_numbers.index(i)
                break
        d1 = start_interval[index] + (middle - cumulative_numbers[index - 1]) * (length_of_intervals(data) / ni[index])
        d1 = round(d1, 3)
        if make:
            print('D1 = %s + (%s / 4 - %s) * %s = %s' % (
            start_interval[index], len(db), cumulative_numbers[index - 1], length_of_intervals(data) / ni[index], d1))
            print('\nInterpretacja:\n 10% badanej zbiorowości osiaga ', d1,
                      ' i mniej, 90% badanej zbiorowości osiąga ', d1, ' i wiecej')
    return d1


def decile9(db, make=False, individual=True):
    if individual:
        # parzysty zbior
        if len(db) % 2 == 0:
            middle = len(db) * 0.9
            middle = int(middle)
            d9 = (db[middle - 1] + db[middle]) / 2
            if make:
                print('D9 = 1/2 x(N * 9/10) + x(N * 9/10) + 1) \nD9 = (%s + %s) / 2 = %s' % (
                db[middle - 1], db[middle], d9))
                print('\nInterpretacja:\n 90% badanej zbiorowości osiaga ', d9,
                      ' i mniej, 10% badanej zbiorowości osiąga ', d9, ' i wiecej')
        # nieparzysty zbior
        else:
            middle = (len(db) * 0.9)
            middle = math.ceil(middle)
            d9 = db[middle - 1]
            if make:
                print('D9 = x((N + 1) * 9/10) ', '\nD9 = ', db[middle - 1])
                print('\nInterpretacja:\n 90% badanej zbiorowości osiaga ', d9,
                      ' i mniej, 10% badanej zbiorowości osiąga ', d9, ' i wiecej')
    else:
        middle = len(db) * 0.9
        middle = int(middle)
        for i in cumulative_numbers:
            if i > middle:
                index = cumulative_numbers.index(i)
                break
        d9 = start_interval[index] + (middle - cumulative_numbers[index - 1]) * (length_of_intervals(data) / ni[index])
        d9 = round(d9, 3)
        if make:
            print('D9 = %s + (%s / 4 - %s) * %s = %s' % (
            start_interval[index], len(db), cumulative_numbers[index - 1], length_of_intervals(data) / ni[index], d9))
            print('\nInterpretacja:\n 90% badanej zbiorowości osiaga ', d9,
                      ' i mniej, 10% badanej zbiorowości osiąga ', d9, ' i wiecej')
    return d9


def quartile_deviation(make=False, individual=True):
    if individual:
        q_dev = (quartile3(data) - quartile1(data)) / 2
        q_dev = round(q_dev, 3)
        if make:
            print('Q = (Q3 - Q1) / 2 \nQ = (%s - %s) / 2 = %s' % (quartile3(data), quartile1(data), q_dev))
    else:
        q_dev = (quartile3(data, False, False) - quartile1(data, False, False)) / 2
        q_dev = round(q_dev, 3)
        if make:
            print('Q = (Q3 - Q1) / 2 \nQ = (%s - %s) / 2 = %s' % (
            quartile3(data, False, False), quartile1(data, False, False), q_dev))
    return q_dev


def positional_ratio_of_variation(make=False, individual=True):
    if individual:
        ratio = (quartile_deviation() / median(data)) * 100
        ratio = round(ratio, 3)
        if make:
            print('Vq = (Q / Me) * 100 \nVq = (%s / %s) * 100 = %s' % (quartile_deviation(), median(data), ratio), '%')
            print('\nInterpretacja:\n Średnio wartości roznia się od mediany o ', quartile_deviation(),
                  ', co stanowi ', ratio, '% mediany w zawęzonym obszarze zmiennosci')
    else:
        ratio = (quartile_deviation(False, False) / median(data, False, False)) * 100
        ratio = round(ratio, 3)
        if make:
            print('Vq = (Q / Me) * 100%',
                  '\nVq = (%s / %s) * 100 = %s' % (quartile_deviation(False, False), median(data, False, False), ratio),
                  '%')
            print('\nInterpretacja:\n Średnio wartości roznia się od mediany o ', quartile_deviation(),
                  ', co stanowi ', ratio, '% mediany w zawęzonym obszarze zmiennosci')
    return ratio


def positional_ratio_of_asymmetry(make=False, individual=True):
    if individual:
        ratio = (quartile3(data) + quartile1(data) - 2 * median(data)) / (2 * quartile_deviation())
        ratio = round(ratio, 3)
        if make:
            print('As = (Q3 + Q1 - 2Me) / 2Q \nAs = (%s + %s - %s) / %s = %s' % (
            quartile3(data), quartile1(data), 2 * median(data), 2 * quartile_deviation(), ratio))
            if ratio > 0:
                print('\nInterpretacja:\nAsymetria prawostronna w zawęzonym obszarze zmiennosci')
            elif ratio < 0:
                print('\nInterpretacja:\nAsymetria lewostronna w zawęzonym obszarze zmiennosci')
            else:
                print('\nInterpretacja:\nRozkład symetryczny w zawęzonym obszarze zmiennosci')
    else:
        ratio = (quartile3(data, False, False) + quartile1(data, False, False) - (2 * median(data, False, False))) / (
                    2 * quartile_deviation(False, False))
        ratio = round(ratio, 3)
        if make:
            print('As = (Q3 + Q1 - 2Me) / 2Q \nAs = (%s + %s - %s) / %s = %s' % (
            quartile3(data, False, False), quartile1(data, False, False), 2 * median(data, False, False),
            2 * quartile_deviation(False, False), ratio))
            if ratio > 0:
                print('\nInterpretacja:\nAsymetria prawostronna w zawęzonym obszarze zmiennosci')
            elif ratio < 0:
                print('\nInterpretacja:\nAsymetria lewostronna w zawęzonym obszarze zmiennosci')
            else:
                print('\nInterpretacja:\nRozkład symetryczny w zawęzonym obszarze zmiennosci')
    return ratio


def positional_ratio_of_concentration(make=False, individual=True):
    if individual:
        concen = (decile9(data) - decile1(data)) / (quartile3(data) - quartile1(data))
        concen = round(concen, 3)
        if make:
            print('W = (D9 - D1) / (Q3 - Q1) \nW = (%s - %s) / (%s - %s) = %s' % (
            decile9(data), decile1(data), quartile3(data), quartile1(data), concen))
            if concentratrion(concen) == 1:
                print('\nInterpretacja:\n Rozkład normalny w zawężonym obszarze zmienności')
            elif concentratrion(concen) == 2:
                print('\nInterpretacja:\n Rozkład wysmukły w zawężonym obszarze zmienności')
            else:
                print('\nInterpretacja:\n Rozkład spłaszczony w zawężonym obszarze zmienności')
    else:
        concen = (decile9(data, False, False) - decile1(data, False, False)) / (
                    quartile3(data, False, False) - quartile1(data, False, False))
        concen = round(concen, 3)
        if make:
            print('W = (D9 - D1) / (Q3 - Q1) \nW = (%s - %s) / (%s - %s) = %s' % (
            decile9(data, False, False), decile1(data, False, False), quartile3(data, False, False),
            quartile1(data, False, False), concen))
            if concentratrion(concen) == 1:
                print('\nInterpretacja:\n Rozkład normalny w zawężonym obszarze zmienności')
            elif concentratrion(concen) == 2:
                print('\nInterpretacja:\n Rozkład wysmukły w zawężonym obszarze zmienności')
            else:
                print('\nInterpretacja:\n Rozkład spłaszczony w zawężonym obszarze zmienności')
    return concen


while run:
    menu()
    answer = input('Co chcesz zrobic? ')
    if answer == '1':
        if load_data():
            run2 = True
            while run2:
                print('\nDane wczytane poprawnie')
                menu2()
                answer2 = input('Co chcesz zrobic? ')
                if answer2 == '1':
                    print(data)
                elif answer2 == '2':
                    data.clear()
                    run2 = False
                    continue
                elif answer2 == '3':
                    run3 = True
                    while run3:
                        menu3()
                        answer3 = input('Co chcesz zrobic? ')
                        if answer3 == '1':
                            print('średnia: \n')
                            arithmetic_mean(data, True)
                            print('\nwariancja: \n')
                            variance(data, True)
                            print('\nodchylenie standardowe: \n')
                            standard_deviation(True)
                            print('\nwspolczynnik wariancji: \n')
                            ratio_of_variation(True)
                            print('\ntrzeci moment centralny: \n')
                            third_central_moment(data, True)
                            print('\nwspolczynnik asymetrii: \n')
                            ratio_of_asymmetry(True)
                            print('\nczwarty moment centralny: \n')
                            fourth_central_moment(data, True)
                            print('\nwspolczynnik koncentracji: \n')
                            ratio_of_concentration(True)
                            print('\n\nMiary pozycyjne:\n')
                            print('mediana: \n')
                            median(data, True)
                            print('\nkwartyl pierwszy: \n')
                            quartile1(data, True)
                            print('\nkwartyl trzeci: \n')
                            quartile3(data, True)
                            print('\ndecyl pierwszy: \n')
                            decile1(data, True)
                            print('\ndecyl dziewiąty: \n')
                            decile9(data, True)
                            print('\nodchylenie ćwiartkowe: \n')
                            quartile_deviation(True)
                            print('\npozycyjny wspolczynnik zmienności: \n')
                            positional_ratio_of_variation(True)
                            print('\npozycyjny wspolczynnik asymetrii: \n')
                            positional_ratio_of_asymmetry(True)
                            print('\npozycyjny wspolczynnik koncentracji: \n')
                            positional_ratio_of_concentration(True)
                        elif answer3 == '2':
                            print('\nIlosc przedziałow: \n')
                            number_of_intervals(data, True)
                            intervals_func(data)
                            print('średnia: \n')
                            arithmetic_mean(data, True, False)
                            print('\nwariancja: \n')
                            variance(data, True, False)
                            print('\nodchylenie standardowe: \n')
                            standard_deviation(True, False)
                            print('\nwspolczynnik wariancji: \n')
                            ratio_of_variation(True, False)
                            print('\ntrzeci moment centralny: \n')
                            third_central_moment(data, True, False)
                            print('\nwspolczynnik asymetrii: \n')
                            ratio_of_asymmetry(True, False)
                            print('\nczwarty moment centralny: \n')
                            fourth_central_moment(data, True, False)
                            print('\nwspolczynnik koncentracji: \n')
                            ratio_of_concentration(True, False)
                            print('\n\nMiary pozycyjne:\n')
                            print('mediana: \n')
                            median(data, True, False)
                            print('\nkwartyl pierwszy: \n')
                            quartile1(data, True, False)
                            print('\nkwartyl trzeci: \n')
                            quartile3(data, True, False)
                            print('\ndecyl pierwszy: \n')
                            decile1(data, True, False)
                            print('\ndecyl dziewiąty: \n')
                            decile9(data, True, False)
                            print('\nodchylenie ćwiartkowe: \n')
                            quartile_deviation(True, False)
                            print('\npozycyjny wspolczynnik zmienności: \n')
                            positional_ratio_of_variation(True, False)
                            print('\npozycyjny wspolczynnik asymetrii: \n')
                            positional_ratio_of_asymmetry(True, False)
                            print('\npozycyjny wspolczynnik koncentracji: \n')
                            positional_ratio_of_concentration(True, False)
                        elif answer3 == '3':
                            run3 = False
                        else:
                            pass
                elif answer2 == '4':
                    run2 = False
                else:
                    pass
        else:
            print('Nie wczytano danych, popraw wprowadzone dane i sprobuj ponownie')

    if answer == '2':
        run = False
