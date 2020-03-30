import tkinter as tk
import pandas as pd
from pandas import DataFrame
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

from numpy import *


 
# Creating  data frame from csv file
df = pd.read_csv('D:\\Python\\acs2015_county_data.csv')
  
# removing null values 
df.dropna(inplace = True) 
  
# extracting greatest 10 
df1 =df.nlargest(10, "TotalPop")
# extracting smallest 10
dfs =df.nsmallest(10,"TotalPop")

#extracting greatest 10 unemployed counties
dfUnemp = df.nlargest(10,"Unemployment")


#bar graph to show the top 10 counties population using nlargest df
def bycounty():
    
    root1=tk.Tk()
    df2 = DataFrame(df1,columns= ['County','TotalPop'])
    #groupby splits the data into groups based on a criteria
    df2 = df2[['County', 'TotalPop']].groupby('County').sum()
    figure1 = plt.Figure(figsize=(6,6), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root1)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='bar',legend=True,ax=ax1,color="blueviolet")
    
    ax1.set_title('Top 10 population county')
    ax1.set_xlabel("County")
    ax1.set_ylabel("Population (in 100,000)")
    root1.mainloop()

#bar graph to show the top 10 counties population using nsmallest df
 
def bycountys():
    
    root1=tk.Tk()
    df2 = DataFrame(dfs,columns= ['County','TotalPop'])
    df2 = df2[['County', 'TotalPop']].groupby('County').sum()
    figure1 = plt.Figure(figsize=(7,7), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root1)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='bar',legend=True,ax=ax1,color="darkmagenta")
    ax1.set_title('Bottom 10 population county')
    ax1.set_xlabel("County")
    ax1.set_ylabel("Population (in 100,000)")
    root1.mainloop()
    
def bycountymean():
    
    root1=tk.Tk()
    df2 = DataFrame(df1,columns= ['County','Income','TotalPop'])
    df2 = df2[['County', 'Income']].groupby('County').mean()
    figure1 = plt.Figure(figsize=(6,3), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root1)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='bar',legend=True,ax=ax1,color="palevioletred")
    ax1.set_title('Top 10 Mean Income by County')
    ax1.set_xlabel("County ")
    ax1.set_ylabel("Mean Income in $")
    root1.mainloop()
    
# plotting multiple variables
def barchartmv1():
    
    root1=tk.Tk()
    df2 = df1[['County', 'PrivateWork', 'PublicWork','SelfEmployed']].groupby('County').sum()
    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root1)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='bar',legend=True,ax=ax1,colors=["royalblue","plum","mediumorchid"])
    ax1.set_title('Top 10 Population Employment Ratio by County')
    ax1.set_ylabel("Average percentage ")
    ax1.set_xlabel("County ")
    root1.mainloop()

def barchartmv2():
    
    root1=tk.Tk()
    df2 = df1[['County', 'White', 'Black','Native','Asian']].groupby('County').sum()
    print(df2)
    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    xvalues=range(0,10)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root1)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='bar',legend=True,ax=ax1)
    ax1.set_title('Top 10 Population Race Ratios by County ')
    ax1.set_ylabel("Race Ratios in percent")
    ax1.set_xlabel("Counties")
    ax1.set_xticks(xvalues)
    root1.mainloop()

def linechart():
    
    root1=tk.Tk()
    df2 = DataFrame(dfUnemp,columns = ['County','Unemployment'])
    df2 = df2[['County','Unemployment']].groupby("County").sum()
    print(df2)
    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    xvalues=range(0,10)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root1)
    line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
    explanation=" 0.Adjuntas 1.Cataño 2.Corson 3.Jayuya 4.Kusilvak Census Area 5.Lares 6.Oglala Lakota 7.Orocovis 8.San Sebastián 9. Utuado"
    
    ax1.set_title('County UnEmployment Rate:Top 10')
    ax1.set_xlabel("County ")
    ax1.set_xticks(xvalues)
    ax1.set_xticklabels(xvalues)
    ax1.set_ylabel("Unemployment (in percentage) ")
    w = tk.Label(root1,compound = tk.CENTER,text=explanation,wraplength=500, justify=LEFT,font=" arial 15 ").pack(side="bottom")
    w.pack() 
    root1.mainloop()


