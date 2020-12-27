# f_out = open('cleaned.txt','a',encoding="utf8")
# with open("Sohadata.txt",'r',encoding="utf8") as f:
#     for line in f:
#         line = line.replace('\n','')
#         line = line.replace('\r','')
#         line = line.replace('\r\n','')
#         line = line.replace('  ', '')
#         f_out.write(line)
#         f_out.write('\n')
# with open("VEdata2.txt",'r',encoding="utf8") as f:
#     for line in f:
#         f_out.write(line)
#         f_out.write('\n')
count = 0
with open("cleaned.txt",'r',encoding="utf8") as f:
    for line in f:
        print(line)
        if count == :3
            break
        count = count + 1