from ai import AI

airep = AI()

command = ""
while True:
    command = airep.listen()
    print(command)
