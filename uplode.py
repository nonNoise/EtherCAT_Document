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
print('Password:',sys.argv[2])

prc = pexpect.spawn("git push origin master")
prc.expect(r"^Username")
prc.sendline(sys.argv[0].strip())
prc.expect( pexpect.EOF )
print(prc.before)
prc.expect(r"^Password")
prc.sendline(sys.argv[1].strip())
prc.expect( pexpect.EOF )
print(prc.before)
