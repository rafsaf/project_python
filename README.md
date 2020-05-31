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
pip3 install -r requirements.txt
```
Aby korzystać z możliwości graficznej obsługi bazy danych Sqlite3 będzie też potrzebny program [Sqlite Browser](https://sqlitebrowser.org/)

```linux
sudo apt-get install sqlitebrowser
```

Następnie w utworzonym folderze project_python uruchamiamy setup.py

```linux
python3 setup.py
```
