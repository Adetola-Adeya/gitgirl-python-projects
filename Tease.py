Write a python script to convert the lists below into a dictionary
name = ['Ayo', 'Barbie', 'Carla', Dede', 'Eugene']
Age = [21, 13, 57, 43, 2]




name = ['Ayo', 'Barbie', 'Carla', 'Dede', 'Eugene']
Age = [21, 13, 57, 43, 2]

print ("Original name list is : " + str(name)) 
print ("Original Age list is : " + str(Age))
res = dict(zip(name,Age))
print ("Resultant dictionary is : " +  str(res)) 
