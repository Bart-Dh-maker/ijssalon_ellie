from helper import decoreer

def print_aanbieding():

    prijzen={
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }
    print(prijzen)

    aanbieding =prijzen["aardbei"]*0.8
    print(aanbieding)


    reclame_tekst=f"Vandaag in de aanbieding : vanille-ijs, 1 liter - slechts €{aanbieding}"

    print(reclame_tekst)


    reclame_tekst2=reclame_tekst[:63]
    print(reclame_tekst2)


    reclame_tekst3=reclame_tekst2.upper()
    print(reclame_tekst3)


    reclame_tekst4=reclame_tekst3.split()
    print(reclame_tekst4)

    for el in reclame_tekst4:
        print(el) 

    for el in reclame_tekst4:
        print(el.lower())
        
    for el in reclame_tekst4:
        if len(el)>=5:
            print(el.upper())
        if len(el)<=4:
            print(el.lower())

decoreer("aanbieding")
print_aanbieding()




            
            
            











                    