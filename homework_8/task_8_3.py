flowers = {"rose":"red", "Nargiz":"yellow", "Shresht":"blue", "Krizantem":"white", "Mexak":"red"}
filt = list(filter(lambda key: flowers[key]=="red", flowers))
print(filt)