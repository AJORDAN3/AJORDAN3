-- Run against a fresh SQLite database.
CREATE TABLE attendance (
    event_id TEXT NOT NULL,
    member_id TEXT NOT NULL,
    PRIMARY KEY (event_id, member_id)
);

-- Two check-ins and a volunteer import overlap for the first event.
INSERT INTO attendance VALUES ('fall-social', 'member-a'), ('fall-social', 'member-b');
INSERT INTO attendance VALUES ('fall-social', 'member-a'), ('field-talk', 'member-a')
ON CONFLICT (event_id, member_id) DO NOTHING;

SELECT event_id, COUNT(*) AS attendees FROM attendance GROUP BY event_id;
SELECT COUNT(DISTINCT member_id) AS semester_reach FROM attendance;
