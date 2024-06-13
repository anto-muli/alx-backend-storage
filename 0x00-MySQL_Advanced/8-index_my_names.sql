-- Create index idx_name_first to the table names
-- and the 1st letter of name

CREATE INDEX idx_name_first
ON names(name(1));
