numphy=int(input('введите кол-во участников математика'))
print('введите имена участников олимпиады по математике')
olymp1 = set()
for i in range(numphy):
    olymp1.add(input())
    k=len(olymp1)
print(k)
print(olymp1)

numath=int(input('введите кол-воучастников физика'))
print('введите имена участников олимпиады по физике')
olymp2 = set()
for i in range(numath):
    olymp2.add(input())
    q=len(olymp2)
print(q)
print(olymp2)

numit=int(input('введите общее кол-во информатика'))
print('введите имена участников олимпиады по информатике')
olymp3 = set()
for i in range(numit):
    olymp3.add(input())
    w=len(olymp3)
print(w)
print(olymp3)

z=set()
z.update(olymp1)
z.update(olymp2)
z.update(olymp3)
t=len(z)
print(t)
print('Общее кол-во участников в трёх олимпиадах',t)
print(z)