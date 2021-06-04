from Zeiterfassung import start_time
from Zeiterfassung import end_time
from Zeiterfassung import option
from Zeiterfassung import again
from Zeiterfassung import start_pause
from Zeiterfassung import end_pause
import csv
from Zeiterfassung import get_date
from Zeiterfassung import get_year
from Zeitbearbeitung import sort_read_csv_entries
from Zeitbearbeitung import read_date_from_csv
from Zeitbearbeitung import final_sorting_zeiten
import tkinter
import tkinter.messagebox
from tkinter import *
from Zeiterfassung import create_zeiten_csv



#Tutorial:
#https://www.youtube.com/watch?v=-BFzBkrblAw

#Erzeugt hintergrundfenster

Fenster = tkinter.Tk()
Fenster.title('Zeiterfassung')
Fenster.geometry('450x320')

buttonEinstempeln = Button(master=Fenster, bg='DeepSkyBlue2', text='Einstempeln', command=start_time)#mit command= kann man eine methode aufrufen
buttonEinstempeln.place(x=55, y=55, width=120, height=30)

buttonAusstempeln = Button(master=Fenster, bg='DeepSkyBlue2', text='Ausstempeln', command=end_time)#mit command= kann man eine methode aufrufen
buttonAusstempeln.place(x=55, y=155, width=120, height=30)

buttonPause_Einstempeln = Button(master=Fenster, bg='DeepSkyBlue2', text='Pause_Einstempeln', command=start_pause)#mit command= kann man eine methode aufrufen
buttonPause_Einstempeln.place(x=255, y=55, width=120, height=30)

buttonPause_Ausstempeln = Button(master=Fenster, bg='DeepSkyBlue2', text='Pause_Ausstempeln', command=end_pause)#mit command= kann man eine methode aufrufen
buttonPause_Ausstempeln.place(x=255, y=155, width=120, height=30)

buttongenerate_Zeiten_csv = Button(master=Fenster, bg='green3', text='Zeiten_CSV_erstellen', command=create_zeiten_csv)
buttongenerate_Zeiten_csv.place(x=155, y=255, width=120, height=30)


print('im working trust me')
Fenster.mainloop()


