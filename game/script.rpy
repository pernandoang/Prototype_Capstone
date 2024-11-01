

label start:
    show screen black_screen
    with dissolve
    pause 1.0
    hide screen black_screen
    with dissolve
    jump prolog_pertama


label prolog_pertama:
    scene envi_mom:
        xsize 1920
        ysize 1080
    show larasati_ll at left:
        xsize 600
        ysize 750
        yalign 0.5
    larasati "[text_prolog_larasati[0]]"
