def print_aanbieding():
# vraag 1.2

    prijzen={
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }
    print(prijzen)

    # vraag 1.3

    aanbieding =prijzen["aardbei"]*0.8
    print(aanbieding)

    # vraag 1.4

    reclame_tekst=f"Vandaag in de aanbieding : vanille-ijs, 1 liter - slechts €{aanbieding}"

    print(reclame_tekst)

    # vraag 1.5

    reclame_tekst2=reclame_tekst[:63]
    print(reclame_tekst2)

    # vraag 1.6

    reclame_tekst3=reclame_tekst2.upper()
    print(reclame_tekst3)

    # vraag 1.7

    reclame_tekst4=reclame_tekst3.split()
    print(reclame_tekst4)

    # vraag 1.8

    for el in reclame_tekst4:
        print(el)

    # vraag 1.9 

    for el in reclame_tekst4:
        print(el.lower())

    # vraag 1.10
        
    for el in reclame_tekst4:
        if len(el)>=5:
            print(el.upper())
        if len(el)<=4:
            print(el.lower())

print_aanbieding()


            
            
            











                    