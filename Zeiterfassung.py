from datetime import datetime
from tkinter import *
import csv
from Zeitbearbeitung import read_date_from_csv
from Zeitbearbeitung import sort_read_csv_entries
from Zeitbearbeitung import final_sorting_zeiten

def get_date():
    date = datetime.now()
    date = str(date)
    date = date[0:10]
    datelist = []
    datelist.append(date)
    print(datelist)
    return datelist
def get_year():
    year = datetime.now()
    year = str(year)
    year = year[0:4]
    print(year)
    return year
def start_time():
    start = datetime.now()
    start = str(start)
    start = start[11:19]
    startlist = []
    startlist.append(start)
    startlist.insert(0, "Arbeitsbeginn: ")
    print(startlist)
    datealreadydone = False
    something_happend = True
    date = get_date()
    year = get_year()
    with open('Zeitenzwischenspeicher.csv', 'a',
              newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
        if datealreadydone == False:
            writer.writerow(date)
            datealreadydone = True
        writer.writerow(startlist)
    if something_happend == True:
        all_csv_entries = read_date_from_csv()
        Zeitliste = sort_read_csv_entries(all_csv_entries)
        with open('Zeiten_sorted_save.csv', 'a',
                  newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
            writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
            writer.writerow(Zeitliste)


    return startlist
def end_time():
    end = datetime.now()
    end = str(end)
    end = end[11:19]
    endlist = []
    endlist.append(end)
    endlist.insert(0, "Arbeitsende: ")
    datealreadydone = False
    something_happend = True
    date = get_date()
    year = get_year()
    with open('Zeitenzwischenspeicher.csv', 'a',
              newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
        if datealreadydone == False:
            writer.writerow(date)
            datealreadydone = True
        writer.writerow(endlist)
    if something_happend == True:
        all_csv_entries = read_date_from_csv()
        Zeitliste = sort_read_csv_entries(all_csv_entries)
        with open('Zeiten_sorted_save.csv', 'a',
                  newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
            writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
            writer.writerow(Zeitliste)


    print(endlist)
    return endlist
def start_pause():
    startpause = datetime.now()
    startpause = str(startpause)
    startpause = startpause[11:19]
    startpauselist = []
    startpauselist.append(startpause)
    startpauselist.insert(0, "Pausenbeginn: ")
    print(startpauselist)
    datealreadydone = False
    something_happend = True
    date = get_date()
    year = get_year()
    with open('Zeitenzwischenspeicher.csv', 'a',
              newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
        if datealreadydone == False:
            writer.writerow(date)
            datealreadydone = True
        writer.writerow(startpauselist)
    if something_happend == True:
        all_csv_entries = read_date_from_csv()
        Zeitliste = sort_read_csv_entries(all_csv_entries)
        with open('Zeiten_sorted_save.csv', 'a',
                  newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
            writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
            writer.writerow(Zeitliste)


    return startpauselist
def end_pause():
    endpause = datetime.now()
    endpause = str(endpause)
    endpause = endpause[11:19]
    endpauselist = []
    endpauselist.append(endpause)
    endpauselist.insert(0, "Pausenende: ")
    print(endpauselist)
    datealreadydone = False
    something_happend = True
    date = get_date()
    year = get_year()
    with open('Zeitenzwischenspeicher.csv', 'a',
              newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
        writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
        if datealreadydone == False:
            writer.writerow(date)
            datealreadydone = True
        writer.writerow(endpauselist)
    if something_happend == True:
        all_csv_entries = read_date_from_csv()
        Zeitliste = sort_read_csv_entries(all_csv_entries)
        with open('Zeiten_sorted_save.csv', 'a',
                  newline='') as f:  # ursprünglich w für write ( a ist adden/appendieren)
            writer = csv.writer(f)  # , quoting=csv.QUOTE_ALL keine lösung
            writer.writerow(Zeitliste)


    return endpauselist
def option():
    auswahlbedingung = 0
    while auswahlbedingung == 0:
        print("You can choose between these options: \n 1: Start working timer \n 2: Stop working timer \n 3: Have a break \n 4: Stop your break \n Which option would you like to use?: ")
        auswahl = input()
        auswahl = int(auswahl)
        if auswahl < 1 or auswahl > 4:
            auswahlbedingung = 0
            print("Please choose just one of the following Numbers: 1,2,3,4")
        else:
            auswahlbedingung = 1

    return auswahl
def again():
    answerbedingung = 0
    while answerbedingung == 0:
        print("Would you like to do another action?(Y/N): ")
        answer = input()
        answernumber = 0
        if answer == "y" or answer == "Y":
            answerbool = True
            answernumber = 1
        if answer == "n" or answer == "N":
            answerbool = False
            answernumber = 1
        if answernumber == 1:
            answerbedingung = 1
        else:
            answerbedingung = 0
    return answerbool
def create_zeiten_csv():
    final_zeiten_csv = []
    final_zeiten_csv = final_sorting_zeiten()
    with open('Zeiten.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(final_zeiten_csv)




if __name__ == "__main__":
    start_time()
    end_time()
    option()
    again()
    start_pause()
    end_pause()
    get_date()
    get_year()
