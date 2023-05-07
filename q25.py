class sampleclass:
    count=0
    def increase(self):
         sampleclass.count += 1
s1 = sampleclass()
s1.increase()

print(s1.count)
s2 = sampleclass()
s2.increase()
print(s2.count)
print(sampleclass.count)
