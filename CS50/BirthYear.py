years_of_birth = [1999, 1990, 1921, 1900]
ages = [2024 - years for years in years_of_birth]

ages2 = []

for years in years_of_birth:
    ages2.append(2024-years)

print((ages))

print((ages2))

#Linha 2: estrutura for feita dentro dos colchetes, facilitando trabalho e linha 
    # Temos 'years' for 'years' in 'years_of_birth'
    ##O primeiro 'years' se refere ao número atual que sera subtraído de 2024
    ###o segundo 'years' refere-se ao número que estará passando pelos números dentro de 'years_of_birth'

##Outra alternativa: fazer uma lista e utilizar o append, teremos o exato mesmo resultado, pois os dois são exatamente a mesma coisa
