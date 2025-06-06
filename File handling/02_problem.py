#A python script to write multiplication tables in a folder into different files

def generate_table(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/tables_{n}.txt","w") as f:
        f.write(table) 

#this will create three files in tables folder and appends table on respective files
for i in range(2 , 5):
    generate_table(i)