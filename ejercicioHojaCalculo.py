from __future__ import division
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

""" 
	Programming exercise
	Ing. Barbara Hernandez
"""



""" 
	Initialize the variable spreadSheet where it will contain the information
	of the file inputfile
"""
spreadSheet = ""
M = []

"""
	Function "read_file" that reads the file with the operations of each cell
"""
def read_file():
	try:
		inputfile = open(sys.argv[1],"r")
		spreadSheet = inputfile.read()
		inputfile.close()
		calculate_cells(spreadSheet)
	except:
		print "Error: No se puede abrir el archivo",sys.argv[1]

"""
	"Calculate_cells" function that calculates the value of each cell
	after performing the corresponding operation

	Input variables:
		spreadSheet: string that contains the file information
					 of entry.
"""
def calculate_cells(spreadSheet):

	i = 0
	k = 0
	F = []
	calculate = []
	n = ''

	# Cycle through the cells of the calculation sheet
	while(i < len(spreadSheet)):
		if(i != len(spreadSheet) - 1):
			if(spreadSheet[i] != "\n"):

				if(spreadSheet[i] != "," and spreadSheet[i] != " "):
					
					if(spreadSheet[i+1] != " " and spreadSheet[i+1] != "," and spreadSheet[i+1] != "\n"):
						n = n + spreadSheet[i]
					else:
						if(n != ''):
							n = n + spreadSheet[i]
							calculate.append(n)	
						else:
							calculate.append(spreadSheet[i])
						n = ''

				elif(spreadSheet[i] == ","):
					result = calculator(calculate,F)
					F.append(result)
					calculate = []

			else:
				result = calculator(calculate,F)
				F.append(result)
				M.append(F)
				F = []
				calculate = []

		else:
			calculate.append(spreadSheet[i])
			result = calculator(calculate,F)
			F.append(result)
			M.append(F)

		i = i +1
	write_file()

""" a cell 
				   (operands and operator)
		F: List containing the row that is currently being calculated

	Returns:
		The result corresponding to the operation of the cell
"""
def calculator(calculate,F):
	
	result = 0
	if(len(calculate)>1):
		operand_1 = value_operand(calculate[0],F)
		operand_2 = value_operand(calculate[1],F)
		
		if calculate[2] == "+":
			result = operand_1 + operand_2
		elif calculate[2] == "-":
			result = operand_1 - operand_2
		elif calculate[2] == "*":
			result = operand_1 * operand_2
		else:
			try:
				result = operand_1 / operand_2
			except ZeroDivisionError as detail:
				print 'Error', detail
				sys.exit()

	else:
		value = value_operand(calculate[0],F)
		result = value
	
	return result

"""
	Function "value_operand" that returns the value of an operator of the cell

	Input variables:
		operand: operating from the cell
		F: List containing the row that is currently being calculated
	Returns:
		The value of each operand
"""
def value_operand(operand,F):
	value = 0.0
	try:
		value = int(operand)
	except:
		try:
			value = float(operand)
		except:
			colum = ord(operand[0]) -65

			try:
				if int(operand[1])-1 == len(M):
					value = F[colum]
				else:
					value = M[int(operand[1])-1][colum]
			except:
				print "Error: En la referencia a la celda",operand,"esta no existe"
				sys.exit()

	return value

"""
	Function "write_file" that writes in the indicated file the resulting matrix
"""
def write_file():
	try:
		outputfile = open(sys.argv[2],"w")
		i = 0
		while(i < len(M)):
			j = 0
			while j < len(M[i]):
				outputfile.write(str(M[i][j]))
				if(j != len(M[i]) - 1):
					outputfile.write(",")
				j = j + 1
			outputfile.write("\n")
			i = i +1
		outputfile.close()
	except:
		print "Error: No se puede escribir en el archivo",sys.argv[2]


read_file()