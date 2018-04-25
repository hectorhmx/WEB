Arreglito=[[1,2,[4,5,[6,7,8]]],9,0]
def aplanador (Arreglito):
for i in A:
	if isinstance(i,list):
		aplanador(i)
	else:
		print i;
