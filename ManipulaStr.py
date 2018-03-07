###########################################################################
#                                                                         #
#                       Exemplos de código Python                         #
#                                                                         #
#           Aplicado na disciplina de Lógica de Programação               #
#                                                                         #
# Autores: Denny Azevedo & Marilene Esquiavoni                            #
#                                                                         #
# Tema: Strings e suas funções                                            #
#                                                                         #
###########################################################################

frase = "Você pode encarar um erro como uma besteira a ser esquecida, ou como um resultado que aponta uma nova direção"

print("=" * 80)
print()
print(frase)
print()
print("=" * 80)

#Tamanho da String - número de caracteres
tam = len(frase)

print()
print("O tamanho da frase é de %d caracteres" % tam)
print()
print("=" * 80)

#Modificar a frase para letras maiúsculas
print()
print(frase.upper())
print()
print("=" * 80)

#Modificar a frase para letras minúsculas
print()
print(frase.lower())
print()
print("=" * 80)

#Verifica caracteres finais da frase
achou = frase.endswith("direção")

print()
print("A frase termina com: direção - %s" % achou)
print()

achou = frase.endswith("rumo")

print()
print("A frase termina com: rumo - %s" % achou)
print()

print("=" * 80)

#Verificar caracteres iniciais da frase
achou = frase.startswith("Você")

print()
print("A frase inicia com: Você - %s" % achou)
print()

achou = frase.startswith("Vamos")

print()
print("A frase inicia com: Vamos - %s" % achou)
print()

print("=" * 80)

#Localizar uma palavra na frase
onde = frase.find("esquecida")

print()
print("A localização na frase da palavra: esquecida - %s" % onde)
print()

onde = frase.find("como")
#observe que foi localizado a primeira ocorrencia da palavra
print()
print("A localização na frase da palavra: como - %s" % onde)
print()

print("=" * 80)

#Troca palavras dentro da frase
nfrase = frase.replace("erro","falha")

print()
print(nfrase)
print()

