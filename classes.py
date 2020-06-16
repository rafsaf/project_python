""" File with classes used in program """

import sqlite3
import datetime
import os

from matplotlib import pyplot as plt
from dateutil.relativedelta import relativedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'database.db')


class Bilans:
    """ Parent class for money results from all domains """

    def __init__(self):
        self.today = datetime.date.today()
        self.current_month = datetime.date(
            year=self.today.year, month=self.today.month, day=1)

    def get_another_month(self, number_int: int = -1):
        """ method to get another month, integer below 0 returns previous months and above 0 returns next months"""
        if number_int == 0:
            return self.current_month
        else:
            return self.current_month + relativedelta(months=+number_int)


class Podatki_i_czynsze(Bilans):
    """
    Represents money spent on taxes etc. in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with
    """

    def __init__(self, month_number_int=0):
        super().__init__()
        self.month_start = self.get_another_month(month_number_int)
        self.month_end = self.get_another_month(month_number_int + 1)

    def get_name_of_month(self):
        """ used to get month name from number """
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
        """ Fetch data about month from database table PODATKI_I_CZYNSZE"""
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("select * from Podatki_i_czynsze where czas >=? and czas <=?;",
                    [self.month_start, self.month_end])
        all_data = cur.fetchall()
        sum_of_money = 0
        result = []
        for data in all_data:
            date_from_str = datetime.datetime.strptime(data[1], "%Y-%m-%d")
            day = date_from_str.day
            sum_of_money += data[2]
            result.append((day, data[2]))
        # result is list of (DAY, MONEY) tuples
        return [result, sum_of_money]
    def get_all_money_from_month(self):
        """ returns result-number of money in month """
        return self.fetch_data_from_database()[1]
    
    def __str__(self):
        return "podatki i czynsze"


class Dochod_ze_sprzedazy(Bilans):
    """
    Represents money earned in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with
    """

    def __init__(self, month_number_int=0):
        super().__init__()
        self.month_start = self.get_another_month(month_number_int)
        self.month_end = self.get_another_month(month_number_int + 1)

    def get_name_of_month(self):
        """ used to get month name from number """
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
        """ Fetch data about month from database table DOCHOD_ZE_SPRZEDAZY"""
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("select * from Dochod_ze_sprzedazy where czas >=? and czas <=?;",
                    [self.month_start, self.month_end])
        all_data = cur.fetchall()
        sum_of_money = 0
        result = []
        for data in all_data:
            date_from_str = datetime.datetime.strptime(data[1], "%Y-%m-%d")
            day = date_from_str.day
            sum_of_money += data[2]
            result.append((day, data[2]))
        # result is list of (DAY, MONEY) tuples
        return [result, sum_of_money]
    def get_all_money_from_month(self):
        """ returns result-number of money in month """
        return self.fetch_data_from_database()[1]
    
    def __str__(self):
        return "dochód ze sprzedaży"


class Pensje_pracownikow(Bilans):
    """
    Represents money spent on salaries etc. in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with
    """

    def __init__(self, month_number_int=0):
        super().__init__()
        self.month_start = self.get_another_month(month_number_int)
        self.month_end = self.get_another_month(month_number_int + 1)


    def get_name_of_month(self):
        """ used to get month name from number """
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
        """ Fetch data about month from database table PENSJE_PRACOWNIKOW"""
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("select * from Pensje_pracownikow where czas >=? and czas <=?;",
                    [self.month_start, self.month_end])
        all_data = cur.fetchall()
        sum_of_money = 0
        result = []
        for data in all_data:
            date_from_str = datetime.datetime.strptime(data[1], "%Y-%m-%d")
            day = date_from_str.day
            sum_of_money += data[2]
            result.append((day, data[2]))
        # result is list of (DAY, MONEY) tuples
        return [result, sum_of_money]
    def get_all_money_from_month(self):
        """ returns result-number of money in month """
        return self.fetch_data_from_database()[1]
    
    def __str__(self):
        return "pensje pracownikow"


class Inne(Bilans):
    """
    Represents money spent or earned from other districts in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with
    """

    def __init__(self, month_number_int=0):
        super().__init__()
        self.month_start = self.get_another_month(month_number_int)
        self.month_end = self.get_another_month(month_number_int + 1)

    def get_name_of_month(self):
        """ used to get month name from number """
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
        """ Fetch data about month from database table INNE"""
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("select * from Inne where czas >=? and czas <=?;",
                    [self.month_start, self.month_end])
        all_data = cur.fetchall()
        sum_of_money = 0
        result = []
        for data in all_data:
            date_from_str = datetime.datetime.strptime(data[1], "%Y-%m-%d")
            day = date_from_str.day
            sum_of_money += data[2]
            result.append((day, data[2]))
        # result is list of (DAY, MONEY) tuples
        return [result, sum_of_money]
    def get_all_money_from_month(self):
        """ returns result-number of money in month """
        return self.fetch_data_from_database()[1]
    
    def get_year(self):
        return str(self.today.year)

    
    def __str__(self):
        return "inne"



