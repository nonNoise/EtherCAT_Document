import pexpect
import argparse
import sys

print ('Username:'+sys.argv[1])
print ('Password:'+sys.argv[2])
print ('Commit:'+sys.argv[3])

command = "make html"
print(command)
prc = pexpect.spawn(command)
prc.expect( pexpect.EOF )
print(prc.before)

command = "git add -A"
print(command)
prc = pexpect.spawn(command)
prc.expect( pexpect.EOF )
#print(prc.before)
command = "git commit -a -m \"" + sys.argv[3]+ "\""
print(command)
prc = pexpect.spawn(command)
prc.expect( pexpect.EOF )
#print(prc.before)

command = "git push origin master"
print(command)
prc = pexpect.spawn(command)
prc.expect("Username for 'https://github.com':")
prc.sendline(sys.argv[1])
prc.expect("Password for 'https://nonNoise@github.com':")
prc.sendline(sys.argv[2])
prc.expect(pexpect.EOF)
print(prc.before)

print("Complete !!")
