# The mysql login credentials
import json


def get_creds() -> dict:
    """Returns the credentials of the mysql database.
    """
    with open('./login/creds.json') as infile:
        creds = json.load(infile)
    return creds


def write_creds(passwd:str) -> None:
    """Writes the credentials to the save file.
    """
    creds = {
        'host': 'localhost',
        'user': 'root',
        'passwd': passwd,
        'db': 'hospital'
    }

    with open('./login/creds.json', 'w') as outfile:
        json.dump(creds, outfile)
