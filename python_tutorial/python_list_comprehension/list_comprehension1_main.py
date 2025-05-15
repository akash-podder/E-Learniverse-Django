# Normal Version
values = []
for x in range(10):
    if x%2==0:
        values.append(x)
print(values)

# List Comprehension
# [x for x in range(10) CONDITION]
values = [x for x in range(10) if x%2==0]
print(values)