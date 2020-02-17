# f = open(r'C:\Users\Матвей\PycharmProjects\first_attempt\source\example.txt','r')
# print(f.read)
# print(f.read(5))
#
# for item in f:
#     print(item)
#
# f.close()

# with open('source/example.txt','r') as f:
#     print(f.read())

with open('source/example.txt','w') as f:
    f.write('Hello world!')
with open('source/example.txt','r+') as f:
    print(f.read())
    f.write('Hello world!')