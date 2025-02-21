# In case it's not obvious, a list comprehension produces a list, but
# it doesn't have to be given a list to iterate over.
#
# You can use a list comprehension with any iterable type, so we'll
# write a comprehension to convert dimensions from inches to centimetres.
#
# Our dimensions will be represented by a tuple, for the length, width and height.
#
# There are 2.54 centimetres to 1 inch.
 
inch_measurement = (3, 8, 20)
 
#cm_measurement = [measurement *2.54 for measurement in inch_measurement] # as a list
#cm_measurement = tuple(measurement * 2.54 for measurement in inch_measurement) as a tuple
cm_measurement = [(measurement,  measurement*2.54) for measurement in inch_measurement] # both orinal and the converted value

print(cm_measurement)
 
# Once you've got the correct values, change the code to produce a tuple, rather than a list.