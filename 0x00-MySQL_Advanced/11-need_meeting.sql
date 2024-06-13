-- Creates a view titled need_meeting 2 lists all students
-- that have a score below 80 (strict)
-- and no last_meeting or > than 1 month.

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students 
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));