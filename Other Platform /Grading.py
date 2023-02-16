def gradingStudents(grades):
    data=[]
    for i in range(len(grades)):
        if((grades[i]>=38) & (grades[i]%5>=3)):
            data+=[grades[i]+(5-grades[i]%5)]
        else:
            data+=[grades[i]]
    return (data)