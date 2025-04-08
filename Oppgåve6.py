import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parametere
L = np.pi  # Lengde på domenet
T = 2.0    # Total tid
Nx = 50    # Antall romlige punkter
Nt = 200   # Antall tidsstegø

h = 1 # L / (Nx - 1)  # Romlig steglengde
k = 0.5# T / Nt        # Tidssteg
r = k / (2 * h**2)  # Crank-Nicolson parameter

# Diskret x-akse
x = np.linspace(0, L, Nx)

# Initialbetingelse
u = np.sin(x)

# Matrisene A og B for Crank-Nicolson
A = np.diag((1 + 2 * r) * np.ones(Nx)) + np.diag(-r * np.ones(Nx - 1), 1) + np.diag(-r * np.ones(Nx - 1), -1)
B = np.diag((1 - 2 * r) * np.ones(Nx)) + np.diag(r * np.ones(Nx - 1), 1) + np.diag(r * np.ones(Nx - 1), -1)

# Håndter randbetingelser (Dirichlet: u(0,t) = u(L,t) = 0)
A[0, :] = A[-1, :] = 0
A[0, 0] = A[-1, -1] = 1
B[0, :] = B[-1, :] = 0
B[0, 0] = B[-1, -1] = 1

# Lagring av løsninger over tid
U = [u.copy()]

# Løser systemet iterativt
for _ in range(Nt):
    b = B @ u  # Høyreside av ligningen
    b[0] = b[-1] = 0  # Sikrer randbetingelser
    u = np.linalg.solve(A, b)  # Løser det lineære systemet
    U.append(u.copy())

# Opprett animasjon
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)
line, = ax.plot([], [], 'b-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x, U[frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=Nt, init_func=init, blit=True, interval=50)
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.title("Crank-Nicolson-metoden for varmeledning")
plt.show()

# Viss vi samanliknar alle dei tre metodane med samme k og h verdi, eg brukte h = 1 og k = 0.5 i mitt tilfelle, så er 
# Crank-Nicolson og eksplisitt Euler ganske like, mens den implisitte modellen bare kolapser og blir ein flat strekk med ein gang.
# Mens dei to andre går nedover sakte.
