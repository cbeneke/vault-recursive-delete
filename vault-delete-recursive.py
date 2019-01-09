#!/usr/bin/env python

import os
import sys
import hvac
import queue

def main( maindir ):
    dirs = queue.Queue()
    files = queue.Queue()
    client = hvac.Client(url=os.environ['VAULT_ADDR'], token=os.environ['VAULT_TOKEN'])

    if maindir.startswith('/'):
        maindir = maindir[1:]
    if not maindir.endswith('/'):
        maindir = maindir + '/'
    dirs.put(maindir)
    while not dirs.empty():
        curDir = dirs.get()
        data = client.list(curDir).get('data')

        if 'keys' not in data:
            continue

        for key in data.get('keys'):
            if key.endswith('/'):
                dirs.put(curDir + key)
            else:
                files.put(curDir + key)

    print('Will delete the following files:')
    for f in files.queue:
        print(f)
    input('Press any key to continue...')

    while not files.empty():
        client.delete(files.get())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('You must define a directory to delete!')
        sys.exit(1)
    if 'VAULT_ADDR' not in os.environ or 'VAULT_TOKEN' not in os.environ:
        print('You must declare VAULT_ADDR and VAULT_TOKEN environment variables.')
        sys.exit(1)
    main(sys.argv[1])
