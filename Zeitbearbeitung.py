import csv
all_csv_entries = []
def read_date_from_csv():
    all_csv_entries = []
    with open('Zeitenzwischenspeicher.csv', 'r', newline='') as f:
        reader = csv.reader(f, delimiter= ',')
        for row in reader:
           all_csv_entries.append(row)
        print('Listeneinträge:')
        print(all_csv_entries)
    return all_csv_entries

def sort_read_csv_entries(all_csv_entries):
    counter = -1
    laenge_ursprungsliste = len(all_csv_entries)
    sortierte_datum_zeiten_liste = []
    for entrie in all_csv_entries:
        counter = counter + 1
        #sortierte_datum_zeiten_liste = [ding for ding in all_csv_entries if str(entrie) in str(ding)]# auskommatiert wenn zeile 48 aktiv
        #print('counter:' + str(counter))
        if len(entrie) == 1: #wenn ein datum auftaucht
            date1 = entrie # reset date1 mit neuem datum
            #print('datum:')
            #print(date1)
            if date1 not in sortierte_datum_zeiten_liste:#überprüfung ob date1 schon mal in liste vorhanden ist ( alternativ nur einen eintrag in liste vergleichen mit date1)
                sortierte_datum_zeiten_liste.append(date1)
                selected_csv_entries = all_csv_entries[counter:laenge_ursprungsliste] #verkürzung der liste nach jedem date1 inklusive date1
                second_counter = 0
                #print('einmalig')
                for thing in selected_csv_entries:
                    second_counter = second_counter + 1
                    #print(second_counter)
                    times = []#reset zeitenliste
                    selected_csv_entries_without_date1 = selected_csv_entries[second_counter:laenge_ursprungsliste] #verkürzung ohne date1 um zeiten rauszuextrahieren/
                    #print('thing:')
                    #print(thing)
                    if thing == date1:# immer wenn das gleiche datum auftaucht (beginnt schon beim ursprungsdatum)
                        #print('gleiches datum appeared')
                        #to test (untere zeile)
                        #sortierte_datum_zeiten_liste = [ding for ding in all_csv_entries if str(thing) in str(ding)]
                        #alternativvariante die funzt
                        for time in selected_csv_entries_without_date1:
                            if len(time) == 1:
                                print('break')
                                break
                            #print('zeit hinzugefügt')
                            times.append(time) #hier werden die zeiten erfasst bis zum nächsten datum (ausschließlich)
                            sortierte_datum_zeiten_liste.append(time)#auskommatiert weil zeile 19 aktiv
    print(sortierte_datum_zeiten_liste)
    return sortierte_datum_zeiten_liste
def final_sorting_zeiten():
    all_csv_entries_new = []
    final_list_zeiten = []
    zwischen_list_zeiten = []
    final_list_zeiten_new= []
    with open('Zeiten_sorted_save.csv', 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            all_csv_entries_new.append(row)
            print('all_csv_entries_new')
            print(all_csv_entries_new)
    mitzaehler = 0

    for item in all_csv_entries_new:
        final_list_zeiten = [ding for ding in all_csv_entries_new if str(item) in str(ding)]
        print(final_list_zeiten)
    for teil in final_list_zeiten:
        teil = str(teil)
        teil = teil.replace('"','')
        teil = teil.replace('[','')
        teil = teil.replace("'","")
        teil = teil.replace(']','')
        teil = teil.replace('"', '')
        final_list_zeiten_new.append(teil)
        #mitzaehler = mitzaehler + 1
        #list_laenge = len(all_csv_entries_new)
        #print('mitzähler' + str(mitzaehler))
        #print('Listlänge:' + str(list_laenge))

        #if mitzaehler < list_laenge:
            #if item != all_csv_entries_new[mitzaehler]:
                #if item not in zwischen_list_zeiten:
                    #zwischen_list_zeiten.append(item)
                    #item = str(item)
                    #item = item.replace('"','')
                    #item = item.replace('[','')
                    #item = item.replace("'","")
                    #item = item.replace(']','')
                    #item = item.replace('"', '')
                    #print('item:')
                    #print(item)
        #final_list_zeiten.append(item)
    #print('finallist:')
    #print(final_list_zeiten)
    return final_list_zeiten_new


if __name__ == "__main__":
    read_date_from_csv()
    sort_read_csv_entries(all_csv_entries)
    final_sorting_zeiten()
if __name__ == "__Zeiterfassung__":
    read_date_from_csv()
    sort_read_csv_entries(all_csv_entries)
    final_sorting_zeiten()

