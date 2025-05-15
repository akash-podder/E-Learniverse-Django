# Nested 3 For Loop
l3 = []

for i in range(5):
    l1  = []
    for j in range(5):
        l2 = []
        for k in range(5):
            l2.append(k)
        l1.append(l2)
    l3.append(l1)

print(l3)

# List Comprehension
# [[[3rd For Loop] 2nd For Loop] 1st For Loop]
new_list = [[[k for k in range(5)] for j in range(5)] for i in range(5)]
print(new_list)