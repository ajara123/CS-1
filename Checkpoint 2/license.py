def license (age, hours):
    while age<16:
        return ('License cannot be issued')
    if hours>200:
        return ('License to be issued')
    else:
        return ('Licence cannot be issued')
        
print (license(18, 205))
print (license (15, 205))
print (license(22, 198))
print (license(16, 206))
