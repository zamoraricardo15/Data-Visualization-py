# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:25:51 2021

@author: rzamoram
"""


#Tarea 1
#Ricardo Zamora Mennigke
#Visualizacion de Datos


#1) Con base en su experiencia indique posibles aplicaciones de la visualizacion
#PowerBI, Visualizacion de metricas

#2. [20 puntos] Utilizando los datos de la tabla cafe.csv realice lo siguiente:

#a) Lea el archivo y verifique que este se ley´o correctamente usando la funci´on dtypes del
import os
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
%matplotlib inline
plt.ioff()
import numpy as np
import pandas as pd

pasada = os.getcwd()
os.chdir("C:/Users/rzamoram/OneDrive - Intel Corporation/Documents/Machine Learning/Visualizacion de Datos en Python/Semana 1")
print(os.getcwd())
datos = pd.read_csv('cafe.csv',delimiter=',',decimal=".")
print(datos.shape)
print(datos.head())
print(datos.info())
datos.dtypes

#b) Dise~ne el prototipo de un gr´afico que permita compara el comportamiento de la variable


#c) Replique el gr´afico dise~nado en el punto anterior utilizando la libreria matplotlib.
class MyPlot(plt.Axes):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

    def labs(self, title = "", x = "", y = "", title_pad = 10, title_size = 12):
      self.set_title(title, pad = title_pad, fontdict = {'fontsize':title_size})
      self.set_xlabel(x)
      self.set_ylabel(y)
    
    def theme_minimal(self):
      self.spines['top'].set_visible(False)
      self.spines['right'].set_visible(False)
      self.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    def add_points(self, data, x, y, color = None):
      if color is None:
        self.plot(data[x], data[y], 'o', ms = 3)
      else:
        for g in data[color].unique():
          d = data[data[color] == g]
          self.plot(d[x], d[y], 'o', ms = 3, label = g)
          legend = self.legend(handletextpad=0.05)
          lhs = legend.legendHandles
          for lh in lhs:
            lh._legmarker.set_markersize(4)

    def add_bars(self, data, x, y, label = False, fun = "sum", color = "#78c4d4"):
      d = data.groupby(x).agg(fun)
      bars = self.bar(d.index, d[y], color = color, alpha = 1)
      if label :
        for bar in bars:
          height = round(bar.get_height(),2)
          self.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords = "offset points",
                    ha = 'center', va = 'bottom')



fig, axes = plt.subplots(figsize=(10, 5), dpi = 100)
axes.__class__ = MyPlot

axes.labs(title = "Largo del pétalo por especie", 
          x = "Species",
          y = "Largo del Pétalo")
axes.theme_minimal()
axes.add_bars(data = datos, x = "country_of_origin", y = "total_cup_points")

ax.legend()
display(fig)


class MyPlot(plt.Axes):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

    def labs(self, title = "", x = "", y = "", title_pad = 10, title_size = 12):
      self.set_title(title, pad = title_pad, fontdict = {'fontsize':title_size})
      self.set_xlabel(x)
      self.set_ylabel(y)
    
    def theme_minimal(self):
      self.spines['top'].set_visible(False)
      self.spines['right'].set_visible(False)
      self.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    def add_points(self, data, x, y, color = None):
      if color is None:
        self.plot(data[x], data[y], 'o', ms = 3)
      else:
        for g in data[color].unique():
          d = data[data[color] == g]
          self.plot(d[x], d[y], 'o', ms = 3, label = g)
          legend = self.legend(handletextpad=0.05)
          lhs = legend.legendHandles
          for lh in lhs:
            lh._legmarker.set_markersize(4)

    def add_bars(self, data, x, y, label = False, fun = "mean", color = "#78c4d4"):
      d = data.groupby(x).agg(fun)
      bars = self.bar(d.index, d[y], color = color, alpha = 1)
      if label :
        for bar in bars:
          height = round(bar.get_height(),2)
          self.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords = "offset points",
                    ha = 'center', va = 'bottom')



fig, axes = plt.subplots(figsize=(10, 5), dpi = 100)
axes.__class__ = MyPlot

axes.labs(title = "Largo del pétalo por especie", 
          x = "Species",
          y = "Largo del Pétalo")
axes.theme_minimal()
axes.add_bars(data = datos, x = "country_of_origin", y = "total_cup_points")

ax.legend()
display(fig)

#d) Repita el punto anterior esta vez utilizando la libreria seanborn
fig, ax = plt.subplots(figsize=(10, 5), dpi = 100)
def theme_minimal(ax):
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

sb.barplot(x="country_of_origin", y="total_cup_points", data=datos, ax = ax)

ax.legend()
display(fig)



#3) Usando como referencia el gr´afico mostrado a continuaci´on identifique los componentes del gr´afico


#4) Utilizando la libreria libreria seanborn y los datos de la tabla

#a) Dise˜ne un gr´afico que permite visualizar la cantidad de pel´ıculas estrenadas en cada a˜no
pasada = os.getcwd()
os.chdir("C:/Users/rzamoram/OneDrive - Intel Corporation/Documents/Machine Learning/Visualizacion de Datos en Python/Semana 1")
print(os.getcwd())
datos = pd.read_csv('peliculas.csv',delimiter=',',decimal=".")
print(datos.shape)
print(datos.head())
print(datos.info())
datos.dtypes

datos['fecha_lanzamiento'] = pd.to_datetime(datos['fecha_lanzamiento'])
datos['year'], datos['month'] = datos['fecha_lanzamiento'].dt.year, datos['fecha_lanzamiento'].dt.month
datos


fig, ax = plt.subplots(figsize=(5, 4), dpi = 200)
def theme_minimal(ax):
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

sb.lineplot(x = "year", y = "n", data = datos)
ax.set_title("Pasajeros que viajan al año")
ax.set_ylabel("Cantidad de pasajeros")
ax.set_xlabel("Año")
theme_minimal(ax)

ax.legend()
display(fig)



#b) Dise˜ne un gr´afico que permita comparar en forma relativa la cantidad de pel´ıculas que 

#san_jose = delitos[delitos.Provincia == "San Jose"]
san_jose = datos.set_index('fecha_lanzamiento')
delitos_mes_canton = san_jose.groupby([pd.Grouper(freq='M'),"genero"]).sum()["n"]
delitos_mes_canton.head(20)

cantones = delitos_mes_canton.index.get_level_values(1).unique()
print(cantones)



import matplotlib.dates as mdates

# Lienzo
fig, ax = plt.subplots(figsize=(6, 3), dpi = 300)
ax.__class__ = MyPlot

ax.labs(title = "Cantidad de Peliculas por Genero y por year", 
        title_pad = 25,
        y = "Cantidad")
ax.theme_minimal()


# Dibujar las lineas
for genero in cantones:
  df = delitos_mes_canton[delitos_mes_canton.index.get_level_values(1) == genero]
  x = df.index.get_level_values(0)
  y = df
  if genero == "Action":
    color = "#046582"
    alpha = 0.5
  elif genero == "Comedy":
    color = "#667474"
    alpha = 0.5
  elif genero == "Drama":
    color = "#742b74"
    alpha = 0.5
  elif genero == "Horror":
    color = "#74741c"
    alpha = 0.5
  elif genero == "Romance":
    color = "#74391c"
    alpha = 0.5
  elif genero == "Thriller":
    color = "#1c0474"
    alpha = 0.5
  elif genero == "Western":
    color = "#04ffff"
    alpha = 0.5
  else:
    color = "#6e7c7c"
    alpha = 0.5
  plt.plot(x,y, color = color, alpha = alpha)



ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y')) # formato de los cortes principales
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%b")) # formato de los cortes secundarios
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3)) # intervalo de los cortes secundarios
ax.tick_params(axis='x', which='minor', labelsize=4, length = 1, pad = 0, labelcolor = "#686d76") # formato texto cortes secundarios

# Anotacinones
fig.text(0.2,0.9,"Genero:", color = "#6e7c7c", weight="bold")
fig.text(0.2,0.86,"Action  ", color = "#046582", weight="bold")
fig.text(0.2,0.82,"Comedy ", color = "#667474", weight="bold")
fig.text(0.2,0.78,"Drama  ", color = "#742b74", weight="bold")
fig.text(0.2,0.74,"Horror ", color = "#74741c", weight="bold")
fig.text(0.2,0.7,"Romance ", color = "#74391c", weight="bold")
fig.text(0.2,0.66,"Thriller  ", color = "#1c0474", weight="bold")
fig.text(0.2,0.62,"Western ", color = "#04ffff", weight="bold")        
         
import seaborn as sb


def theme_minimal(ax):
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)


theme_minimal(ax)

ax.legend()
display(fig)

#c) Dise˜ne una paleta de color para el gr´afico y justifique la selecci´on de colores.

fig, ax = plt.subplots(figsize=(7, 5), dpi = 200)

def theme_minimal(ax):
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.grid(color='grey', linestyle='-', linewidth=0.55, alpha=0.5)
  ax.set_title('Cantidad de Peliculas por Genero y por year')
  ax.set_xlabel('year')
  ax.set_ylabel('Cantidad de Peliculas')
 

paleta = {
  "Action": "#046582",
  "Comedy": "#667474",
  "Horror": "#74741c",
  "Drama": "#742b74",
  "Romance": "#74391c",
  "Thriller": "#1c0474",
  "Western": "#04ffff"}

for genero in cantones:
  df = delitos_mes_canton[delitos_mes_canton.index.get_level_values(1) == genero]
  x = df.index.get_level_values(0)
  y = df

sb.lineplot(x = "year", y = "n",data = datos,ax=ax,hue="genero",
             style="genero", markers=True, dashes=False,palette=paleta)
sb.lineplot(x = "year", y = "n",data = datos,ax=ax)
theme_minimal(ax)
ax.legend()
display(fig)


##5) Utilizando la tabla temperaturasUSA.csv realice los siguiente:
#a) Lea los datos y verifique que se ley´o de forma correcta
pasada = os.getcwd()
os.chdir("C:/Users/rzamoram/OneDrive - Intel Corporation/Documents/Machine Learning/Visualizacion de Datos en Python/Semana 1")
print(os.getcwd())
datos = pd.read_csv('temperaturasUSA.csv',delimiter=',',decimal=".")
print(datos.shape)
print(datos.head())
print(datos.info())
datos.dtypes

#b)b) Dise˜ne utilizando l´apiz y papel un gr´afico que permita comparar el comportamiento de la

#c) c) Replique el gr´afico del punto anterior utilizando el paquete seanborn
#san_jose = datos.set_index('month')
#delitos_mes_canton = san_jose.groupby([pd.Grouper(freq='M'),"location"]).mean()["mean"]
#delitos_mes_canton.head(20)
#
#cantones = delitos_mes_canton.index.get_level_values(1).unique()
#print(cantones)


import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(7, 5), dpi = 200)


def theme_minimal(ax):
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.grid(color='grey', linestyle='-', linewidth=0.55, alpha=0.5)
  ax.set_title('Temperatura por lugar y mes')
  ax.set_xlabel('mes')
  ax.set_ylabel('Temperatura')
 

paleta = {
  "Chicago": "#046582",
  "San Diego": "#74391c",
  "Houston": "#1c0474",
  "Death Valley": "#04ffff"}

#for genero in cantones:
#  df = delitos_mes_canton[delitos_mes_canton.index.get_level_values(1) == location]
#  x = df.index.get_level_values(0)
###  y = df
#day_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#plt.xticks(x="month", day_order)
  
str_month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
ax.set_xticks(range(0,12))
ax.set_xticklabels(str_month_list)

sb.lineplot(x = "month", y = "mean",data = datos,ax=ax,hue="location",
             style="location", markers=True, dashes=False,palette=paleta)
sb.lineplot(x = "month", y = "mean",data = datos,ax=ax)
theme_minimal(ax)


ax.legend()
display(fig)