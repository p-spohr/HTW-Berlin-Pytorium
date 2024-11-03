# %%

import sys
import os

# %%

print('This is main')
print(sys.version)

my_path = 'C:\\Users\\pat_h\\OneDrive\\p-spohr-repos\\HTW-Berlin-Pytorium\\module1\\code1.py'

if len(sys.argv) > 1 and sys.argv[1] == 'code1':
    os.system(f'powershell py {my_path}')