def lollipopEmp():

    root1=tk.Tk()
    df['EmployedMean'] = df.State.map(df.groupby(['State']).Employed.mean())
    temp = df['EmployedMean'].tolist()
    employedMean  = list( dict.fromkeys(temp)) 
    States = df['State'].tolist()
    States  = list( dict.fromkeys(States))
    xvalues = range(1,53)
    
    
    fig = plt.Figure(figsize =(16,5),dpi = 100)
    ax1 = fig.add_subplot(111)
    ax1.stem(xvalues, employedMean)
    ax1.set_title(' States Vs Employment')
    ax1.set_xlabel('States')
    ax1.set_ylabel('Employed Population ( in 1000s)')
    ax1.set_xticks(xvalues)
    lp = FigureCanvasTkAgg(fig, master=root1)
    lp.draw()
    lp.get_tk_widget().pack()
    
    explanation = "'1.Alabama', '2.Alaska', '3.Arizona', '4.Arkansas', '5.California', '6.Colorado', '7.Connecticut', '8.Delaware', '9.District of Columbia', '10.Florida', '11.Georgia', '12.Hawaii', '13.Idaho', '14.Illinois', '15.Indiana', '16.Iowa', '17.Kansas', '18.Kentucky', '19.Louisiana', '20.Maine', '21.Maryland', '22.Massachusetts', '23.Michigan', '24.Minnesota', '25.Mississippi', '26.Missouri', '27.Montana', '28.Nebraska', '29.Nevada', 30.'New Hampshire', '31.New Jersey', '32.New Mexico', '33.New York', '34.North Carolina', '35.North Dakota', '36.Ohio', '37.Oklahoma', '38.Oregon', '39.Pennsylvania', '40.Rhode Island', '41.South Carolina', '42.South Dakota', '43.Tennessee', '44.Texas', '45.Utah', '46.Vermont', '47.Virginia', '48.Washington', '49.West Virginia', '50.Wisconsin', '51.Wyoming', '52.Puerto Rico'"
    w = tk.Label(root1,compound = tk.CENTER,text=explanation,wraplength=1500, justify=LEFT).pack(side="left")
    w.pack()
    root1.mainloop()
 
def scatterPU():
    root1=tk.Tk()
    
    df['PovertyMean'] = df.State.map(df.groupby(['State']).Poverty.mean())
    df['UnemploymentMean'] = df.State.map(df.groupby(['State']).Unemployment.mean())
    povertyMean = df['PovertyMean'].tolist()
    povertyMean  = list( dict.fromkeys(povertyMean))
    unemployedMean = df['UnemploymentMean'].tolist()
    unemployedMean  = list( dict.fromkeys(unemployedMean))
    fig = Figure(figsize =(16,5),dpi = 100)
    ax1 = fig.add_subplot(111)
    ax1.scatter(unemployedMean,povertyMean,edgecolors='skyblue')
    ax1.set_title('Unemployment Vs Poverty')
    ax1.set_xlabel('Unemployment ( in population % )')
    ax1.set_ylabel('Poverty ( in population % )')
    pu = FigureCanvasTkAgg(fig, master=root1)
    pu.draw()
    pu.get_tk_widget().pack()
    root1.mainloop()
    
def pieRace():
    
    root1=tk.Tk()
    racesMean=[]
    racesMean.append(df.loc[:,"White"].mean())
    racesMean.append(df.loc[:,"Hispanic"].mean())
    racesMean.append(df.loc[:,"Black"].mean())
    racesMean.append(df.loc[:,"Native"].mean())
    racesMean.append(df.loc[:,"Asian"].mean())
    racesMean.append(df.loc[:,"Pacific"].mean())
    races=['White','Hispanic','Black','Native','Asian','Pacific']
    colors=['red','goldenrod','wheat','khaki','salmon','blue']
    explode = (0.1, 0, 0, 0, 0.1, 0.2)
    fig = plt.Figure(figsize =(6,5),dpi = 100)
    ax1 = fig.add_subplot(111)
    ax1.pie(racesMean,labels=races,colors=colors,autopct='%.1f',explode=explode)
    ax1.set_title('Constitution of Races')
    
    pr = FigureCanvasTkAgg(fig, master=root1)
    pr.draw()
    pr.get_tk_widget().pack()
    root1.mainloop()


