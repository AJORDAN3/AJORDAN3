"""Local volunteer and attendance register. Requires Python 3."""
import argparse
import sqlite3


def identifier(value):
    cleaned = value.strip().casefold()
    if not cleaned:
        raise argparse.ArgumentTypeError("Enter a nonempty identifier.")
    return cleaned


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    for name in ("volunteer", "checkin"):
        command = commands.add_parser(name)
        command.add_argument("event", type=identifier)
        command.add_argument("member", type=identifier)
    commands.add_parser("report")
    args = parser.parse_args()
    with sqlite3.connect("attendance.sqlite3") as db:
        db.execute("""CREATE TABLE IF NOT EXISTS activity (
            event TEXT NOT NULL, member TEXT NOT NULL, action TEXT NOT NULL,
            PRIMARY KEY (event, member, action))""")
        if args.action != "report":
            cursor = db.execute(
                "INSERT OR IGNORE INTO activity VALUES (?, ?, ?)",
                (args.event, args.member, args.action),
            )
            print("Recorded." if cursor.rowcount else "Already recorded.")
            return
        print("Event | Volunteers | Attendance")
        for event, volunteers, visits in db.execute("""
            SELECT event, SUM(action='volunteer'), SUM(action='checkin')
            FROM activity GROUP BY event ORDER BY event"""):
            print(f"{event} | {volunteers} | {visits}")
        visits, members = db.execute("""
            SELECT COUNT(*), COUNT(DISTINCT member)
            FROM activity WHERE action='checkin'""").fetchone()
        print(f"Visits: {visits} | Distinct members: {members}")


if __name__ == "__main__":
    main()
