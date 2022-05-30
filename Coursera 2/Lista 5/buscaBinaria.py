#definindo a funçao de busca binaria;
def busca(lista, elemento):
  primeiro = 0
  ultimo = len(lista) - 1

  while primeiro <= ultimo:
    meio = (ultimo + primeiro) // 2
    print(meio)
   
    if lista[meio] == elemento:
      return meio
    
    else:
      
      if lista[meio] > elemento:
        ultimo = meio - 1
      
      else:
        primeiro = meio + 1
    

      
  return False


