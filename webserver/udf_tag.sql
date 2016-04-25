CREATE OR REPLACE FUNCTION tag_func() RETURNS TRIGGER AS $tag_update$
    DECLARE
        t json;
    BEGIN
        -- Loop through tags in inserted row
        FOR t IN SELECT * FROM json_array_elements(NEW.meta->'tags')
        LOOP
            -- Check if new tag exists
            IF EXISTS (SELECT tag FROM MetaTags WHERE tag = CAST(t AS TEXT)) THEN
                -- Update count
                UPDATE MetaTags SET count = count + 1 WHERE tag = CAST(t AS TEXT);
            ELSE 
                RAISE NOTICE 'Inserting into MetaTags';
                INSERT INTO MetaTags (tag) VALUES (CAST(t AS TEXT));
            END IF;
        END LOOP;
        RETURN NEW;
    END;
$tag_update$ LANGUAGE plpgsql;
