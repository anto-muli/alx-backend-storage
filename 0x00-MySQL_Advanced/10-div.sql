-- Create function SafeDiv that divides (and returns)
-- the 1st by the 2nd number or returns 0
-- if the 2nd number is equal to 0.

DELIMITER $$
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END
$$
DELIMITER ;
