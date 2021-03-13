# Finds the base word for any word with derivational suffixes.
Quick-and-dirty script to find the base word for any word with derivational suffixes. Extremely noisy, handle with care.

## Input files
The script requires three input files. First, a space-separated file with the lemmas in your corpus and their absolute frequency, named `input.txt`. Unfortunately, the file I used to compute my output is too large to be uploaded here.

    volta 1260829
    modo 1209297
    fine 1190979
    punto 1160029
    italia 1150307
    vita 1139233
    persona 1139018
    diritto 1117652
    ...

The second file required is a list of derivational suffixes, one per line, named `morphemes.txt`.

    ata
    one
    uccio

The last file is a clean list of nouns, named `input_cleaner.txt`, in case your `input.txt` is too noisy.

    casa
    italia
    pizza

## The output
The script does its thing and prints out the results into `output.txt`. Two filters in the script ensure that the output only includes nouns with a corpus frequency >10 whose base-noun has a corpus frequency >200.

    mario 112255 mare 251022 -io
    collegio 107802 collega 153361 -io
    serata 107319 sera 241663 -ata
    solito 102505 sole 257950 -ito
    regionale 101876 regione 855258 -ale
    trattato 101212 tratto 123608 -ato
    consigliere 97162 consiglio 957543 -ere
    segnale 95152 segno 175429 -ale
    
Curious about Italian nouns? Check out my input and output data in this repo!
