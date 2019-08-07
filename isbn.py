from api_env import api_endpoint, api_key
from tkinter import *
from tkinter import scrolledtext
import requests

def btn_1_click():
	isbn = txt_1.get()
	res = get_isbn(api_key, api_endpoint, isbn)
	
	sctx_1.delete(1.0, END)
	sctx_1.insert(INSERT, res)

def get_isbn(api_key, api_endpoint, isbn):
    query = "isbn:" + isbn
    param = {'q':query, 'key':api_key}

    r = requests.get(url = api_endpoint, params = param)

    data = r.json()
    data = data['items'][0]['volumeInfo']
	
    res = ""
    res += 'Judul : ' + str(data['title']) + "\n"
    res += 'Pengarang : ' + "\n"
    for i in data['authors']: res += '- ' + str(i) + "\n"
    res += 'Jumlah Halaman : ' + str(data['pageCount']) + "\n"
    
    return res


isbn = "9781447299851"

window = Tk()
window.title("BookFind (ISBN Based)")
window.geometry('300x250')

lbl_1 = Label(window, text="Masukkan ISBN: ")
lbl_1.grid(column=2, row=0)

txt_1 = Entry(window, width=20)
txt_1.grid(column=2, row=1)

btn_1 = Button(window, text="Cari!", command=btn_1_click)
btn_1.grid(column=2, row=2)

sctx_1 = scrolledtext.ScrolledText(window, width=35, height=10)
sctx_1.grid(column=2, row=4)

window.mainloop()