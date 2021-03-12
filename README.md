# Finds the base word for any word with derivational suffixes.
Quick-and-dirty script to find the base word for any word with derivational suffixes. Extremely noisy, handle with care.

## Input files
The script requires a comma-separated file with the lemmas in your corpus and their absolute frequency, named `input.txt`.

    volta,1260829
    modo,1209297
    fine,1190979
    punto,1160029
    italia,1150307
    vita,1139233
    persona,1139018
    diritto,1117652
    ...

The only other file required is a list of derivational suffixes, one per line, named `morphemes.txt`.

    ata
    one
    uccio

## The output
The script does its thing and prints out the results into `output.txt`.

    mario 112255 mare 251022 -io
    collegio 107802 collega 153361 -io
    serata 107319 sera 241663 -ata
    solito 102505 sole 257950 -ito
    terrorismo 102395 terrore  0 -ismo
    regionale 101876 regione 855258 -ale
    trattato 101212 tratto 123608 -ato
    consigliere 97162 consiglio 957543 -ere
    segnale 95152 segno 175429 -ale
    
Curious about Italian nouns? Check out my input and output data in this repo!