class Draw_plot_one_month:
    """ Class used to represent all money results for specific month, including all sectors
    
    draw() method creates pyplot digrams to sum up results"""

    def __init__(self, month_number_int=0):
        self.podatki = Podatki_i_czynsze(month_number_int)
        self.dochod = Dochod_ze_sprzedazy(month_number_int)
        self.pensje = Pensje_pracownikow(month_number_int)
        self.inne = Inne(month_number_int)

    def get_ys_for_plot(self, result_list_from_fetch_data):
        """ method converting list of (day-how_much_money) tuples from classes """
        context:dict = {i:0 for i in range(1,32)}
        for element in result_list_from_fetch_data:
            context[element[0]] += element[1]
        for key, value in context.items():
            if key == 31:
                continue
            context[key+1] += value
        return [value for value in context.values()]

    def draw(self):
        """ creates pyplot histogram for money results in month """

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                if height != 0:
                    axes[0].annotate('{}'.format(height),
                                xy=(rect.get_x() + rect.get_width() / 2, height),
                                xytext=(0, 3),  # 3 points vertical offset
                                textcoords="offset points",
                                ha='center', va='bottom')



        # to create list with sum of money
        podatki = self.podatki.get_all_money_from_month()
        dochod = self.dochod.get_all_money_from_month()
        pensje = self.pensje.get_all_money_from_month()
        inne = self.inne.get_all_money_from_month()

        list_money_sectors = []
        list_money_sectors.append(podatki)
        list_money_sectors.append(dochod)
        list_money_sectors.append(pensje)
        list_money_sectors.append(inne)
        list_money_sectors.append(podatki+dochod+pensje+inne)

        gains = []
        loss = []

        for i in list_money_sectors:
            if i>0:
                gains.append(i)
                loss.append(0)
            elif i == 0:
                gains.append(0)
                loss.append(0)
            else:
                gains.append(0)
                loss.append(i)


        labels = [self.podatki, self.dochod, self.pensje, self.inne, "Łącznie"]        
        # pyplot
        f, axes = plt.subplots(2, 1)

        x1 = axes[0].bar([0.5,1,1.5,2,2.5], loss, 0.4, color='red', label='Straty')
        x2 = axes[0].bar([0.5,1,1.5,2,2.5], gains, 0.4, color='blue', label='Zyski')
        axes[0].legend(["Straty","Zyski"])
        axes[0].set_xticks([0.5,1,1.5,2,2.5])
        axes[0].set_xticklabels(labels)
        autolabel(x1)
        autolabel(x2)
        title = axes[0].set_title("Podsumowanie: {}, okres {} do {}* (bez początku miesiąca)".format(self.dochod.get_name_of_month(), self.dochod.month_start, self.dochod.month_end))
        title.set_position([0.5,1.1])


        xs = [i for i in range(1,32)]
        axes[1].plot(xs, self.get_ys_for_plot(self.podatki.fetch_data_from_database()[0]))
        axes[1].plot(xs, self.get_ys_for_plot(self.pensje.fetch_data_from_database()[0]))
        axes[1].plot(xs, self.get_ys_for_plot(self.dochod.fetch_data_from_database()[0]))
        axes[1].plot(xs, self.get_ys_for_plot(self.inne.fetch_data_from_database()[0]))
        axes[1].set_xticks([1,5,10,15,20,25,31])
        axes[1].legend([self.podatki, self.pensje, self.dochod, self.inne])

        plt.show()

class Month_text_sum_up:
    """ Class used to sum up money results which are represented later by text in tkinter module  """
    def __init__(self, month_number_int=0):
        self.podatki = Podatki_i_czynsze(month_number_int)
        self.dochod = Dochod_ze_sprzedazy(month_number_int)
        self.pensje = Pensje_pracownikow(month_number_int)
        self.inne = Inne(month_number_int)

    def return_text_for_month(self):
        """ text informations about specified month """
        month = self.podatki.get_name_of_month()
        podatki = self.podatki.get_all_money_from_month()    
        dochod = self.dochod.get_all_money_from_month()    
        pensje = self.pensje.get_all_money_from_month()    
        inne = self.inne.get_all_money_from_month()
        year = self.inne.get_year()
        if inne > 0:
            sign1 = "+"
        else:
            sign1 = "" 
        result = podatki + dochod + pensje + inne
        if result > 10000:
            sign2 = "+"
            rating = "Dobry rezultat"
        elif result < 0:
            sign2 = ""
            rating = "Zły rezultat"
        else: 
            if podatki == 0 and dochod == 0 and pensje == 0 and inne ==0:
                rating = "Brak danych"
            else:
                rating = "Średni rezultat- stagnacja"
        text_message = "Miesiac: {} {} \nPodatki: {} zł\nDochody: +{} zł\nPensje dla pracowników: {} zł\nInne wydatki: {}{} zł\nŁącznie: {}{} zł\n{}".format(month, year, podatki, dochod, pensje, sign1, inne, sign2, result, rating)
        
        return text_message

    def return_text_for_3_last_months(self, number=3):
        """ text informations about last 3 months 
        
        number- int how much months before actual month consider"""
        podatki = 0
        dochod = 0
        pensje = 0
        inne = 0
        result = 0
        month = ""
        for i in range(-number,1):
            podatki += Podatki_i_czynsze(i).get_all_money_from_month()
            dochod += Dochod_ze_sprzedazy(i).get_all_money_from_month()
            pensje += Pensje_pracownikow(i).get_all_money_from_month()
            inne += Inne(i).get_all_money_from_month()
            month += Inne(i).get_name_of_month() + ", "
        month = month.rstrip(", ")
        if inne > 0:
            sign1 = "+"
        else:
            sign1 = "" 
        result = podatki + dochod + pensje + inne
        if result > 10000:
            sign2 = "+"
            rating = "Dobry rezultat"
        elif result < 0:
            sign2 = ""
            rating = "Zły rezultat"
        else: 
            if podatki == 0 and dochod == 0 and pensje == 0 and inne ==0:
                rating = "Brak danych"
            else:
                rating = "Średni rezultat- stagnacja"
        text_message = "Miesiac: {}\nPodatki: {} zł\nDochody: +{} zł\nPensje dla pracowników: {} zł\nInne wydatki: {}{} zł\nŁącznie: {}{} zł\n{}".format(month, podatki, dochod, pensje, sign1, inne, sign2, result, rating)
        
        return text_message
    

