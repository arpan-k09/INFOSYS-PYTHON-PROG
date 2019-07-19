#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    pl = len(patient_medical_speciality_list)

    cop = 0
    coe = 0
    coo = 0

    for index in range(1,pl,2):
        if patient_medical_speciality_list[index] == "P":
            cop = cop + 1
        elif patient_medical_speciality_list[index] == "O":
            coo = coo + 1
        elif patient_medical_speciality_list[index] == "E":
            coe = coe + 1
        else:
            break

    if (cop > coo) and (cop > coe):
        speciality = medical_speciality["P"]
    elif (coo > cop) and (coo > coe):
        speciality = medical_speciality["O"]
    elif (coe > cop) and (coe > coo):
        speciality = medical_speciality["E"]
    else:
        speciality = "Same entry"


    return speciality







#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)