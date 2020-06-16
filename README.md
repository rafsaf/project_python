# Projekt na Programowanie 2 UWr

## Instalacja(LinuxMint Ubuntu 19.3):

Można instalować np. w ~/Desktop

```linux
sudo apt-get update
sudo apt-get upgrade python3
sudo apt-get install python3-pip git
git clone https://github.com/rafsaf/project_python.git
```
Spis bibliotek z których korzysta projekt jest w pliku requirements.txt.
Najlepiej korzystać z virtualenv(lub posiadać wymienione biblioteki).
```linux
pip3 install virtualenv
cd project_python
virtualenv venv
source venv/bin/activate
```
Po pomyślnym uruchomieniu (venv):
```linux
pip3 install -r requirements.txt
```
Aby korzystać z możliwości graficznej obsługi naszej bazy danych Sqlite będzie też potrzebny program [Sqlite Browser](https://sqlitebrowser.org/)
```linux
sudo apt-get install sqlitebrowser
```
Następnie w utworzonym folderze project_python uruchamiamy setup.py
```linux
python3 setup.py
```

Module classes
--------------
File with classes used in program 

Variables
---------
BASE_DIR

DATABASE_PATH

Classes
-------
Bilans 
    Parent class for money results from all domains

    Ancestors (in MRO)
    ------------------
    classes.Bilans
    builtins.object

    Descendents
    -----------
    classes.Podatki_i_czynsze
    classes.Dochod_ze_sprzedazy
    classes.Pensje_pracownikow
    classes.Inne

    Static methods
    --------------
    __init__(self)
        Initialize self.  See help(type(self)) for accurate signature.

    get_another_month(self, number_int=-1)
        method to get another month, integer below 0 returns previous months and above 0 returns next months

    Instance variables
    ------------------
    current_month

    today

Dochod_ze_sprzedazy 
    Represents money earned in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with

    Ancestors (in MRO)
    ------------------
    classes.Dochod_ze_sprzedazy
    classes.Bilans
    builtins.object

    Static methods
    --------------
    __init__(self, month_number_int=0)
        Initialize self.  See help(type(self)) for accurate signature.

    fetch_data_from_database(self)
        Fetch data about month from database table DOCHOD_ZE_SPRZEDAZY

    get_all_money_from_month(self)
        returns result-number of money in month

    get_another_month(self, number_int=-1)
        method to get another month, integer below 0 returns previous months and above 0 returns next months

    get_name_of_month(self)
        used to get month name from number

    Instance variables
    ------------------
    month_end

    month_start

Draw_plot_one_month 
    Class used to represent all money results for specific month, including all sectors

    draw() method creates pyplot digrams to sum up results

    Ancestors (in MRO)
    ------------------
    classes.Draw_plot_one_month
    builtins.object

    Static methods
    --------------
    __init__(self, month_number_int=0)
        Initialize self.  See help(type(self)) for accurate signature.

    draw(self)
        creates pyplot histogram for money results in month

    get_ys_for_plot(self, result_list_from_fetch_data)
        method converting list of (day-how_much_money) tuples from classes

    Instance variables
    ------------------
    dochod

    inne

    pensje

    podatki

Inne 
    Represents money spent or earned from other districts in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with

    Ancestors (in MRO)
    ------------------
    classes.Inne
    classes.Bilans
    builtins.object

    Static methods
    --------------
    __init__(self, month_number_int=0)
        Initialize self.  See help(type(self)) for accurate signature.

    fetch_data_from_database(self)
        Fetch data about month from database table INNE

    get_all_money_from_month(self)
        returns result-number of money in month

    get_another_month(self, number_int=-1)
        method to get another month, integer below 0 returns previous months and above 0 returns next months

    get_name_of_month(self)
        used to get month name from number

    get_year(self)

    Instance variables
    ------------------
    month_end

    month_start

Month_text_sum_up 
    Class used to sum up money results which are represented later by text in tkinter module

    Ancestors (in MRO)
    ------------------
    classes.Month_text_sum_up
    builtins.object

    Static methods
    --------------
    __init__(self, month_number_int=0)
        Initialize self.  See help(type(self)) for accurate signature.

    return_text_for_3_last_months(self, number=3)
        text informations about last 3 months 

        number- int how much months before actual month consider

    return_text_for_month(self)
        text informations about specified month

    Instance variables
    ------------------
    dochod

    inne

    pensje

    podatki

Pensje_pracownikow 
    Represents money spent on salaries etc. in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with

    Ancestors (in MRO)
    ------------------
    classes.Pensje_pracownikow
    classes.Bilans
    builtins.object

    Static methods
    --------------
    __init__(self, month_number_int=0)
        Initialize self.  See help(type(self)) for accurate signature.

    fetch_data_from_database(self)
        Fetch data about month from database table PENSJE_PRACOWNIKOW

    get_all_money_from_month(self)
        returns result-number of money in month

    get_another_month(self, number_int=-1)
        method to get another month, integer below 0 returns previous months and above 0 returns next months

    get_name_of_month(self)
        used to get month name from number

    Instance variables
    ------------------
    month_end

    month_start

Podatki_i_czynsze 
    Represents money spent on taxes etc. in ONE SPECIFIC month 

    Method get_another_month() from parent class Bilans is used to set month to work with

    Ancestors (in MRO)
    ------------------
    classes.Podatki_i_czynsze
    classes.Bilans
    builtins.object

    Static methods
    --------------
    __init__(self, month_number_int=0)
        Initialize self.  See help(type(self)) for accurate signature.

    fetch_data_from_database(self)
        Fetch data about month from database table PODATKI_I_CZYNSZE

    get_all_money_from_month(self)
        returns result-number of money in month

    get_another_month(self, number_int=-1)
        method to get another month, integer below 0 returns previous months and above 0 returns next months

    get_name_of_month(self)
        used to get month name from number

    Instance variables
    ------------------
    month_end

    month_start
