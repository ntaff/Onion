import requests
import re

#ping = requests.get('http://3g2upl4pq6kufc4m.onion')
#print(ping.status_code)

fin = open("test.md", "r")
content = fin.readlines()
content = [x.strip() for x in content]
fin.close()
fin = open("test.md", "w+")
for line in content:
    print(line)
    s = re.search('([a-zA-Z0-9.\/:[\]()-]*]*).\|.([a-zA-Z0-9.\/:[\]()-]*]*).\|.([a-zA-Z0-9.\/:[\]()!-]*]*)', line)
    if s :
        if ".onion" in s.groups()[1]:
            ping = 99
            if ping != 200 :
    	           fin.write(line.replace(s.groups()[2], '![down](https://img.shields.io/badge/Statut-DOWN-red)')+'\n')
            if ping == 200 :
                   fin.write(line.replace(s.groups()[2], '![up](https://img.shields.io/badge/Statut-UP-green)')+'\n')
        else :
            fin.write(line+'\n')
    else :
        fin.write(line+'\n')
fin.close()
