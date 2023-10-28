import triangleManager
import matplotlib.pyplot as plt
import numpy as np

x = triangleManager.Triangle(6,6)

x_donusturulmus = []
y_donusturulmus = []


# 0 derece üçgen
plt.plot(x.x_arr, x.y_arr,'-')
plt.plot(x.x_arr,x.y_arr,'o')
plt.plot(x.gx,x.gy,'D')

plt.text(x.gx+0.1,x.gy+0.1,"Gx, Gy")


# döndürülen üçgen

aci = 72
radyan = np.deg2rad(aci)

donus_matrisi = np.array([[np.cos(radyan), -np.sin(radyan)],
                          [np.sin(radyan), np.cos(radyan)]])


for xi, yi in zip(x.x_arr, x.y_arr):
    vector = np.array([xi - x.gx, yi - x.gy])
    donus_vektoru = np.dot(donus_matrisi, vector)
    x_donusturulmus.append(donus_vektoru[0] + x.gx)
    y_donusturulmus.append(donus_vektoru[1] + x.gy)


plt.plot(x_donusturulmus, y_donusturulmus, color='red')
plt.plot(x_donusturulmus, y_donusturulmus,'o', color='grey')


plt.grid()
plt.show()

