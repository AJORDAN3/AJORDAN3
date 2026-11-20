-- Select today's active work from a fictional task board.
CREATE TABLE task (
    title TEXT NOT NULL, planned_on TEXT, due_on TEXT,
    status TEXT NOT NULL CHECK (status IN ('todo','doing','waiting','done'))
);
INSERT INTO task VALUES
('Prepare field notes','2026-06-08',NULL,'doing'),
('Submit abstract',NULL,'2026-06-07','todo'),
('Request venue quote',NULL,'2026-06-07','waiting'),
('Archive draft',NULL,'2026-06-07','done');

WITH today(day) AS (VALUES ('2026-06-08'))
SELECT title, status FROM task, today
WHERE status IN ('todo','doing') AND (planned_on = day OR due_on <= day)
ORDER BY (due_on < day) IS TRUE DESC, title;
