import pexpect
import argparse
import sys

print('Username:',sys.argv[1])
print('Password:',sys.argv[2])
print('Commit:',sys.argv[3])

prc = pexpect.spawn("make html")
prc.expect( pexpect.EOF )
print(prc.before)

prc = pexpect.spawn("git add -A")
prc.expect( pexpect.EOF )
#print(prc.before)

prc = pexpect.spawn("git commit -a -m \"" + sys.argv[3]+ "\"")
prc.expect( pexpect.EOF )
#print(prc.before)

prc = pexpect.spawn("git push origin master")
prc.expect("Username for 'https://github.com':")
prc.sendline(sys.argv[1])
prc.expect("Password for 'https://nonNoise@github.com':")
prc.sendline(sys.argv[2])
prc.expect(pexpect.EOF)
#print(prc.before)

