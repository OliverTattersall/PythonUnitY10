import json
import requests
import webbrowser
from tkinter import *
from requests.exceptions import ConnectionError
list1=[]
list2=[]
symbollist=[]

def main(value):
    list1=[]
    list2=[]
    try:
        r=requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol="+ value + "&api_token=ox4j7MTFbQnh0vO7GGeFSRVXuHT4K8qERHJxh8NTZpyhEe7Qf25GpXhrvizX")
        r2=requests.get("https://api.worldtradingdata.com/api/v1/history?symbol="+ value + "&api_token=ox4j7MTFbQnh0vO7GGeFSRVXuHT4K8qERHJxh8NTZpyhEe7Qf25GpXhrvizX")
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
            myfile = open("API2.html","w")
            myfile.write("<!DOCTYPE HTML><html><head></head><body><p>"+datajson['data'][0]['name']+"("+datajson['data'][0]['symbol']+")"+"</p><p>"+datajson['data'][0]['volume']+" shares traded today</p><canvas id="+" 'chartjs-0' "+"></canvas><script src=" 'https://cdn.jsdelivr.net/npm/chart.js@2.8.0' "></script><script src=" 'https://canvasjs.com/assets/script/canvasjs.min.js' "></script><script>var ctx = document.getElementById('chartjs-0').getContext('2d');var chart = new Chart(ctx, {type: 'line',data: {labels: [")
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
            url = 'file:/Users/oliver.tattersall/Desktop/Mycoding/Pythonunit/API2.html'
            webbrowser.open(url, new=2)
        except:
            print(value)
            T2 = Text(root, height=3, width=30)
            T2.grid(row=2, column=0,padx=30, pady=25)
            T2.insert(END, "Sorry, this symbol is not in \nthe database, it will be \ndeleted. Please select a new stock")
            deletestock(value)
    except ConnectionError as e:    # This is the correct syntax
        print("Network error")
        T2 = Text(root, height=2, width=30)
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


root=Tk()
root.title("Stocks")
root.geometry("600x600+0+0")
root.config(bg='deep sky blue')

OPTIONS=makeList()
var=StringVar(root)
var.set(OPTIONS[0])
w=OptionMenu(root,var,*OPTIONS, command=main)
w.grid(row=1,column=0, padx=30,pady=25)
T = Text(root, height=2, width=30)
T.grid(row=0, column=0,padx=30, pady=25)
T.insert(END, "Pick a stock to learn more \nabout")





root.mainloop()
            