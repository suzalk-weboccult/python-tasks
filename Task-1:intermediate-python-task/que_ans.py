count_que=0
count_ans=0
with open("/home/wot-suzal/internship/intermediate_python_task_1/text_files/questions.txt","r") as file:
    for line in file:
        count_que+=1
with open("/home/wot-suzal/internship/intermediate_python_task_1/text_files/questions.txt","r") as file:
    for line in file:
        count_ans+=1

if count_que==count_ans:
    for i in range(1,count_que+1):
        with open("/home/wot-suzal/internship/intermediate_python_task_1/text_files/answers.txt","r") as file:
            for line in file:
                if str(i) in line:
                    with open('/home/wot-suzal/internship/intermediate_python_task_1/text_files/que_ans.txt', 'a') as f:
                        lst=line.split(". ")
                        f.writelines(lst[1])
                        with open("/home/wot-suzal/internship/intermediate_python_task_1/text_files/questions.txt","r") as file:
                            for line in file:
                                if str(i) in line:
                                    with open('/home/wot-suzal/internship/intermediate_python_task_1/text_files/que_ans.txt', 'a') as f:
                                        f.writelines(line)
else:
    print("please check the number of questions and answers in the input files")