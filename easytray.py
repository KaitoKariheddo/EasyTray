import gi
import signal
import sys

gi.require_version('Gtk', '3.0')
gi.require_version("AppIndicator3", '0.1')
gi.require_version("Notify", '0.7')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

#Icon Titel setzen
APPINDICATOR_ID = "Easy Tray"

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, gtk.STOCK_INFO, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    #Menüeinträge nach folgendem Muster anlegen, eintrag_ZAHL hochzählen
    #label = Angezeigter Eintrag; testFunktion = Name der zu definierenden Funktion
    eintrag_2 = gtk.MenuItem(label="Test")
    eintrag_2.connect('activate', testFunktion)
    menu.append(eintrag_2)

    eintrag_1 = gtk.MenuItem(label="Verlassen")
    eintrag_1.connect('activate', verlassen)
    menu.append(eintrag_1)

    menu.show_all()
    return menu

def verlassen(_):
    notify.uninit()
    gtk.main_quit()
    sys.exit()

#So werden Funktionen definiert
def testFunktion(_):
    notify.Notification.new("Banapfel").show()
    
if __name__== '__main__':
    main = main()
    gtk.main()