statesWithPercap={}
statesWithHighprod={}    
def highestPercapitaInc():
    
    root1=tk.Tk()
    from heapq import nlargest
    
    States = df['State'].tolist()
    States  = list( dict.fromkeys(States))
    df['percapIncome'] = df.State.map(df.groupby(['State']).IncomePerCap.mean())
    percapMean = df['percapIncome'].tolist()
    percapMean  = list( dict.fromkeys(percapMean))
    
    for i in range(52):
        statesWithPercap[States[i]]=percapMean[i]
    tenPercap =nlargest(10,statesWithPercap,key=statesWithPercap.get)
    tenPercapMean=[]
    for i in range(10):
        tenPercapMean.append(statesWithPercap[tenPercap[i]])
    
    fig = plt.Figure(figsize =(10,5),dpi = 100)
    ax1 = fig.add_subplot(111)
    ax1.barh(tenPercap,tenPercapMean,height=0.8,align='center',color='yellowgreen')
    ax1.set_title('Top 10 states Vs Percapita Income')
    ax1.set_ylabel('States')
    ax1.set_xlabel("Percapita Income (In $)")
    
    pi = FigureCanvasTkAgg(fig, master=root1)
    pi.draw()
    pi.get_tk_widget().pack()
    root1.mainloop()
    
def highProduction():
    root1=tk.Tk()
    from heapq import nlargest
    
    States = df['State'].tolist()
    States  = list( dict.fromkeys(States))
    df['Production'] = df.State.map(df.groupby(['State']).Production.mean())
    productMean = df['Production'].tolist()
    productMean  = list( dict.fromkeys(productMean))
    
    for i in range(52):
        statesWithHighprod[States[i]]=productMean[i]
    tenHighprod =nlargest(5,statesWithHighprod,key=statesWithHighprod.get)
    tenHighprodMean=[]
    for i in range(5):
        tenHighprodMean.append(statesWithHighprod[tenHighprod[i]])
    
    xvalues=range(1,6)
    fig = plt.Figure(figsize =(10,5),dpi = 100)
    ax1 = fig.add_subplot(111)
    ax1.stem(xvalues,tenHighprodMean)
    

    ax1.set_title('Top 5 States Vs Production ')
    ax1.set_xlabel('States')
    ax1.set_ylabel("Production( In %)")
    ax1.set_xticks(xvalues)
    
    explanation ="1.Indiana 2.Alabama 3.Ohio 4.Tennessee 5.Kentucky"
    w=Label(root1,text=explanation,anchor=CENTER,justify=LEFT,width=200,font=('arial',18))
    w.pack(side='bottom',expand=1)
    
    pro = FigureCanvasTkAgg(fig, master=root1)
    pro.draw()
    pro.get_tk_widget().pack()
    root1.mainloop()
    
def barmv4():   
    
    root1=tk.Tk()
    df2 = df[['State','ChildPoverty','Poverty']].groupby('State').sum()
    df2=df2.nlargest(10,"Poverty")
    #  creating columns and showing as %
    df2['Povertypercent'] = df2['Poverty']/100
    df2['Childpercent'] = df2['ChildPoverty']/100
      
    df2 = DataFrame(df2,columns= ['Povertypercent','Childpercent'])
    figure1 = plt.Figure(figsize=(6,6), dpi=100)
    ax2 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root1)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2.plot(kind='bar',legend=True,ax=ax2)
    ax2.set_title('Top 10 states by poverty %', fontsize='small')
    ax2.set_ylabel("\nPoverty Percentage ")
    root1.mainloop()
    
def citizensDonut():
    root1=tk.Tk()
    citizenMean=df.loc[:,"Citizen"].mean()
    popMean =df.loc[:,"TotalPop"].mean()
    nonCitizenMean = popMean -citizenMean
    
    population=[citizenMean,nonCitizenMean]
    popDivision=['Citizens','Non-Citizens']
    
    
    
    colors=['tomato','lightsalmon']
    
    fig = plt.Figure(figsize =(5,5),dpi = 100)
    ax1 = fig.add_subplot(111)
    ax1.pie(population,labels=popDivision,colors=colors,radius=1.3,autopct='%1.1f%%')
    donutCircle=plt.Circle( (0,0), 0.7, color='white')
    ax1.set_title('Citizens - Non citizens')
    ax1.add_artist(donutCircle)
    
    d = FigureCanvasTkAgg(fig, master=root1)
    d.draw()
    d.get_tk_widget().pack()
    root1.mainloop()
    
