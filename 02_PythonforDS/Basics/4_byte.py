#Given a variable of type bytes how do convert it to string, given if I don't know which encoding decoding was used for byte?
#Answer you can't 

s = 'abcd'  #Latin and included in ASCII so take 1 byte per charector
print(len(s))
 #lets take hebrew now
s = 'שלום' #Hebrew Arabic Russian Greek even special charector in English take 2 byte
print(len(s))

#Unicode --> Lest assign a a unique number to every charector ever created and it will be represented using UTF-8
#UTF-* means, if its ASCII it will take 1 byte, for Hebre, Russian Greek 2 bytes, chenese Japnese 3 bytes and emojis 
#b = bytes('abc') # won't work without mentioning encoding
b = bytes('abc', encoding='utf-8')
print(b)
#or
b = b'abc'
print(type(b))
print(b[0]) 


s = 'שלום'
b = bytes(s, encoding='utf-8')
print(b)
#Simillarly to convert back to string
s = str(b, encoding='utf-8')
print(s)
s = str(b, encoding='latin-1')
print(s)  #wrong output


#byte string  like String are immutable
s = 'abcd'
# s[0] = 'r'  #can't do
b =b'abcd'
# b[0] ='65'  #can't do
