import settings



with open(settings.CSV_FILE) as file:
    for line in file:
        print(line)


