
import sqlite3
import datetime

from matplotlib import pyplot as plt
from dateutil.relativedelta import relativedelta
from setup import DATABASE_PATH


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
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
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
        return self.fetch_data_from_database()[1]
    
    def __str__(self):
        return "podatki i czynsze"


class Dochod_ze_sprzedazy(Bilans):
    """
    Represents money spent on taxes etc. in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with
    """

    def __init__(self, month_number_int=0):
        super().__init__()
        self.month_start = self.get_another_month(month_number_int)
        self.month_end = self.get_another_month(month_number_int + 1)

    def get_name_of_month(self):
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
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
        return self.fetch_data_from_database()[1]
    
    def __str__(self):
        return "dochód ze sprzedaży"


class Pensje_pracownikow(Bilans):
    """
    Represents money spent on taxes etc. in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with
    """

    def __init__(self, month_number_int=0):
        super().__init__()
        self.month_start = self.get_another_month(month_number_int)
        self.month_end = self.get_another_month(month_number_int + 1)
        print(self.month_end)

    def get_name_of_month(self):
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
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
        return self.fetch_data_from_database()[1]
    
    def __str__(self):
        return "Pensje pracownikow"


class Inne(Bilans):
    """
    Represents money spent on taxes etc. in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with
    """

    def __init__(self, month_number_int=0):
        super().__init__()
        self.month_start = self.get_another_month(month_number_int)
        self.month_end = self.get_another_month(month_number_int + 1)

    def get_name_of_month(self):
        name = self.month_start.strftime("%B")
        return name

    def fetch_data_from_database(self):
        conn = sqlite3.connect(DATABASE_PATH)
        cur = conn.cursor()
        cur.execute("select * from Inne where czas >=? and czas <=?;",
                    [self.month_start, self.month_end])
        all_data = cur.fetchall()
        print(all_data)
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
        return self.fetch_data_from_database()[1]
    
    def __str__(self):
        return "Inne"



class Draw_plot_one_month:

    def __init__(self, month_number_int=0):
        self.podatki = Podatki_i_czynsze(month_number_int)
        self.dochod = Dochod_ze_sprzedazy(month_number_int)
        self.pensje = Pensje_pracownikow(month_number_int)
        self.inne = Inne(month_number_int)
    
    def get_sum_up(self):

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
        axes[0].set_xticks([0.5,1,1.5,2,2.5])
        axes[0].set_xticklabels(labels)
        autolabel(x1)
        autolabel(x2)

        axes[1].plot([1,1],[2,2])
        plt.show()







x  = Draw_plot_one_month().get_sum_up()
