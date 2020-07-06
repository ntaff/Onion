import requests
import re
from time import sleep
import datetime
#print(requests.get('http://verified2ebdpvms.onion/favicon.ico').status_code)

# /!\ Activate Kalitorify first /!\


statuscodes = (200,301,302,401,403,504)
while(1):
    fin = open("test.md", "r")
    content = [x.strip() for x in fin.readlines()]
    fin.close()
    fin = open("test.md", "w+")
    for line in content:
        s = re.search('([a-zA-Z0-9.\/:[\]()-]*]*).\|.([a-zA-Z0-9.\/:[\]()-]*]*).\|.([a-zA-Z0-9.\/:[\]()!-]*]*)', line)
        if s :
            if ".onion" in s.groups()[1]:
                try :
                    if ping := requests.get(s.groups()[1], timeout=20, verify = False).status_code in statuscodes:
                        fin.write(line.replace(s.groups()[2], '![up](https://img.shields.io/badge/Statut-UP-green)')+'\n')
                    else :
    	                fin.write(line.replace(s.groups()[2], '![down](https://img.shields.io/badge/Statut-DOWN-red)')+'\n')
                except :
                    fin.write(line.replace(s.groups()[2], '![down](https://img.shields.io/badge/Statut-DOWN-red)')+'\n')
            else :
                fin.write(line+'\n')
        else :
            fin.write(line+'\n')
    fin.close()
    print(f"Fichier actualisé le {str(datetime.datetime.now())}")
    sleep(1800)
