#test_write_file

#import time

from functions.write_file import write_file

print("\nResult for calculator/lorem.txt:")
#go = time.time()
print(f'{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')
print("\nResult for pkg/morelorem.txt:")
print(f'{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')
print("\nResult for /tmp/temp.txt:")
print(f'{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}\n')
#time.sleep(5)
#halt = time.time()
#print(f"Elapsed: {halt - go:.2f} seconds")