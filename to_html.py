from json import load
from sys import stdin, stdout

toots = load(stdin)

stdout.write('<!DOCTYPE html><html><head><meta charset="utf-8"><title>HTML</title></head><body>')

for toot in toots:
    stdout.write('<h2>{} {}</h2>'.format(toot['account']['username'], toot['created_at']))
    stdout.write(toot['content'])

stdout.write('</body></html>\n')

