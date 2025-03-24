import re 


x = "Giovanna tem 54 anos de idade e três gatos pretos, três gatos cinzas e 5 cachorros"

print(re.findall("gatos", x))
print(re.search("gatos",x))
print(re.search("gatos",x).span())
print(re.search("gatos",x).string)
print(re.search("gatos",x).group())
print(re.split("\s",x,2))
print(re.sub("gatos","julia",x,2))