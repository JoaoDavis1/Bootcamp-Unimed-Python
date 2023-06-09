curso = "pYtHoN"

print(curso.upper())
print(curso.lower())
print(curso.title())

curso01 = "    Python"
#strip remove todo espaço sobrando
print(curso01.strip())
#lstrip revove todo espaço da esquerda(left)
print(curso01.lstrip())
#rstrip remove todo espaço da direita(rigth)
print(curso01.rstrip())

curso02 = "Python"
#centralização
print(curso02.center(12, "*"))
#Junção
print(".".join(curso02))