def transportDonut():
    root1=tk.Tk()
    listTransport=[]
    listTransport.append(df.loc[:,"Drive"].mean())
    listTransport.append(df.loc[:,"Carpool"].mean())
    listTransport.append(df.loc[:,"Transit"].mean())
    listTransport.append(df.loc[:,"Walk"].mean())
    listTransport.append(df.loc[:,"OtherTransp"].mean())
    Transport = ["Drive","Carpool","Transit","Walk","OtherTransport"]
    colors = ['yellowgreen','goldenrod','coral','violet','darksalmon']
    fig = plt.Figure(figsize =(7,4),dpi = 100)
    ax1 = fig.add_subplot(111)
    ax1.pie(listTransport,labels=Transport,colors=colors,radius=1.3,autopct='%1.1f%%')
    donutCircle=plt.Circle( (0,0), 0.7, color="white")
    ax1.set_title('Transport in the Country:THE USA')
    ax1.add_artist(donutCircle)
    d = FigureCanvasTkAgg(fig, master=root1)
    d.draw()
    d.get_tk_widget().pack()
    root1.mainloop()
    
def pop():
    root1=tk.Tk()
    root1.configure(background='wheat')
    b1 = Button(root1,text="Top 10 Population by County",font="times 15 bold",command=bycounty,anchor=CENTER)
    b2 = Button(root1,text="Bottom 10 Population by County",font="times 15 bold",command=bycountys,anchor=CENTER)
    
    b1.pack()
    b2.pack(side='bottom')
    root1.mainloop()
     
def race():
    root1=tk.Tk()
    root1.configure(background='wheat')
    b1 = Button(root1,text="Citizens Vs Non-citizens",font="times 15 bold",command=citizensDonut,anchor=CENTER)
    b2 = Button(root1,text="Race Ratio by county",font="times 15 bold",command=barchartmv2,anchor=CENTER)
    b3 = Button(root1,text="Race Ration of the entire country",font="times 15 bold",command=pieRace,anchor=CENTER)
    
    b1.pack()
    b2.pack(side='bottom')
    b3.pack(side='bottom')
    root1.mainloop()
    
def emp():
    root1=tk.Tk()
    root1.configure(background='wheat')
    b1 = Button(root1,text="State Vs Employment",font="times 15 bold",command=lollipopEmp,anchor=CENTER)
    b2 = Button(root1,text="Top 5 states by production",font="times 15 bold",command=highProduction,anchor=CENTER)
    b3 = Button(root1,text="Employment Ratio by County",font="times 15 bold",command=barchartmv1,anchor=CENTER)
    b4 = Button(root1,text="Means of Transport",font="times 15 bold",command=transportDonut,anchor=CENTER)
    
    b1.pack()
    b2.pack(side='bottom')
    b3.pack(side='bottom')
    b4.pack(side='bottom')
    root1.mainloop()
    
def inc():
    root1=tk.Tk()
    root1.configure(background='wheat')
    b1 = Button(root1,text="Mean Income by County",font="times 15 bold",command=bycountymean,anchor=CENTER)
    b2 = Button(root1,text="Top 10 states by Percapita Income",font="times 15 bold",command=highestPercapitaInc,anchor=CENTER)
     
    b1.pack()
    b2.pack(side='bottom')
    root1.mainloop()
     
def ecny():
    root1=tk.Tk()
    root1.configure(background='wheat')
    b1 = Button(root1,text="Top 10 States by Poverty",font="times 15 bold",command=barmv4,anchor=CENTER)
    b2 = Button(root1,text="Top 10 Counties by Unemployment",font="times 15 bold",command=linechart,anchor=CENTER)
    b3 = Button(root1,text="Poverty With respect to Unemployment",font="times 15 bold",command=scatterPU,anchor=CENTER)
     
    b1.pack()
    b2.pack(side='bottom')
    b3.pack(side='bottom')
    root1.mainloop()
       
    
     
root = tk.Tk()
root.configure(background='wheat')
root.title('US Census Data Analysis')
l=Label(root,text="United States : Census Data Analysis",bg='wheat',anchor=CENTER,justify=LEFT,font="times 37 bold" )
l.pack()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)


#creating menu list to access some graphs

filemenu.add_command(label="Population ", command=pop)
filemenu.add_command(label="Employment", command=emp)
filemenu.add_command(label="Income ", command=inc)
filemenu.add_command(label="Races ",command=race)
filemenu.add_command(label="Economic declines", command=ecny)



filemenu.add_separator()

menubar.add_cascade(label="Analyses", menu=filemenu)
root.config(menu=menubar)
root.mainloop()