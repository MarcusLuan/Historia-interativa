def entradas():
  global prota, local, razao, ato1, acao, ato2, fim
  prota = input("Primeiro, diga o nome do seu protagonista(Ex: Ana): ")
  local = input("Agora, diga onde ocorre sua historia(Ex: Casa): ")
  razao = input("Agora, diga o que o prota estava fazendo no local(Ex: Andando): ")
  ato1 = input("Agora, diga um evento inesperado que ocorreu(Ex: Ela se melou): ")
  acao = input("Diga o que o protagonista fez(Ex: Ela correu ate o local): ")
  ato2 = input("Agora, diga o que aconteceu logo apos isso(Ex: Ele continuou andando): ")
  fim = input("Por fim, finalize a historia com um final feliz(Ex: Ela conseguiu um 10): ")

def finalizar():
  global prota, local, razao, ato1, acao, ato2, fim
  print ("Aqui esta sua historia:")
  print("Era uma vez, em", local,", uma pessoa chamada", prota,".")
  print ("Certo dia,", prota,"estava", razao,", ate que, de repente,", ato1,".")
  print ("Imediatamente,", acao,", e entao,", ato2,".")
  print ("Felizmente,", fim,", Fim.")
  
print("Bem vindo a historias.com, seu site para criar historias curtas.")
print("PS: As historias podem sair com erros, entao, forneca um input claro.")
entradas()
print ("-"*60)
finalizar()
