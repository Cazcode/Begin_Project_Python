import matplotlib.pyplot as plt

months = ['Julio', 'Agosto', 'Septiembre', 'Octubre']
sells = [855, 942, 975, 1053]
x_points = range(len(sells))

fig = plt.figure('Ventas')
ax = fig.gca()

ax.plot(x_points, sells)

ax.set_xticks(x_points)

ax.set_xticklabels(months)

ax.set_ylim([min(sells)-100, max(sells)+100])

plt.grid()

plt.show()