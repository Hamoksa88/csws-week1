from audioop import reverse


name=["Danny","Jake","Bogy","ibi"]


for name in name:
    print(f"Hello {name.title()}")
Countries=["Usa","Canada","New Zealend","Italy"]
print(sorted(Countries))
print (Countries)
print(sorted(Countries, reverse=True))
Countries.reverse()
print(Countries)
Countries.sort()
print(Countries)
print(len(Countries))
Countries.append("France")
print(Countries)
Countries.insert(2,"Netherland")#
print(Countries)
del Countries[2]
print(Countries)
Countries.remove("France")
print(Countries)
x = Countries.pop(3)
print(Countries)