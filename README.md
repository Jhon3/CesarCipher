# Cesar Cipher

  
A simple program to parse ciphertext with a cesar cipher and decode it.

## Execute

To execute the program run the code:
>python3 cryptanalysisCesar.py alfa.txt cifra.txt


Note that you have passed the alphabet used and the ciphertext, the program will try all possibilities and will save the results in the "results" folder, there you will be able to analyze the texts resulting from the attempts. After analysis you will confirm that key 33 (text 33) has been used.

## Modes
The program has two modules, the first is the normal one, where at the end of the execution the user will need to check in the worst case all the output files. The second mode is master, in which the program makes use of *langdetect*, a lib that uses natural language processing. With it, all the result files are analyzed and at the end the program indicates the possible keys to break the cipher.
To install the *langdetect* just run:
> pip3 install langdetect
