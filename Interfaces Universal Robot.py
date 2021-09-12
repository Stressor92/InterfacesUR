import socket
import time


HOST = "xxx.xx.x.xx"                    #IP Adresse vom UR
HOSTSERVER = "xxx.xx.x.xxx"             #Eigene IP einfügen
PORTDASHBOARD = 29999                   #Port vom Interface
PORTPRIMARY = 30001                     #Port vom Primary
PORTSERVER = 5050                       #Port zum Server (Irgendeinen freien Port festlegen)
PORTSECONDARY = 30002 


def Dashboard(command):                                         #Funktion um mit dem Dashboard zu interagieren; Übergabe Befehl
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Socket erstellen 
    s.connect((HOST, PORTDASHBOARD))                            #verbinden mit dem Interface
    data=s.recv(1024)                                           #Nachricht vom UR
    print(data)                                                 #Ausgabe der Nachricht
    s.sendall(str.encode(command))                              #Einen String(Command) an den UR Senden
    data=s.recv(1024)                                           #Nachricht vom UR
    print(data)                                                 #Ausgabe der Nachricht
    s.close()                                                   #Verbindung schließen                                  

def Primary(script):                                            #Funktion um mit dem Dashboard zu interagieren; Übergabe Befehl
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Socket erstellen 
    s.connect((HOST, PORTPRIMARY))                              #verbinden mit dem Interface
    s.sendall(str.encode(script))                               #ein Skriptbefehl an den UR Senden
    s.close()                                                   #Verbindung schließen   


def Secondary(script):                                            #Funktion um mit dem Dashboard zu interagieren; Übergabe Befehl
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Socket erstellen 
    s.connect((HOST, PORTSECONDARY))                              #verbinden mit dem Interface
    s.sendall(str.encode(script))                               #ein Skriptbefehl an den UR Senden
    s.close()                                                   #Verbindung schließen   

def Server(string):                                                   #Funktion um als Server zu fungieren ( Der Roboter muss versuchen auf den Server zuzugreifen (socket_open())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #Socket erstellen 
    s.bind((HOSTSERVER, PORTSERVER))                            #Server erstellen mit IP Adresse und eigenen Port                
    s.listen(1)                                                   # Anzahl der möglichen Verbindungen
    (clientsocket, address) = s.accept()                        #Verbindung akzeptieren
    print('Connected by', address)                              # Verbindung mit Adresse ausdrucken 
    data=clientsocket.recv(1024)                                 #Nachricht vom UR
    print(data)                                                 #Ausgabe der Nachricht
    #clientsocket.sendall(str.encode(string))                   #string senden, funktioniert noch nicht
                                                 

    #Beispiel für Dashboard command verschicken   
# Dashboard("popup hello world\n")                     #(/n wegen dem Datentyp String) 
# time.sleep(5)
# Dashboard("close popup\n")
# weitere Commands: https://s3-eu-west-1.amazonaws.com/ur-support-site/42728/DashboardServer_e-Series.pdf

    #Beispiel für Skriptbefehl über das PrimaryInterface verschicken  
#script = "def funktion():\n"                                   #Funktion definieren
#script += "pos=get_actual_tcp_pose()\n"
#script += "pos[2]=pos[2]+50/1000\n"
#script += "movej(pos)\n"
#script += "end\n"                                              #Funktion beenden
#Primary(script)                                                #Primary Interface ausführen




