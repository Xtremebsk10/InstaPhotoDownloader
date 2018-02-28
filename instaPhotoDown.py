import requests
from bs4 import BeautifulSoup
import re
import urllib2
import tkinter


def getPhoto():
    #search photo with the given link
    link = u_input.get()
    req = requests.get(link)
    soup = BeautifulSoup(req.content)
    photos = soup.find_all("script")
    text = str(photos[2])
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    #======instagram's first link of the third script is the maximum quality image link========
    photo_link = urls[0]
    
    #saving image
    img = urllib2.urlopen(photo_link)
    name = "image" + ".jpg"
    localFile = open(name,'wb')
    localFile.write(img.read())
    localFile.close()
    
    #showing "done" label
    done_lab.pack()
    
#init window (500x300)
master = Tk()
master.geometry("500x300")
master.title("Insta Photo Downloader")

#objects init
tit = Label(master, text = "Instagram photo downloader", font=("Arial",30))
desc = Label(master, text = "Please, insert the link of the phtoto you want to download", font=("Arial", 12))
u_input = Entry(master, bg='white', width = 60)
button = Button(master, text = "Download photo", command = getPhoto)
done_lab = Label(master, text = "Done!")

#style order
tit.pack(pady=35)
desc.pack()
u_input.pack(pady=20)
button.pack(pady = 20)
done_lab.pack_forget()


master.mainloop()