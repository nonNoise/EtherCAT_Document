import pexpect
import argparse
import sys

prc = pexpect.spawn("make html")
prc.expect( pexpect.EOF )

prc = pexpect.spawn("git add -A")
prc.expect( pexpect.EOF )

prc = pexpect.spawn("git commit -a -m \"test init\" ")
prc.expect( pexpect.EOF )

print('Username      : ', sys.argv[0])
print('Password      : ', sys.argv[1])

prc = pexpect.spawn("git push origin master")
prc.expect("Username for 'https://github.com':")
prc.sendline(sys.argv[0])

prc.expect("Password for 'https://nonNoise@github.com':")
prc.sendline(sys.argv[1])
prc.expect( pexpect.EOF )