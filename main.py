
from pyscript import document

def candidate_checker(e):
    club_members = ["ranee de guzman", "michael de leon", "ange del rosario", "milli meneses", "belle serdena"]

    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()
    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members

    messages = [
        f'Sorry {candidate}, your name is not on the list.',
        f'Congratulations {candidate}, you are now part of the marching band!'
    ]

    document.getElementById('result').innerHTML = messages[member_checker]


