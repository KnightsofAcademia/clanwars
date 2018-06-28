# clanwars
The Clan War Data Tool

## Install and run
1. Python 3.6.5 (or latest release) using whatever method for whatever OS
2. Fork and clone the repo. Make sure there are no spaces or special characters in the full path
3. Look for `.env.example` file, make a copy and rename it to `.env`. Open using a text editor and put in your own userID and API key from Habitica
4. Create a virtual environment and activate it. Make sure there are no spaces or special characters in the full path
5. Install pip (inside venv)
```bash
    python -m pip install --upgrade pip
```
6. Navigate to the directory which has the manage.py file in it (inside venv)
7. Install requirements (inside venv)
```bash
    pip install -r requirements.txt
```
8. Update the database
```bash
    python manage.py migrate
```
9. Run the test server
```bash
    python manage.py runserver
```
10. Open a browser to `127.0.0.1:8000`

## Notes
+ Bash python command may be python3 depending on OS
+ The (pseudo-code) algorithm 
```python
    def get_clan_participation(clan, challenge):
        clan_members_participation = 0
        clan_members_in_challenge = 0
        for user in clan:
            if user in challenge:
                clan_members_participation += user.participation
                clan_members_in_challenge += 1
        return clan_members_participation / clan_members_in_challenge        
```



