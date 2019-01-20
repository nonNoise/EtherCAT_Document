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
print(prc.before)
prc.sendline(sys.argv[0].strip())
prc.expect(r"^Password")
print(prc.before)
prc.sendline(sys.argv[1].strip())
