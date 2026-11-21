# Event attendance

Use Python 3 and a terminal in this folder. The first command creates attendance.sqlite3 in the working directory. Use a different working directory for each semester. Use a consistent event ID and member ID across commands.

```sh
python3 attendance.py report
python3 attendance.py volunteer kickoff member-01
python3 attendance.py checkin kickoff member-01
python3 attendance.py checkin workshop member-01
python3 attendance.py report
```

The example yields two visits and one distinct member. Signing up to volunteer alone counts toward staffing. Check the volunteer in when they arrive to count attendance. Repeating either action is safe. Keep your populated database local.
