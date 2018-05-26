# clanwars
The Clan War Data Tool

## Notes
+ Make sure to use the included python environment (KOA-Django-Env)
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
