import json
import requests
import webbrowser
from tkinter import *
from requests.exceptions import ConnectionError
from tkinter import filedialog
from PIL import ImageTk, Image

symbollist=[]

def main(var):
    var=str(var)
    list1=[]
    list2=[]
    try:
        r=requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol="+ var + "&api_token=wDlGeK1dKNkRmKknWMEyMXmFAHeqddSElO07Th6uqZy5Qx1bMMuZmGdrrtQE")
        r2=requests.get("https://api.worldtradingdata.com/api/v1/history?symbol="+ var + "&api_token=wDlGeK1dKNkRmKknWMEyMXmFAHeqddSElO07Th6uqZy5Qx1bMMuZmGdrrtQE")
        try:
            if (r.status_code == 200):
        
                datajson = r.json()
            
            else:
                data = "Error has occured"
                #writeHTML(data)
            if r2.status_code == 200:
                datajson2=r2.json()
                counter=0
                for i in datajson2['history']:
                    list1.insert(0, datajson2['history'][str(i)]['close'])
                for i in datajson2['history']:
                    list2.insert(0,str(i)[0:4])
                    
            myfile=open("API.html","w")       
            myfile.write("<!DOCTYPE HTML><html><head><link rel=" 'stylesheet' " href=" 'stocks.css' "></head><body><ul><li><a class=" 'active' " href=" 'API.html' ">Home</a></li><li><a href=" 'stocks.html' ">Graph</a></li><li><a href=" 'mutualfund.html' ">Compare and Contrast</a></li></ul><table><tr><td>"+datajson['data'][0]['name']+"("+datajson['data'][0]['symbol']+")"+"</td></tr><tr><td>"+datajson['data'][0]['volume']+" shares traded today</td></tr><tr><td>Current price is "+datajson['data'][0]['price']+"(" +datajson['data'][0]['currency']+ ")</td></tr><tr><td>There are "+datajson['data'][0]['shares']+" shares in total</td></tr><tr><td>"+datajson['data'][0]['name'] +" has a total value of "+datajson['data'][0]['market_cap']+" dollars and is on the "+datajson['data'][0]['stock_exchange_long']+"</td></tr></table></body></html>")
            myfile.close()
                    
            
            myfile = open("stocks.html","w")
            myfile.write("<!DOCTYPE HTML><html><head><link rel=" 'stylesheet' " href=" 'stocks.css' "></head><body><ul><li><a class=" 'active' " href=" 'API.html' ">Home</a></li><li><a href=" 'stocks.html' ">Graph</a></li><li><a href=" 'mutualfund.html' ">Compare and Contrast</a></li></ul><canvas id="+" 'chartjs-0' "+"></canvas><script src=" 'https://cdn.jsdelivr.net/npm/chart.js@2.8.0' "></script><script src=" 'https://canvasjs.com/assets/script/canvasjs.min.js' "></script><script>var ctx = document.getElementById('chartjs-0').getContext('2d');var chart = new Chart(ctx, {type: 'line',data: {labels: [")
            for i in range(len(list2)):
                if i !=0:
                    myfile.write("," + list2[i] )
                else:
                    myfile.write(list2[i])
            myfile.write("],datasets: [{label: 'Stock Price',data: [")
            for i in range(len(list1)):
                if i !=0:
                    myfile.write("," + list1[i] )
                else:
                    myfile.write(list1[i])
            myfile.write("],pointRadius:0}]},options: {}});</script></body></html>")
            myfile.close()
            
        except:
            T2 = Text(root, height=4, width=30,bg='deep sky blue')
            T2.grid(row=2, column=0,padx=30, pady=25)
            T2.insert(END, "Sorry, this symbol is not in \nthe database, it will be \ndeleted. Please select a new \nstock")
            #deletestock(var)
    except ConnectionError as e:    # This is the correct syntax
        print("Network error")
        T2 = Text(root, height=2, width=30,bg='deep sky blue')
        T2.grid(row=2, column=0,padx=30, pady=25)
        T2.insert(END, "Network error")
        
def makeList():
    myfile=open("stocksymbols.json","r")
    symbol=myfile.read()
    stuff=json.loads(symbol)
    for i in range(len(stuff)):
        symbollist.append(stuff[i]['Symbol'])
    myfile.close()
    return symbollist
def deletestock(a):
    list3=[]
    myfile=open("stocksymbols.json","r")
    symbol=myfile.read()
    stuff=json.loads(symbol)
    for i in range(len(stuff)):
        if a==stuff[i]['Symbol']:
            stuff.remove(stuff[i])
            break
    stuffstr=json.dumps(stuff)
    myfile.close()
    myfile=open("stocksymbols.json",'w')
    myfile.write(stuffstr)
    myfile.close()

