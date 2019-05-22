# Ex 3.4 - 3.7

def send_invitations(guests):
	for name in guests:
		print("Hello " + name + ', would you like to dinner?')


guests = ['fred', 'amy', 'daisy']

send_invitations(guests)

guests.remove('amy')
guests.insert(1, 'danny')

send_invitations(guests)

print("I have found a bigger table...")
guests.insert(0, 'wang')
guests.insert(len(guests)/2, 'liu')
guests.append('jin')
send_invitations(guests)

for i in range(len(guests) - 2):
	name = guests.pop()
	print("Sorry, " + name)

send_invitations(guests)

del guests[0]
del guests[0]

print(guests)