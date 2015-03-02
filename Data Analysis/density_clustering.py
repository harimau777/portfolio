#! /usr/bin/python

#This program performs density based clustering by calculating core points, border points, and outlier points.

import sys

e_distance = 2		#The distance used to define a points e neighborhood.
min_pnts = 3		#The minimum number of neighborhood points required to be considered a core point.

core_list = []		#Holds core points and the points in their neighborhood.
border_list = []	#Holds border points and the points in their neighborhood.
outlier_list = []	#Holds points that are neither core points or border points.
temp_list = []		#Holds points temporarily until we can determine if they are border or outlier
			#	points.

#Read the data from the file:
point_list = []
point_file = open(sys.argv[1], "r")
for i in point_file:
        point = i.strip().split('\t')
	point_list.append([float(point[0]), float(point[1]), point[2]])
point_file.close()

#Find core points:
for pnt1 in point_list:
	neighborhood = []		#Holds the points in pnt1's neighborhood.
	for pnt2 in point_list:
		distance = ((pnt1[0] - pnt2[0])**2 + (pnt1[1] - pnt2[1])**2)**.5
		if distance <= e_distance:	#If pnt2 is in pnt1's neighborhood.
			neighborhood.append(pnt2)
	if len(neighborhood) >= min_pnts:	#If pnt1 is a core point
		core_list.append([pnt1, neighborhood])
	else:
		temp_list.append(pnt1)

#Determine if non-core points are border or outlier points:
for pnt in temp_list:	#Loop through each point in the temporary list.
	border_switch = 0	#Indicates if pnt has been found to be a border point (1) or not (0).
	for core_point in core_list:	#Loop through each of the core points.
		for neighbor in core_point[1]:	#Loop through the current core point's neighbors.
			if (pnt[0] == neighbor[0]) and (pnt[1] == neighbor[1]):
				border_list.append(pnt)
				border_switch = 1
				break
		if border_switch == 1:
			break
	if border_switch == 0:
		outlier_list.append(pnt)

#Print the results:
print "Core points:"
for i in core_list:
	print i[0]
print "\nBorder points:"
for i in border_list:
	print i
print "\nOutlier points:"
for i in outlier_list:
	print i

#Write the output file:
fout = open("q5_out_core", "w")
fout.write("Core:\n")
for pnt in core_list:
	out_str = str(pnt[0][0]) + "\t" + str(pnt[0][1]) + "\t" + str(pnt[0][2]) + "\n"
	fout.write(out_str)
fout.write("Border:\n")
for pnt in border_list:
	out_str = str(pnt[0]) + "\t" + str(pnt[1]) + "\t" + str(pnt[2]) + "\n"
	fout.write(out_str)
fout.write("Outlier:\n")
for pnt in outlier_list:
	out_str = str(pnt[0]) + "\t" + str(pnt[1]) + "\t" + str(pnt[2]) + "\n"
	fout.write(out_str)
fout.close

print "Core List:"
for pnt in core_list:
	print pnt
print "Border List:"
for pnt in border_list:
	print pnt
print "noise list:"
for pnt in outlier_list:
	print pnt
