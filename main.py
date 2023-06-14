def calcola(mode):
    inp_bin = list()
    # Conversione
    for digit in inp:
        inp_bin += hex_dict[digit]

    # Calcolo del numero di bit di controllo
    check_bits_number = 0
    if mode:
        while (2 ** check_bits_number) <= (len(inp_bin) + check_bits_number):
            check_bits_number += 1
    else:
        while (2 ** check_bits_number) <= (len(inp_bin)):
            check_bits_number += 1

    # Calcolo della posizione dei bit di controllo
    check_bits_pos = list()
    for i in range(check_bits_number):
        check_bits_pos.append(len(inp_bin) - 2 ** i)
    check_bits_pos.reverse()

    # Calcolo dei bit di controllo
    check_bits = list()
    for i in check_bits_pos:
        check_bits.append(int(inp_bin[i]))

    check_bits_pos.reverse()
    inp_bin.reverse()

    # Se cerchiamo i bit da aggiungere, inseriamoli nell'array
    if mode:
        for k in range(check_bits_number):
            # I bit avranno 0 come valore perché non influisce sull'exor
            inp_bin.insert((2 ** k) - 1, 0)

    check_bits_result = list()

    # Compensiamo per i 'check_bits_number' elementi in più nell'array
    for k in range(check_bits_number):
        if mode:
            offset = len(inp_bin) - (1 + check_bits_number) - check_bits_pos[k]
        else:
            offset = len(inp_bin) - 1 - check_bits_pos[k]

        check_bits_result.append(0)
        j = 2 ** k

        for e in inp_bin:
            # Saltiamo i bit già calcolati e passiamo alla prossima iterazione del for
            if offset > 0:
                offset -= 1
                continue
            # j positivo marca i numeri da considerare
            if j > 0:
                check_bits_result[k] += int(e)
            # Reset dopo i numeri ignorati
            elif -j == 2 ** k:
                j = 2 ** k
                continue

            j -= 1

            # Evitiamo lo 0 per far funzionare '-j' (-0 === 0)
            if j == 0:
                j -= 1

        # Se gli 1 sono pari, l'exor risulta 0, altrimenti 1
        if check_bits_result[k] % 2:
            check_bits_result[k] = 1
        else:
            check_bits_result[k] = 0

    check_bits_result.reverse()

    if mode:
        print("I bit di controllo da aggiungere sono: ", check_bits_result)
    else:
        print("I bit di controllo per gli errori sono: ", check_bits_result)


while True:
    # Input
    inp = input("Inserisci il numero in base 16: ").lower()

    # Dizionario per conversione da base 16 a base 2
    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

    # Calcolo di parità
    calcola(False)  # Bit di errore
    calcola(True)  # Bit da aggiungere
