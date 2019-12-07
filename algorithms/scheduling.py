# from collections import deque
class people:
    def __init__(self,id,streams):
        self.id = id
        self.streams = []
        self.streams = streams.copy()

    def __str__(self):
        return (self.id)


n = int(input("number of people: "))
arr = []
while n>0:
    id = input("id: ")
    streams = input("Streams (enter space separated T,M,D): ").split()
    n-=1
    arr.append(people(id,streams))

# my_queue = deque([])

t_arr = []
m_arr = []
d_arr = []

for i in range(len(arr)):
    for j in range(len(arr[i].streams)):
        if arr[i].streams[j]=="T":
            t_arr.append("T"+arr[i].id)
        if arr[i].streams[j]=="M":
            m_arr.append("M"+arr[i].id)
        if arr[i].streams[j]=="D":
            d_arr.append("D"+arr[i].id)

# t_arr = t_arr[::-1].copy()
# m_arr = m_arr[::-1].copy()
# d_arr = d_arr[::-1].copy()

# print("-------------")

# print("-------------")

t_current = []
m_current = []
d_current = []


if len(t_arr)!=0:
    for k in range(len(t_arr)):
        if (("M"+t_arr[k][1] not in m_current) and ("D"+t_arr[k][1] not in d_current)):
            t_current.append(t_arr.pop(k))
            break

if len(m_arr)!=0:
    for k in range(len(m_arr)):
        if (("T"+m_arr[k][1] not in t_current) and ("D"+m_arr[k][1] not in d_current)):
            m_current.append(m_arr.pop(k))
            break
if len(d_arr)!=0:
    for k in range(len(d_arr)):
        if (("M"+d_arr[k][1] not in m_current) and ("T"+d_arr[k][1] not in t_current)):
            d_current.append(d_arr.pop(k))
            break

print("current status: \n  t    m    d")
print(t_current,m_current,d_current)
print("\n")
print(t_arr)
print(m_arr)
print(d_arr)

print("-----------------\n")

while(len(t_arr)!=0 or len(m_arr)!=0 or len(d_arr)!=0):
    choice = input("t or m or d : ").strip()
    print("current status: \n  t    m    d")
    if choice=="t" and len(t_current)!=0:
        t_current.pop()
    elif choice=="m" and len(m_current)!=0:
        m_current.pop()
    elif choice=="d" and len(d_current)!=0:
        d_current.pop()
    else:
        print("-- Invalid choice --")
        continue
    print(t_current,m_current,d_current)
    print("\n")
    # print(t_arr[::-1])
    # print(m_arr[::-1])
    # print(d_arr[::-1])
    print(t_arr)
    print(m_arr)
    print(d_arr)
    print("\nAfter scheduling: ")

    if len(t_arr)!=0:
        if len(t_current)==0:
            for k in range(len(t_arr)):
                if (("M"+t_arr[k][1] not in m_current) and ("D"+t_arr[k][1] not in d_current)):
                    t_current.append(t_arr.pop(k))
                    break
    if len(m_arr)!=0:
        if len(m_current)==0:
            for k in range(len(m_arr)):
                if (("T"+m_arr[k][1] not in t_current) and ("D"+m_arr[k][1] not in d_current)):
                    m_current.append(m_arr.pop(k))
                    break
    if len(d_arr)!=0:
        if len(d_current)==0:
            for k in range(len(d_arr)):
                if (("M"+d_arr[k][1] not in m_current) and ("T"+d_arr[k][1] not in t_current)):
                    d_current.append(d_arr.pop(k))
                    break
    print("  t    m    d")
    print(t_current,m_current,d_current) 
    print()
    print(t_arr)
    print(m_arr)
    print(d_arr)
    # print(t_arr[::-1])
    # print(m_arr[::-1])
    # print(d_arr[::-1])
    print("-----------------\n")

# print(arr[0])



# ---------- SAMPLE INPUT -----------------

# number of people: 7
# id: 1
# Streams (enter space separated T,M,D): T M D
# id: 2
# Streams (enter space separated T,M,D): T M D
# id: 3
# Streams (enter space separated T,M,D): T M D
# id: 4
# Streams (enter space separated T,M,D): T M
# id: 5
# Streams (enter space separated T,M,D): D
# id: 6
# Streams (enter space separated T,M,D): D
# id: 7
# Streams (enter space separated T,M,D): T