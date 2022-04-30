# EasyTray
Simple Tray Menu in Python

Inspired by [candidtim](https://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html)

## Dependencies
`sudo pacman -S python gobject-introspection gtk3 libnotify`

## Add Entry:
```
    eintrag_2 = gtk.MenuItem(label="Test")
    eintrag_2.connect('activate', testFunktion)
    menu.append(eintrag_2)
```
Duplicate this block

Count up **eintrag_X**
Set **label="ENTRY"**
Name function **testFunktion**

## Define Function
```
    def testFunktion(_):
        YOUR CODE
```

## Examples
```
    import os
    import subprocess
    ...
    # in def Function() 
    os.system(command)
    # or.. for starting a script
    subprocess.run(["path/to/script", "arguments"], shell=True)
```
