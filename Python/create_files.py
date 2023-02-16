file_builder=open('mi_log.txt', 'w+')

for n in range(100):
   file_builder.write(f'I´m in line {n+1}\n')
#file_builder.write('Hey, I´m in a file!')
file_builder.close()