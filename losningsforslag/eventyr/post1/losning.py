from deps.post1 import walkForward, turnLeft, turnRight, validate

turnLeft()
for i in range(5):
    walkForward()
turnLeft()
walkForward()

validate() # Vurderer om koden din er riktig eller ikke. ALLTID kall denne funksjonen på slutten av scripte ditt!
