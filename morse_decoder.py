def decodeMorse(morse_code):
    MORSE_CODE = {'.-.-.-':'.','-.-.--':'!','...---...': 'SOS', '': ' ','..-.': 'F', '-..-': 'X',
                     '.--.': 'P', '-': 'T', '..---': '2',
                     '....-': '4', '-----': '0', '--...': '7',
                     '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                     '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                     '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                     '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                     '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                     '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

    #if there are spaces in the code, need to remove them to detect the words
    if morse_code.find(' ') != -1:
        words = morse_code.split(' ')
        morse_code = ''
        index=0
        for word in words:
            if word == '':#there is a space here
                if index != 0 and index != (len(words)-1):#don't count spaces at very beggining or very end
                    morse_code += MORSE_CODE[word]
            else:#there is not a space
                morse_code += MORSE_CODE[word]
            index+=1
    else:# if there are not spaces in the morse code
        words = morse_code
        morse_code = MORSE_CODE[words]
        return morse_code

    #now must check number of spaces between the words
    if morse_code.count('  ') >=1:#if there are multiple spaces between any words
        index = 0
        next_char=''
        extra_space=0
        modified_morse = ''
        for char in morse_code:
            if (index+1)!= len(morse_code):#need to check the proceeding character
                next_char = morse_code[index+1]
            if char ==' ' and next_char !=' ':#if it is only one space, keep it
                modified_morse+= char
            elif char!=' ':#if it is not a space, keep it
                modified_morse += char
            index+=1

        index = 0
        morse_code=''
        for char in modified_morse:#this for loop ensures there are no spaces remaining at beggining or end
            if char != ' ':
                morse_code = modified_morse[index::]
                for char2 in morse_code:
                    if char2 == ' ' and index == (len(morse_code) - 1):
                        morse_code = morse_code[:index]
                        return morse_code
                return morse_code
            index += 1

    index = 0
    #this for loop ensures there are no spaces remaining at beggining or end
    for char in morse_code:
        if char!=' ':
            morse_code = morse_code[index::]
            for char2 in morse_code:
                if char2 == ' ' and index == (len(morse_code)-1):
                    morse_code = morse_code[:index]
                    return morse_code
            return morse_code
        index+=1

if __name__ == "__main__":
    print(decodeMorse('  .  '))
    print(decodeMorse('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))
    print(decodeMorse('.... . -.--   .--- ..- -.. .'))
    print(decodeMorse('   .  . '))
    print(decodeMorse('...   ---  ...'))
    print(decodeMorse(' . '))
    print(decodeMorse('.-')) #a
    print(decodeMorse('.')) #e
    print(decodeMorse('..')) #I
    print(decodeMorse('...---...')) #SOS

# hey jude: '.... . -.--   .--- ..- -.. .'
# E: ' . '
# ['...  ---  ...'] Got 'S  O S', expected 'S O S'
#['   .  . '] Got '  E E', expected 'E E'
# '...   ---  ...'Got 'S  O S', expected 'S O S'
# ('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
# 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'