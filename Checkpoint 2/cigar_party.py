def cigar_party(number, weekend):
    if weekend=='True':
        if number>=40:
            return True
        else:
            return False
    if weekend=='False' and number>=40 and number<=60:
        return True
    else:
        return False


print (cigar_party(30,'False'))
print (cigar_party(50,'False'))
print (cigar_party(70,'True'))
print (cigar_party(30,'True'))
