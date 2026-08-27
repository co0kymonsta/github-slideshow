def response(hey_bob):
    clean = hey_bob.strip()
    if not clean:
        return('Fine. Be that way!')
    if clean.endswith('?') and clean.isupper():
        return('Calm down, I know what I\'m doing!')
    if clean.isupper():
        return('Whoa, chill out!')
    if clean.endswith('?'):
        return('Sure.')
    if isinstance(hey_bob, str):
        return('Whatever.')
    
    
