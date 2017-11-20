from json import dump
from mastodon import Mastodon
from sys import stderr, stdout

def json_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError(obj)

mastodon = Mastodon(client_id='clientcred.secret',
                    access_token='usercred.secret',
                    api_base_url='https://cybre.space',
                    ratelimit_method='pace')

notifications = mastodon.notifications(limit=40)
stdout.write('[\n')
first = True

while True:
    max_id = None

    stderr.write('writing {} notifications\n'.format(len(notifications)))

    for notification in notifications:
        if not first:
            stdout.write(',\n')
        
        first = False

        dump(notification, stdout, default=json_handler, indent=1)

        stderr.write('searching for next page block\n')

        if '_pagination_next' in notification:
            stderr.write('found next page block\n')
            max_id = notification['_pagination_next']['max_id']

    if max_id == None:
        stderr.write('done')
        stdout.write(']\n')
        break

    stderr.write('next fetch\n')
    notifications = mastodon.notifications(max_id=max_id, limit=40)

