## Given an ordered list of arrivals to the party and a name, return whether the guest with that name was fashionably late.
## Fashionably late: llegar luego de la mitad de los miembros (sin llegar el último)
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
def tarde(list, name):
    if (list.index(name) > len(list)/2) and (list.index(name) != len(list)-1):
        print("el invitado ", name, "está Fashionably late")
    else: print("el invitado ", name, "no esta Fashionably late")
tarde(party_attendees, 'Adela') ## Adela fue la primera y no llego atrde
tarde(party_attendees, 'Mona') ## Mona llegó Fashionably late
tarde(party_attendees, 'Ford') ## Ford llegó de ultimo