from operator import mod

frequency = {
    'e' : 12.02,
    't' : 9.10,
    'a' : 8.12,
    'o' : 7.68,
    'i' : 7.31,
    'n' : 6.95,
    's' : 6.28,
    'r' : 6.02,
    'h' : 5.92,
    'd' : 4.32,
    'l' : 3.98,
    'u' : 2.88,
    'c' : 2.71,
    'm' : 2.61,
    'f' : 2.30,
    'y' : 2.11,
    'w' : 2.09,
    'g' : 2.03,
    'p' : 1.82,
    'b' : 1.49,
    'v' : 1.11,
    'k' : 0.69,
    'x' : 0.17,
    'q' : 0.11,
    'j' : 0.10,
    'z' : 0.07
}

maxLength = 50

text = 'lxyikbcisvqlmkoakmepoinrwqgifboseifmkqbrhhvwjqqeoerxdmntkipwemieopaamkxivwhcdqkeglgedmoxseesszywwswkzxvhzeutscigkifmpixxocvegujrwluiywvrgqgboqolwlgagzosivgkwxomrrqnopdgkvgbsqgrlkjbeimivetmeiyidqgzwezvhwqtvqixkihqjaoqrrvpgnzyusrmsvmioicawiamjytmopdgkjgtdmqiqjwzlpzvlrvpwezinwvpsbasopqewlvjwitawdzrzigskqoadwcvfwprfifbzioxkivwmkctdhywmtyfhhkauwixlrwmvicypmnqsbdrjvgbjmvxeccvstmidhaiatdrjgquhiiceyvezmivhxcqdmmwzitmlwghwlgguwppgwgtdbciuioiavdrjxcjdmowdxcymimxhvqnlpzsumiqfigtumemavnxhefwxbciltclhzdghqcbupdrjepllpzxryephiywistbmvzweiiifbjqdkkkstgcwytvszjyqhvpwapqzeuvgbzrryiplwxsyitusvpjdgvcjqikfsubkjpxzeuamnamfmgvlbjtusoxliwybmpotwieqdckmbkvlggbgcxlsefaxtzarjhbzmnlhpxmkedxkpgvybcctygcwaasuqkvywpxvmfmkbjgnmubkiihzidaabzwhbrmjqzrfmpoxzzrcmglvmheqhuwabrevxjilpzaoivbhixodvfgwaoiuhcgxwprgmvawtathvhwjudrjcgbsvjxkitclcmrlrcvwvovbtqalmysqxjmuwhtdraattjklxcvfwprfifbzioeixgztmdrjtnmsavrwpaamzkvlwgltgneoiuwxbcifyvxjqxiwedtwbdxzswtvjzvhxwzfqikwlgbgcxlsefbgbcipetswbjrdxguhwmeucdikqnxkiuxwmyewajqupdxgmuihxzeuifnjwhmqzgvlwmckeujwmiwwypvavbxkiubsbzqhrvmpxgelrglomceyifmuqyigxqxjwyyfiqvwtvwwvwvgnosxgjxslnxrqgmlcijxphqdtzhgioiflolhvwvoqgpeinqeqoigxqvgzoldqgzakvruiviatzvvsptqiihzmntdinxistwftteiiyewmfwwlgzwqnlragdwzjrhjcbstapdakvlpztoepikbzgkrqtgotfosiowznldzgjwmiuxmeslwkslrvwmbolhxqcupkegwoiqjztrtwtszwywxjmqzzwwmntfwokrmpolwwisvqnabvfoiiqnmixkinwxbtgrwvwxxmsgyebawilhanmlbkefoczvqnxkswozboseinwkqikvsomgvzzhvalwddghwqtveccwlgvlpzckexmvmxmgifbgmhfueemlpzprwuussdrjttwvcxxlwvpwapfmiebgnnspiuxwkppdxkwfzztrvvaxzjqwekesvdrgmeilmoldxkbeitldzgbgljalxjamzkpxwrijbnlhpfjquvrxjcklcmiuwypatzswlgzkpvzhwwoymnxhhvpwujzhmuifioxhqrblwbeurgzsnzassuqlqqikicldqiivehbwzhsqxjagniijevqnmkvhwuezioiyitbzmmidwqvzxnvhzgzkigmvrvymqoisvqdavbxkirzuwptwlgkgukeqcoiqpvzhlqxwlxvlxkkkpvzhhgauzdfhhkbsavxumwuhpjjpefvwansyitkguhsqwgvkmvvjykvybcewmvivlnxrxjmazmisyvilqjristqflzglwkwfuzeqajqdmzrwitxjqnmqkrcfbzvvagzwuzvumngjmniopkvybcilvdijovmqfkvlwpgktclkiohrydtwbcisvkkwgzwwitlsgvqddqvuwppgwqwfjzpdypkzqikdmpbsjgiwgquhcoiuxqzadvpwlgqhiyefgqzvqikwstmhwmxvgkbavbeqspgewpwvswzumnmqyralzzepgquhwiiqxuchxgmhvulaodxlqgaeibecmpmkidhwlgbsjgiwaqcdlnxdvvazqktlrivwfoqrrvpsvyarynltmasopqewlwcdmpdwznmrrgijttrhbvgwimxkitmhwmxlrvpwbvmzepmkmhejebqfmfrrapngzdxvgnwkmgmqoubgaptspkmjajjkmvmupxsptqvwvowdhfaomdkkxvwjchsxvubzioepebwfqnwrspbgmixhvvpwuvvnivkmzmiqxngvwhmqevmvjtestnmkqkegajqdmolhgquhiickeuvgbtiwgqvxqmqhhcvqbcmqkemgrzjifghganelheckbjqhvuazwppgwviqbprhhypwvvwnifqfuvcdfqclbcissuaajdplxawxikvrhwkltvyqgj'

length = len(text)
m      = 26 # eng alph length

def countEq(str1, str2) :

    minLen = min(len(str1), len(str2))
    count  = 0

    for i in range(minLen) :
        if str1[i] == str2[i] :
            count += 1

    return float(count) / minLen

def textFr(text) :

    n  = len(text)    
    fr = {}

    for i in text :
        try :
            fr[i] += 1
        except :
            fr[i] = 1

    return max(fr, key=lambda i: fr[i])

def decode(text, key) :

    keyLength = len(key)
    length    = len(text)
    decPeaces = []
    decText   = ''

    for i in range(keyLength) :
        decPeaces.append(''.join(map(lambda a: chr(ord('a') + mod(ord(a) - ord(key[i]), 26)), text[i : length : keyLength])))

    for j in range(len(decPeaces[len(decPeaces) - 1])) :
        for i in decPeaces :
            decText += i[j]

    return decText[:maxLength]

def indexMeth(text) :
    
    strs = []
    eqs  = []
    keyStr = ''
    
    for i in range(m/2) :
        strs.append(text[i:] + text[:i])

    for i in range(1, len(strs)) :
        eqs.append(countEq(text, strs[i]))

    keyLength = max(range(len(eqs)), key=lambda i: eqs[i]) + 1
    maxFr     = max(frequency, key=lambda i: frequency[i])

    for i in range(keyLength) :
        keyStr += chr(ord('a') + mod(ord(textFr( text[i : length : keyLength] )) - ord(maxFr), 26))

    print keyStr
    keyStr = 'decisive'
    #decText = decode(text, keyStr)
    decText = decode(text, keyStr)

    print keyStr
    print decText

indexMeth(text)
#print decode(text, 'favorit')
