##Given a list of teams, where each team is a list of names, return the 2nd player (captain) from the last listed team
equipos = [
        ["Juan", "Marcos", "Luis"],
        ["Miguel", "Ana", "Carlos"],
        ["Pedro", "Sofia", "Diego"]
    ]
def selec(eq):
    if not equipos or len(equipos[-1]) < 2:
        return None
    return equipos[-1][1]
print(selec(equipos))
