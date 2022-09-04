friends = ["Joey", "Chandler", "Ross",
           "Monica", "Rachel", "Phoebe"]

numbers = [1, 2, 3, 4, 5, 6]

friends.extend(numbers)
print(friends)

friends = ["Joey", "Chandler", "Ross",
           "Monica", "Rachel", "Phoebe"]

friends.append("Ursula")
print(friends)

friends.insert(1, "Gunther")
print(friends)

friends.remove("Ursula")
print(friends)

print(friends.index("Phoebe"))

print(friends.count("Joey"))

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)