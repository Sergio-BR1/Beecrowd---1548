def mergeSort(lista):

	if len(lista) > 1:
		meio = len(lista) // 2
		esquerda = lista[:meio]
		direita = lista[meio:]
		mergeSort(esquerda)
		mergeSort(direita)
	
		topo_esq, topo_dir, k = 0, 0, 0
		while topo_esq < len(esquerda) and topo_dir < len(direita):
			if esquerda[topo_esq] > direita[topo_dir]:
				lista[k] = esquerda[topo_esq]
				topo_esq+=1
			else:
				lista[k] = direita[topo_dir]
				topo_dir+=1
			k+=1
	
		while topo_esq < len(esquerda):
			lista[k] = esquerda[topo_esq]
			topo_esq+=1
			k+=1
			
		while topo_dir < len(direita):
			lista[k] = direita[topo_dir]
			topo_dir+=1	
			k+=1

N = int(input())
for i in range(N):
	M = int(input())
	aux = input().split()
	alunos = [int(j) for j in aux]
	copia = alunos.copy()
	mergeSort(copia)
	count = 0
	for j in range(len(copia)):
		if alunos[j] != copia[j]:
			count+=1
	print(M-count)
			