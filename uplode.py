import pexpect
import argparse
import sys

prc = pexpect.spawn("make html")
prc.expect( pexpect.EOF )
print(prc.before)

prc = pexpect.spawn("git add -A")
prc.expect( pexpect.EOF )
print(prc.before)

prc = pexpect.spawn("git commit -a -m \"test init\" ")
prc.expect( pexpect.EOF )
print(prc.before)

print('Username:',sys.argv[1])
print(len(sys.argv[1]))
print('Password:',sys.argv[2])
print(len(sys.argv[2]))

prc = pexpect.spawn("git push origin master")
prc.expect("Username for 'https://github.com':")
prc.sendline("nonNoise")
prc.expect("Password for 'https://nonNoise@github.com':")
prc.sendline(sys.argv[1].strip())
print(prc.before)