def websiteopen():
    list1=[]
    list2=[]
    list3=[]
    date=''
    compare1=var2.get()
    compare2=var3.get()
    r3=requests.get("https://api.worldtradingdata.com/api/v1/history?symbol="+ compare1 + "&api_token=wDlGeK1dKNkRmKknWMEyMXmFAHeqddSElO07Th6uqZy5Qx1bMMuZmGdrrtQE")
    r4=requests.get("https://api.worldtradingdata.com/api/v1/history?symbol="+ compare2 + "&api_token=wDlGeK1dKNkRmKknWMEyMXmFAHeqddSElO07Th6uqZy5Qx1bMMuZmGdrrtQE")
    datajson3 = r3.json()
    datajson4 = r4.json()
    if len(datajson3['history'])>len(datajson4['history']):
        for i in datajson4['history']:
            date=str(i)
        for i in datajson3['history']:
            list2.insert(0,str(i)[0:4])
            if str(i)==date:
                break
    elif len(datajson4['history'])>len(datajson3['history']):
        for i in datajson3['history']:
            date=str(i)
        for i in datajson4['history']:
            list2.insert(0,str(i)[0:4])
            if str(i)==date:
                break
    else:
        for i in datajson4['history']:
            list2.insert(0,str(i)[0:4])
    
    
    for i in datajson4['history']:
        list1.insert(0, datajson4['history'][str(i)]['close'])
        if str(i)==date:
                break
    for i in datajson3['history']:
        list3.insert(0, datajson3['history'][str(i)]['close'])
        if str(i)==date:
                break
    
    myfile = open("mutualfund.html","w")
    myfile.write("<!DOCTYPE HTML><html><head><link rel=" 'stylesheet' " href=" 'stocks.css' "></head><body><ul><li><a class=" 'active' " href=" 'API.html' ">Home</a></li><li><a href=" 'stocks.html' ">Graph</a></li><li><a href=" 'mutualfund.html' ">Compare and Contrast</a></li></ul><canvas id="+" 'chartjs-0' "+"></canvas><script src=" 'https://cdn.jsdelivr.net/npm/chart.js@2.8.0' "></script><script src=" 'https://canvasjs.com/assets/script/canvasjs.min.js' "></script><script>var ctx = document.getElementById('chartjs-0').getContext('2d');var chart = new Chart(ctx, {type: 'line',data: {labels: [")
    for i in range(len(list2)):
        if i !=0:
            myfile.write("," + list2[i] )
        else:
            myfile.write(list2[i])
    myfile.write("],datasets: [{label: ' "+datajson4['name']+" ',borderColor: '#AEC6CF',data: [")
    for i in range(len(list1)):
        if i !=0:
            myfile.write("," + list1[i] )
        else:
            myfile.write(list1[i])
    myfile.write("],pointRadius:0}, {label: '"+datajson3['name']+"', data: [")
    for i in range(len(list3)):
        if i !=0:
            myfile.write("," + list3[i] )
        else:
            myfile.write(list3[i])
    myfile.write("],pointRadius:0}]},options: {}});</script></body></html>")
    myfile.close()
        
    
    
def penis():
    var1=var.get()
    main(var1)
    websiteopen()
    url = 'file:/Users/oliver.tattersall/Desktop/Mycoding/Pythonunit/API.html'
    webbrowser.open(url, new=2)

root=Tk()
root.title("Stocks")
root.geometry("1200x800+0+0")
root.config(bg='deep sky blue')

OPTIONS=makeList()
var=StringVar(root)
var.set(OPTIONS[0])
w=OptionMenu(root,var,*OPTIONS, command=main)
w.grid(row=1,column=0, padx=30,pady=25, sticky=W)
var2=StringVar(root)
var2.set(OPTIONS[0])
w2=OptionMenu(root,var2,*OPTIONS)
w2.grid(row=1,column=1, padx=30,pady=25, sticky=W)
var3=StringVar(root)
var3.set(OPTIONS[0])
w3=OptionMenu(root,var3,*OPTIONS)
w3.grid(row=1,column=2, padx=30,pady=25, sticky=W)

T = Text(root, height=2, width=30,bg='deep sky blue')
T.grid(row=0, column=0,padx=30, pady=25,sticky=W)
T.insert(END, "Pick a stock to learn more \nabout")

T3 = Text(root, height=2, width=30,bg='deep sky blue')
T3.grid(row=0, column=1,padx=30, pady=25,sticky=W)
T3.insert(END, "Pick 2 stocks to compare")


imgframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
imgframe.grid(row=3,column=0, padx=10,pady=5, sticky=W)
canvas = Canvas(imgframe,height=450,width=600)
canvas.grid(row=0,column=0)
myimage = Image.open("stocks.jpg")
#myimage = myimage.resize((200, 150), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimage)
canvas.create_image(0, 0, image=myimg, anchor = NW)

button=Button(root, text="go to website",fg='medium blue', command=penis)
button.grid(row=4,column=0)


root.mainloop()
