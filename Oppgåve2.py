import numpy as np

x = 1.5
f = np.exp(x)


for i in range(1,20):
    h = 1*10**(-i)
    f_est = ((np.exp(x+h)-np.exp(x-h))/(2*h))
    print(f_est, i)

# Her ser vi at ved 15 desiamler blir det feil, altså dataen klarer ikkje å rekne meir nøyaktig, og den blir feil.
# Her i dette tilfellet blir det til plutseleg 0, fordi vi 0 over brøkstreken.
# I taylor rekken så er det den første verdien som er den ekta veriden vi vil ha, men vi har mange ledd bak denne.
# Men jo mindre h er jo mindre bli denne feilen
# Men i denne oppgåva så blir feilen/dei andre ledda mykje mindre enn i oppgåve 1.
# Altså feilen er ledda etter f'(x): ((h**2)/6)*f'''(x) + O(h**4), utrekning for denne er i pdf
# Og då ser vi at feilen er proposjonal med h**2