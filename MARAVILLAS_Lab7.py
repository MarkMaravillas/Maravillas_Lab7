#VARIABLES
NAME = input("What is your Name?: ")
SECTION = input("What is your Section?: ")
PRELIM_GRADE = float(input("ENTER PRELIM-GRADE?:"))

if PRELIM_GRADE < 40 or PRELIM_GRADE > 100:
    print("INVALID: WRONG PRELIM GRADE")
    exit
else:
    
 MID_GRADE = float(input("ENTER MIDTERM-GRADE?:"))
if MID_GRADE < 40 or MID_GRADE > 100:
    print("INVALID: WRONG MIDTERM GRADE")
    exit
else:
    
 FINAL_GRADE = float(input("ENTER FINALS-GRADE?:"))
if FINAL_GRADE < 40 or MID_GRADE > 100:
    print("INVALID: WRONG FINALS GRADE")
else:

#FORMULA
 OVERALL_FINALS = round((PRELIM_GRADE * .3333) + (MID_GRADE * .3333) + (FINAL_GRADE * .3333), 0)
    
#OUTPUT
print("Name:" + NAME)  
print("Section:" + SECTION) 
print("PRELIM Grade:" , PRELIM_GRADE)    
print("MIDTERM Grade:" , MID_GRADE)
print("FINALS Grade:" , FINAL_GRADE) 

#FINALS CONDITION
if OVERALL_FINALS < 75:
    print("GPA:", "5.00", "FAILED", OVERALL_FINALS) 
    
elif OVERALL_FINALS >= 75 and OVERALL_FINALS <= 77:
    print("GPA:", "3.00", "PASSED", OVERALL_FINALS)
    
elif OVERALL_FINALS >= 78 and OVERALL_FINALS <= 80:
    print("GPA:", "2.75", "FAIR", OVERALL_FINALS)

elif OVERALL_FINALS >= 81 and OVERALL_FINALS <= 83:
    print("GPA:", "2.50", "FAIRLY SATISFACTORY", OVERALL_FINALS)

elif OVERALL_FINALS >=  84 and OVERALL_FINALS <= 86:
    print("GPA:", "2.25", "SATISFACTORY", OVERALL_FINALS)
    
elif OVERALL_FINALS >= 87 and OVERALL_FINALS <= 89:
    print("GPA:", "2.00", "GOOD", OVERALL_FINALS)

elif OVERALL_FINALS >= 90 and OVERALL_FINALS <= 92:
    print("GPA:", "1.75", "VERY GOOD", OVERALL_FINALS)  

elif OVERALL_FINALS >= 93 and OVERALL_FINALS <= 95:
    print("GPA:", "1.50", "SUPERIOR", OVERALL_FINALS)   

elif OVERALL_FINALS >= 96 and OVERALL_FINALS <= 98:
    print("GPA:", "1.25", "OUTSTANDING", OVERALL_FINALS)       
    
elif OVERALL_FINALS >= 99 and OVERALL_FINALS >=100:
    print("GPA:", "1.00", "EXCELLENT", OVERALL_FINALS)             
        
            