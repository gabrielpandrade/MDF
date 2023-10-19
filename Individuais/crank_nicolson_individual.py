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
A = np.zeros((nx - 2, nx - 2))
B = np.zeros((nx - 2, nx - 2))
c = np.zeros((nt - 1, nx - 2))

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

np.fill_diagonal(A, 2 + 2 * sigma)
for i in range(nx - 2):
    for j in range(nx - 2):
        if i == j+1:
            A[i][j] = -sigma
        if i == j-1:
            A[i][j] = -sigma

np.fill_diagonal(B, 2 - 2 * sigma)
for i in range(nx - 2):
    for j in range(nx - 2):
        if i == j+1:
            B[i][j] = sigma
        if i == j-1:
            B[i][j] = sigma

for i in range(nt - 1):
    c[i][0] = sigma * fx[i]
    c[i][-1] = sigma * gx[i]

for i in range(1, nt):
    u[i][0] = fx[i-1]
    u[i][-1] = gx[i-1]
    u[i][1:-1] = np.linalg.solve(A, np.dot(B, u[i-1][1:-1]) + c[i-1])

iplots = 6
plt.title("Evolução do Método de Crank-Nicolson")
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
ax.set_title("Método de Crank-Nicolson")
plt.show()