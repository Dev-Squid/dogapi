-- Define the trigger function
CREATE OR REPLACE FUNCTION increment_vote_count()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE comments
    SET vote_count = vote_count + 1
    WHERE comment_id = NEW.comment_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Define the trigger
CREATE TRIGGER increment_vote_count_trigger
AFTER INSERT ON votes
FOR EACH ROW
EXECUTE FUNCTION increment_vote_count();