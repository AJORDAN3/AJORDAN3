CREATE TABLE handoff (
    id INTEGER PRIMARY KEY,
    project TEXT NOT NULL,
    decision TEXT NOT NULL,
    next_step TEXT NOT NULL
);
INSERT INTO handoff (project, decision, next_step) VALUES
('demo', 'Track one attendance row per member and event.', 'Try a duplicate check-in.'),
('other', 'Use fictional records.', 'Write the sample input.'),
('demo', 'The duplicate test passed.', 'Add semester reach to the report.');

SELECT decision, next_step FROM handoff
WHERE project = 'demo' ORDER BY id DESC LIMIT 1;
