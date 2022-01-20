import matplotlib.pyplot as plt

def factorial(start,stop=1):
	if start == stop:
		return 1

	if start == 0:
		return 1

	return start * factorial(start-1,stop)

def calcDoubleBirthdayProbability(people):
	return (1 - (factorial(365,365-people)/365**people))

people = []
propability = []

currentProbability = 0
currentpeople = 0

# while currentProbability <0.8:
while currentpeople <=365:
	currentProbability = calcDoubleBirthdayProbability(currentpeople)
	people.append(currentpeople)
	propability.append(currentProbability)

	currentpeople +=1

print (f"With {int(people[-1]):d} people in the room, there is a probability of {propability[-1]*100:2.5f}% that to people have the same birthday.")

fig, ax = plt.subplots()

ax.plot(people,propability)
ax.set_xlabel("number of people")
ax.set_ylabel("probability of pair")
ax.set_title("birthday problem")

plt.show()

