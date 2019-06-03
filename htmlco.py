#python3
#
#htmlco.py html copy tool!
#
#htmlco.py free software;you can redistribute it and/or modify
#Htmlcopy is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#Copyright (c) 2019 1ibr4 <twitter@1ibr4  https://twitter.com/1ibr4>
#
#I made when I was 16
#
#
#
import urllib.request
def fileopen():
    try:
        file = open(file_name, 'w')
        file.write(result)
    except Exception as e:
        print(e)
    finally:
        file.close()




logo = open("logo.txt","r")

reads = logo.read()

print(reads)


url = input(('URL>'))
http = 'http'
quit = 'quit'
if http in url: 
    htmldata = urllib.request.urlopen(url)
    result = (htmldata.read().decode('UTF-8'))
    htmldata.close()
    file_name = input(('filename>'))
    if quit in file_name:
        print("Bye bye")
    else:
        fileopen()




elif quit in url:
    print("bye bye")
   
else:
    print("not found")
    
