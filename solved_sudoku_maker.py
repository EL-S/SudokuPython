from random import randint

#build a cell by cell system next

def gen_sudoku():

    sudoku = [[0 for i in range(9)] for i in range(9)]

    waiting = True
    
    while waiting:
        
        possible = True
        
        for row_number in range(9):
            current_row = sudoku[row_number]
            #maybe if it returns impossible only zero out the current row
            for cell_value in range(1,10):
                c = 0
                attempted = []
                while possible:
                    c += 1
                    while possible:
                        if len(attempted) == 9:
                            possible = False 
                            
                        pos = randint(0,8)
                        if pos in attempted:
                            pass #already attempted
                        else:
                            attempted.append(pos)
                            break #not used before
                    if current_row[pos] == 0: #if there is no value
                        if row_number != 0:
                            #check all the above positions to make sure the number isn't there already

                            if pos < 3:
                                pos_check = [0,3] #0,1,2
                            elif pos < 6:
                                pos_check = [3,6] #3,4,5
                            else:
                                pos_check = [6,9] #6,7,8
                            
                            if row_number == 3 or row_number == 6: #do nothing this is fine
                                if check_above_row(cell_value,row_number,pos,sudoku):
                                    current_row[pos] = cell_value
                                    break
                                
                            elif row_number == 1 or row_number == 4 or row_number == 7: #check the above row in the cell doesn't already have the number
                                row_end_num = 2

                                current_cell_values = cell_check_func(row_end_num,row_number,sudoku,pos_check)
                                
                                #now check the number isn't in the cell

                                if cell_value in current_cell_values:
                                    #bad
                                    pass
                                else:
                                    #now do the above row check
                                    if check_above_row(cell_value,row_number,pos,sudoku):
                                        current_row[pos] = cell_value
                                        break
                                    
                            elif row_number == 2 or row_number == 5 or row_number == 8: #check the above 2 rows don't have 

                                row_end_num = 3

                                current_cell_values = cell_check_func(row_end_num,row_number,sudoku,pos_check)
                                
                                #now check the number isn't in the cell

                                if cell_value in current_cell_values:
                                    #bad
                                    pass
                                else:
                                    #now do the above row check
                                    
                                    if check_above_row(cell_value,row_number,pos,sudoku):
                                        current_row[pos] = cell_value
                                        break
                        else:
                            current_row[pos] = cell_value
                            break
        if possible == False:
            sudoku = [[0 for i in range(9)] for i in range(9)]
        else:
            waiting = False
    return sudoku

def cell_check_func(row_end_num,row_number,sudoku,pos_check):
    current_cell_values = []
    for i in range(1,row_end_num):
        above_row_number = row_number - i
        
        above_row = sudoku[above_row_number]
        for num in range(pos_check[0],pos_check[1]):
            current_cell_values.append(above_row[num])

    return current_cell_values
    

def check_above_row(cell_value,row_number,pos,sudoku):
    above_values = []
    for row_number_check in range(row_number):
        value = sudoku[row_number_check][pos]
        above_values.append(value)
    if cell_value in above_values:
        #repeat the loop
        return False
    else:
        return True

while True:
    sudoku = gen_sudoku()

    for row in sudoku:
        print(row)
    print("_____________________________________")
                    
            
            
        
