from getpass import getpass
from mastodon import Mastodon

email = input('Email: ')
password = getpass('Password: ')

mastodon = Mastodon(client_id='clientcred.secret', api_base_url='https://cybre.space')
mastodon.log_in(email, password, to_file='usercred.secret')

