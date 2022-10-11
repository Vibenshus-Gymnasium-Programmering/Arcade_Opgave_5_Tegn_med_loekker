import arcade

def optegn_felter():
    """ Denne funktion tegner de 8 felter op, som I skal udfylde. """
    # Tegner de nederste 4 felter 
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Tegner de øverste 4 felter
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def tegn_felt_1():
    for raekke in range(30):
        for soejle in range(30):
            x = 0  # I stedet for nul, beregn den korrekt x-lokation ud fra soejle
            y = 0  # I stedet for nul, beregn den korrekt y-lokation ud fra raekke
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def tegn_felt_2():
    # Udskift "pass" med jeres egen kode til for-loopet.
    # Brug modulusoperatoren "%" sammen med et if-statement til at vaelge farven.
    # Undlad at loope fra 30 til 60 for at flytte det hele over. I skal bare laegge 300 til x.
    pass


def tegn_felt_3():
    # Brug modulusoperatoren (%) og et if (måske if/else) statement til at vælge farve med
    # Undlad at bruge flere if-statements.
    pass


def tegn_felt_4():
    # Brug modulusoperatoren og kun et if-statement til at vælge farven.
    pass


def tegn_felt_5():
    # Brug IKKE if-statements til felt 5-8. Ændrer i stedet i løkkerne. 
    pass


def tegn_felt_6():
    pass


def tegn_felt_7():
    pass


def tegn_felt_8():
    pass


def main():
    # Danner et vindue
    arcade.open_window(1200, 600, "Opgave 5 - Tegn med løkker")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Tegner omridset af felterne
    optegn_felter()

    # Tegn felterne
    tegn_felt_1()
    tegn_felt_2()
    tegn_felt_3()
    tegn_felt_4()
    tegn_felt_5()
    tegn_felt_6()
    tegn_felt_7()
    tegn_felt_8()

    arcade.finish_render()

    arcade.run()


main()

