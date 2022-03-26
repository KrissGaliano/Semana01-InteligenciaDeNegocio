import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

print('------------ARCHIVOS PANAMERICANOS-----------------')
archivo=pd.read_csv('Panamericanos_Lima.csv')
print(archivo)
def calculo_suma():
    print('la suma es: ',archivo['Oro'].sum())
    print('la suma es: ',archivo.Oro.sum())

def calculo_conteo():
    print('el conteo es: ',len(archivo['Oro']))
    print('el conteo es: ',len(archivo.Oro))
    print('el conteo es: ',archivo['Oro'].count())
    print('el conteo es: ',archivo.Oro.count())

def calculo_media():
    print('la media es: ',archivo.Oro.sum()/archivo.Oro.count())
    print('la media es: ',archivo.Oro.mean())

def calculo_media2(redondeo=2):
    media=archivo.Oro.mean()
    media=round(media,redondeo)
    return media

def calculo_mediana():
    numero=np.size(archivo.Oro)
    posicion=round(numero/2)
    print('Posicion mediana: ',posicion)
    mediana=archivo.Oro[posicion-1]
    return mediana

def calculo_moda():
    moda=archivo.Oro.mode()
    return moda

def percentil():
    percentil=archivo.Oro
    print("Min: ",np.quantile(percentil,0))
    print("Q1: " ,np.quantile(percentil,0.25))
    print("Q2: " ,np.quantile(percentil, 0.50))
    print("Q3: " ,np.quantile(percentil, 0.75))
    print("QMax: " ,np.quantile(percentil, 1))

    print("Varianza: " ,np.average(percentil))

def varianza():
    plt.style.use('seaborn')
    varianza = archivo.Oro

    mean = np.mean(varianza)
    std = np.std(varianza)
    y = scipy.stats.norm.pdf(varianza,mean,std)
    plt.plot(varianza,y)

    plt.title('Distribución acumulada')

    plt.xlabel('Altura en cm')
    plt.ylabel('Probabilidad')
    plt.show()


calculo_suma()
calculo_conteo()
calculo_media()
print('la media redondeado es: ',calculo_media2())
print('La mediana es: ',calculo_mediana())
print('la moda es: ',calculo_moda())
percentil()
varianza()