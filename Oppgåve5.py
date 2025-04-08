import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    return np.sin(np.pi * x)  # Initialbetingelse u(x,0) = sin(pi*x)

def solve_heat_equation():
    h = 10 # Romlig steg
    k = 1 # Tids steg
    Nt = 200 # Antall tidssteg
    Nx = 50 # antall x verdier
    L = 1
    
    x = np.linspace(0, L, Nx+1)
    u = np.zeros((Nx+1, Nt+1))
    u[:, 0] = f(x)  # Initialbetingelse
    
    # Implisitt Euler
    for j in range(0, Nt):
        for i in range(1, Nx):
            u[i, j+1] = (u[i+1, j+1]*k + u[i, j]*h**2 + u[i-1, j+1]*k)/(h**2+2*k)
    
    return x, u, Nt, k

def animate_solution():
    x, u, Nt, k = solve_heat_equation()
    fig, ax = plt.subplots()
    line, = ax.plot(x, u[:, 0], 'r-')
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    title = ax.set_title("Varmeligningen med implisitt Euler (t = 0.000s)")
    
    def update(frame):
        line.set_ydata(u[:, frame])
        time_value = frame
        title.set_text(f"Varmeligningen med implisitt skjema (t = {time_value:.3f}s)")
        return line, title

    ani = animation.FuncAnimation(fig, update, frames=Nt, interval=50, blit=False)
    plt.show()

animate_solution()

# Å sette h veldig stor så står modellen nesten heilt i ro
# Å sette k veldig stor så kolapser den med ein gang, og blir om til ein bein strek
# Eg satt dei og lik kvarandre, og då gjekk modellen ganske raskt nedover og blei om til ein strek