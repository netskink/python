import subprocess

print('demo of subprocess')

command = 'export | grep HOME'
result = subprocess.run(['bash', '-c', command], capture_output=True, text=True)

print(f'result: {result.stdout}')
