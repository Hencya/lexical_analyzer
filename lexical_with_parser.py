import string

# input 
input_sentence = input("Masukan kalimat yang ingin anda cek :")
string_check = input_sentence.lower() + "#"
tokens = input_sentence.lower().split()
tokens.append('EOS')

# Lexical analyzer
# initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 
              'q6','q7', 'q8', 'q9', 'q10','q11','q12',
              'q13', 'q14', 'q15', 'q16', 'q17', 'q18',
              'q19', 'q20', 'q21', 'q22', 'q23', 'q24',
              'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
              'q31', 'q32', 'q33', 'q34', 'q35', 'q36',
              'q37', 'q38', 'q39', 'q40', 'q41', 'q42',
              'q43', 'q44', 'q45', 'q46', 'q47', 'q48',
              'q49', 'q50'
              ]

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state,alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

# space before input string
transition_table['q0',' '] = 'q0'

# transition for new token

transition_table[('q50', 'm')] = 'q1'
transition_table[('q50', 'a')] = 'q13'
transition_table[('q50', 'n')] = 'q17'
transition_table[('q50', 't')] = 'q30'
transition_table[('q50', 's')] = 'q40'
transition_table[('q50', 'b')] = 'q45'

# update the transition table for the following token: mak
transition_table[('q0', 'm')] = 'q1'
transition_table[('q1', 'a')] = 'q2'
transition_table[('q2', 'k')] = 'q3'
transition_table[('q3', ' ')] = 'q50'
transition_table[('q3', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'

# update the transition table for the following token: majo
transition_table[('q0', 'm')] = 'q1'
transition_table[('q1', 'a')] = 'q2'
transition_table[('q2', 'j')] = 'q8'
transition_table[('q8', 'o')] = 'q9'
transition_table[('q9', ' ')] = 'q50'
transition_table[('q9', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'

# update the transition table for the following token: mamang
transition_table[('q0', 'm')] = 'q1'
transition_table[('q1', 'a')] = 'q2'
transition_table[('q2', 'm')] = 'q4'
transition_table[('q4', 'a')] = 'q5'
transition_table[('q5', 'n')] = 'q6'
transition_table[('q6', 'g')] = 'q7'
transition_table[('q7', ' ')] = 'q50'
transition_table[('q7', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'


# update the transition table for the following token: meli
transition_table[('q0', 'm')] = 'q1'
transition_table[('q1', 'e')] = 'q10'
transition_table[('q10', 'l')] = 'q11'
transition_table[('q11', 'i')] = 'q12'
transition_table[('q12', ' ')] = 'q50'
transition_table[('q12', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'

# update the transition table for the following token: abah
transition_table[('q0', 'a')] = 'q13'
transition_table[('q13', 'b')] = 'q14'
transition_table[('q14', 'a')] = 'q15'
transition_table[('q15', 'h')] = 'q16'
transition_table[('q16', ' ')] = 'q50'
transition_table[('q16', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'

# update the transition table for the following token: nyingok
transition_table[('q0', 'n')] = 'q17'
transition_table[('q17', 'y')] = 'q18'
transition_table[('q18', 'i')] = 'q19'
transition_table[('q19', 'n')] = 'q20'
transition_table[('q20', 'g')] = 'q21'
transition_table[('q21', 'o')] = 'q22'
transition_table[('q22', 'k')] = 'q23'
transition_table[('q23', ' ')] = 'q50'
transition_table[('q23', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'


# update the transition table for the following token: ngenjuk
transition_table[('q0', 'n')] = 'q17'
transition_table[('q17', 'g')] = 'q24'
transition_table[('q24', 'e')] = 'q25'
transition_table[('q25', 'n')] = 'q26'
transition_table[('q26', 'j')] = 'q27'
transition_table[('q27', 'u')] = 'q28'
transition_table[('q28', 'k')] = 'q29'
transition_table[('q29', ' ')] = 'q50'
transition_table[('q29', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'

# update the transition table for the following token: televisi
transition_table[('q0', 't')] = 'q30'
transition_table[('q30', 'e')] = 'q31'
transition_table[('q31', 'l')] = 'q32'
transition_table[('q32', 'e')] = 'q33'
transition_table[('q33', 'v')] = 'q34'
transition_table[('q34', 'i')] = 'q35'
transition_table[('q35', 's')] = 'q36'
transition_table[('q36', 'i')] = 'q37'
transition_table[('q37', ' ')] = 'q50'
transition_table[('q37', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'


# update the transition table for the following token: telok
transition_table[('q0', 't')] = 'q30'
transition_table[('q30', 'e')] = 'q31'
transition_table[('q31', 'l')] = 'q32'
transition_table[('q32', 'o')] = 'q38'
transition_table[('q38', 'k')] = 'q39'
transition_table[('q39', ' ')] = 'q50'
transition_table[('q39', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'

# update the transition table for the following token: sungi
transition_table[('q0', 's')] = 'q40'
transition_table[('q40', 'u')] = 'q41'
transition_table[('q41', 'n')] = 'q42'
transition_table[('q42', 'g')] = 'q43'
transition_table[('q43', 'i')] = 'q44'
transition_table[('q44', ' ')] = 'q50'
transition_table[('q44', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'

# update the transition table for the following token: bakso
transition_table[('q0', 'b')] = 'q45'
transition_table[('q45', 'a')] = 'q46'
transition_table[('q46', 'k')] = 'q47'
transition_table[('q47', 's')] = 'q48'
transition_table[('q48', 'o')] = 'q49'
transition_table[('q49', ' ')] = 'q50'
transition_table[('q49', '#')] = 'accept'
transition_table[('q50', ' ')] = 'q50'
transition_table[('q50', '#')] = 'accept'



#Parser
#Symbols Defination
non_terminals = ['S', 'NN', 'VB']
terminals = ['mak', 'abah', 'televisi', 'sungi', 'bakso',
             'telok', 'mamang', 'meli', 'majo', 'nyingok', 'ngenjuk']

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

print()
print()
print('                 LEXICAL ANALYZER                     ')
# lexical analysis main
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept':
    current_char = string_check[idx_char]
    current_token += current_char
    state = transition_table[(state,current_char)]
    if state == 'q3':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q7':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q9':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q12':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q16':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q23':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q29':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q37':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q39':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q44':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'q49':
        print('current token: ' ,current_token,' valid')
        current_token = ''
    if state == 'error':
        print('error')
        break;
    idx_char = idx_char + 1

# conclusion
if state == 'accept':
    print('semua token di input: ', input_sentence, ' valid')


print()
print()
print('                     PARSER                         ')
#Parsing Process main
if state == 'accept':
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
                break
        elif top in non_terminals:
            print('Top adalah simbol non_terminals')
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                symbol_pushed = parse_table[(top, symbol)]
                for i in range(len(symbol_pushed)-1, -1, -1):
                    stack.append(symbol_pushed[i])
            else:
                print('error')
                break
        else:
            print('error')
            break
        print('Isi Stack : ', stack)
        print()

    #Kesimpulan
    print()
    if symbol == 'EOS' and len(stack) == 0:
        print('Input String ', input_sentence, ' Accepted, Sesuai Grammar')
    else:
        print('ERROR, Input String ', input_sentence,
            'Rejected, Tidak Sesuai Grammar')
else :
    print('error')
