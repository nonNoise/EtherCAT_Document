import pexpect
import argparse
import sys
import time

print ('Username: '+sys.argv[1])
print ('Password: '+sys.argv[2])
print ('Commit: '+sys.argv[3])

command = "make html"
print(command)
prc = pexpect.spawn(command)
prc.expect( pexpect.EOF )
print(prc.before)
time.sleep(1)

command = "git add -A"
print(command)
prc = pexpect.spawn(command)
prc.expect( pexpect.EOF )
#print(prc.before)
time.sleep(1)

command = "git commit -a -m \"" + sys.argv[3]+ "\""
print(command)
prc = pexpect.spawn(command)
prc.expect( pexpect.EOF )
print(prc.before)
time.sleep(1)

command = "git push origin master"
print(command)
prc = pexpect.spawn(command)
try:
	prc.expect("Username for 'https://github.com':")
	print(prc.before)
	prc.sendline(sys.argv[1])
	prc.expect("Password for 'https://"+sys.argv[1]+"@github.com':")
	print(prc.before)
	prc.sendline(sys.argv[2])
	prc.expect(pexpect.EOF)
except pexpect.EOF:	
	prc.expect(pexpect.EOF)
	
time.sleep(1)

print("Complete !!")
