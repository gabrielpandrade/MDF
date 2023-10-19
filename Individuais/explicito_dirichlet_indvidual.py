import matplotlib.pyplot as plt
import numpy as np

L0 = 0
Ln = 3
T = 1
nx = 100
nt = 2200
a = 1
L = Ln - L0
fx = np.zeros(nt - 1)
gx = np.zeros(nt - 1)
dx = L / (nx - 1)
dt = T / (nt - 1)
sigma = a * dt / (dx ** 2)
x = np.linspace(L0, Ln, nx)
t = np.linspace(0, T, nt)
u = np.zeros((nt, nx))

escalar = 1
media = 1.5
desvio_padrao = 0.3
i = 0
for p in x:
    u[0][i] = escalar * ((2 / (np.sqrt(2 * np.pi * (desvio_padrao ** 2)))) *
                         np.exp((-1 * (p - media) ** 2) / (2 * (desvio_padrao ** 2))))
    i = i + 1

fx = np.zeros(nt - 1)
gx = np.zeros(nt - 1)

for i in range(nt - 1):
    u[i + 1][0] = fx[i]
    u[i + 1][-1] = gx[i]
    for j in range(nx - 1):
        u[i + 1][j] = u[i][j] + sigma * (u[i][j - 1] - 2 * u[i][j] + u[i][j + 1])

iplots = 6
plt.title("Evolução do Método Explícito")
plt.xlabel("posição")
plt.xlabel("calor")
plots = int(nt / iplots)
for n in range(nt):
    if n % plots == 0:
        plt.plot(x, u[n], label="{:.1f}".format(t[n]))
plt.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, T = np.meshgrid(x, t)
surf = ax.plot_surface(X, T, u, cmap='hot')
fig.colorbar(surf)
ax.set_xlabel("posição")
ax.set_ylabel("tempo")
ax.set_zlabel("calor")
ax.set_title("Método Explícito")
plt.show()
