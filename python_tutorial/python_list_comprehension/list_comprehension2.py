# String that starts with `a` & ends with `y`
string_list = ["any", "albany", "apple", "world", "hello", ""]
new_list = []

for s in string_list:
    if len(s) >=2 and s[0] == 'a' and s[-1] == 'y':
        new_list.append(s)

print(new_list)

# List Comprehension
# [x for x in range(10) CONDITION]
new_list = [s for s in string_list
            if len(s) >=2 and s[0] == 'a' and s[-1] == 'y'
          ]
print(new_list)

new_list = [s for s in string_list
            if len(s) >=2
            if s[0] == 'a'
            if s[-1] == 'y'
          ]

print(new_list)