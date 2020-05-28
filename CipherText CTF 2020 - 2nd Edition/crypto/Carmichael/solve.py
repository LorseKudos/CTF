from itertools import product

enc_flag = "gevcyr_qrf_pna_or_qbar_jvgu_nyy_nytbevguzf"

alph1={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
alph2={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def enc(text,key):
	cipher=""
	while key>25:
		key=key//2
	for i in text:
		if i in alph1:
			cipher+=alph2[(alph1[i]+key)%26]
		else:
			cipher+=i
	return cipher

def dec(cipher,key):
	text=""
	while key>25:
		key=key//2
	for i in cipher:
		if i in alph1:
			text+=alph2[(alph1[i]-key)%26]
		else:
			text+=i
	return text

i = 0
for j, k in product(range(25), range(25)):
    print(dec(enc(dec(enc_flag, i), j), k))
