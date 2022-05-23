import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
xlab = 'Tempo em relação a Segunda ás 10h (h)'
ylab = 'Temperatura Prevista ($\mathrm{^o}$C)'
fsize, lsize = 22, 16
horas = np.linspace(0, 3*8, 8)
tempo = ['Seg 10h', 'Seg 13h', 'Seg 16h', 'Seg 19h', 'Seg 22h', 'Ter 1h', 'Ter 4h', 'Ter 7h']
temp = np.array([18, 23, 23, 20, 17, 14, 13, 13])
ax.plot(horas, temp, marker = 'o', ms = 10, color = 'blue')
ax.set_xlabel(xlab, fontsize = fsize)
ax.set_ylabel(ylab, fontsize = fsize)
ax.tick_params(labelsize = lsize, width = 2)
ax.tick_params(axis = 'x', labelrotation = 30)
ax.grid(ls = '--')
plt.show()
