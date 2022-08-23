from collections import Counter


with open('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/3.txt') as f:
    binaries = f.read().splitlines()
    decimals = [int(entry, 2) for entry in binaries]


first = [item[0] for item in binaries]
sec = [item[1] for item in binaries]
thi = [item[2] for item in binaries]
fou = [item[3] for item in binaries]
fif = [item[4] for item in binaries]
six = [item[5] for item in binaries]
sev = [item[6] for item in binaries]
eig = [item[7] for item in binaries]
nin = [item[8] for item in binaries]
ten = [item[9] for item in binaries]
ele = [item[10] for item in binaries]
twe = [item[11] for item in binaries]

c1 = Counter(first)
c2 = Counter(sec)
c3 = Counter(thi)
c4 = Counter(fou)
c5 = Counter(fif)
c6 = Counter(six)
c7 = Counter(sev)
c8 = Counter(eig)
c9 = Counter(nin)
c10 = Counter(ten)
c11 = Counter(ele)
c12 = Counter(twe)

print(c1.most_common(1))
print(c1.most_common(1))
print(c2.most_common(1))
print(c3.most_common(1))
print(c4.most_common(1))
print(c5.most_common(1))
print(c6.most_common(1))
print(c7.most_common(1))
print(c8.most_common(1))
print(c9.most_common(1))
print(c10.most_common(1))
print(c11.most_common(1))
print(c12.most_common(1))

gamma_rate = '100110110100'
epsilon_rate = '011001001011'

gamma_dec = int(gamma_rate, 2)
episol_dec = int(epsilon_rate, 2)

print(gamma_dec * episol_dec)