# f  = open('example.txt' , "r")
# # print(f.read())
# f.close()

# open_file = open('./test1.txt', 'r')
# # print(open_file.read())
# open_file.close()




# z = open("example1.txt" , "r")
# print(z.readlines())



# Append


# with open('./example1.txt', "a") as a:
#     a.write("hti sisjdhdbasbdaskldasdjasd\n")  # \n adds a new line

# with open('./example1.txt', "r") as a:
#     content = a.read()
#     print(content)



# with open('./example1.txt' , "w") as file:
#     file.write("This is Update text")
    
# with open('./example1.txt' , "r") as file:
#     print(file.read())




with open("example.txt" , "w" , encoding="utf-8") as file:
    file.write("Ahmed Raza Become Billionaire ❤❤")    

print("File written successfully!")


with open("example.txt" , "a" , encoding="utf-8") as file:
    file.write("\n Ahmed Win this World 💸💸💸")    

print("File written successfully!")


with open("example.txt" , "r" , encoding="utf-8") as file:
    content = file.read()
    print(content)
    
    
    
# Read and Write:


with open( "example1.txt", "r+", encoding="utf-8") as file:
    file.write("\n Ahmed Own this World 💸💸💸")    
    content = file.read()
    print(content)