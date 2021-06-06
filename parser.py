import string

#Input
input_sentence = input("Masukan kalimat yang ingin anda cek :")
tokens = input_sentence.lower().split()
tokens.append('EOS')

#Symbols Defination
non_terminals = ['S', 'NN', 'VB']
terminals = ['mak', 'abah', 'televisi', 'sungi', 'bakso', 'telok', 'mamang', 'meli', 'majo', 'nyingok', 'ngenjuk']

#Parse Table Definition
parse_table = {}

parse_table[('S', 'mak')] = ['NN', 'VB', 'NN']
parse_table[('S', 'abah')] = ['NN', 'VB', 'NN']
parse_table[('S', 'televisi')] = ['NN', 'VB', 'NN']
parse_table[('S', 'sungi')] = ['NN', 'VB', 'NN']
parse_table[('S', 'bakso')] = ['NN', 'VB', 'NN']
parse_table[('S', 'telok')] = ['NN', 'VB', 'NN']
parse_table[('S', 'mamang')] = ['NN', 'VB', 'NN']
parse_table[('S', 'nyingok')] = ['error']
parse_table[('S', 'meli')] = ['error']
parse_table[('S', 'majo')] = ['error']
parse_table[('S', 'ngenjuk')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'mak')] = ['mak']
parse_table[('NN', 'abah')] = ['abah']
parse_table[('NN', 'televisi')] = ['televisi']
parse_table[('NN', 'sungi')] = ['sungi']
parse_table[('NN', 'bakso')] = ['bakso']
parse_table[('NN', 'telok')] = ['telok']
parse_table[('NN', 'mamang')] = ['mamang']
parse_table[('NN', 'nyingok')] = ['error']
parse_table[('NN', 'meli')] = ['error']
parse_table[('NN', 'majo')] = ['error']
parse_table[('NN', 'ngenjuk')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'mak')] = ['error']
parse_table[('VB', 'abah')] = ['error']
parse_table[('VB', 'televisi')] = ['error']
parse_table[('VB', 'sungi')] = ['error']
parse_table[('VB', 'bakso')] = ['error']
parse_table[('VB', 'telok')] = ['error']
parse_table[('VB', 'mamang')] = ['error']
parse_table[('VB', 'nyingok')] = ['nyingok']
parse_table[('VB', 'meli')] = ['meli']
parse_table[('VB', 'majo')] = ['majo']
parse_table[('VB', 'ngenjuk')] = ['ngenjuk']
parse_table[('VB', 'EOS')] = ['error']

#Stack Initialitation
stack = []
stack.append('#')
stack.append('S')

#Input Reading Intialitation
idx_tekon = 0
symbol = tokens[idx_tekon]

#Parsing Process
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('Top = ', top)
    print('Symbol = ', symbol)
    if top in terminals:
        print('Top adalah simbol terminals')
        if top == symbol:
            stack.pop()
            idx_tekon = idx_tekon + 1
            symbol = tokens[idx_tekon]
            if symbol == 'EOS':
                print('Isi stack : ', stack)
                stack.pop()
        else:
            print('error')
            break;
    elif top in non_terminals:
        print('Top adalah simbol non_terminals')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbol_pushed = parse_table[(top, symbol)]
            for i in range(len(symbol_pushed)-1,-1,-1):
                stack.append(symbol_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('Isi Stack : ', stack)
    print()

#Kesimpulan
print()
if symbol == 'EOS' and len(stack) == 0:
    print('Input String ', input_sentence, ' Accepted, Sesuai Grammar')
else:
    print('ERROR, Input String ', input_sentence, 'Rejected, Tidak Sesuai Grammar')