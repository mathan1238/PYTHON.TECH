votes = {1:"a",2:"a",3:"c",4:"a",5:"c",6:"b",7:"b",8:"b",9:"b",10:"c",\
         11:"a",12:"b",13:"b",14:"c",15:"b"}

result = {}
for i in votes:
    vol=votes[i]
    if vol not in result:
        result[vol]=1
    else:
        result[vol]=result[vol]+1
print("Voting result are !")
print(result)
mx = 0
for i in result:
    if result[i] > mx:
        mx= result[i]
        leader=i
print("The leader of the the primary class is",leader,"with",mx,"votes")

print("congrates to that student")
