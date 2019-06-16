import click
import requests

"""
    THIS PROGRAM WILL BE TESTED BY USING PUBLIC API CALLS
    FROM https://api.publicapis.org
    SINCE LATER ON, I WILL BE CALLING MY OWN API FOR THE BOTNET HOSTED ON MY SERVER
"""

# base URL of the test API
BASE_URL = 'https://api.publicapis.org'


@click.group()
def kingtaipan():
    """A CLI wrapper for the king_taipan botnet Command and Control server."""

@click.option('-a', '--no-auth', is_flag=True, help="List APIs with no required authentication")
@click.option('-n', '--name', help="search and list an API by name")
@click.option('-c', '--category', help="list APIs of specific type")
@kingtaipan.command()
#  listapis command checks if the no_auth flag has been enabled
def listapis(no_auth:bool,name:str,category:str):
    """List the selected APIs for King Taipan."""
    # params for the request
    params = {
        # title as the param for this API but for my API I will be returning a "name" property key
        'title': name,
        'category': category
    }

    if no_auth:
        params['auth'] = 'null'
    response = requests.get(url=f'{BASE_URL}/entries', params=params)
    if response.status_code is 200:
        for i, entry in enumerate(response.json()['entries']):
            pretty_entry = '\n'.join(f'{k} -- {v}' for k, v in entry.items())
            print(f'NUMBER: {i + 1}\n{pretty_entry}\n')
    else:
        print(f'Fetching available APIs failed with error message: {response.text}')

@kingtaipan.command()
def listcategories():
    """List all king_taipan's API categories."""
    response = requests.get(url=f'{BASE_URL}/categories')
    if response.status_code is 200:
        print('\n'.join(response.json()))
    else:
        print(f'Could not get API categories, error response: {response.text}')




if __name__ == "__main__":
    kingtaipan(prog_name='kingtaipan')