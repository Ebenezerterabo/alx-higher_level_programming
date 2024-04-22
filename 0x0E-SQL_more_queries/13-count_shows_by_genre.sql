-- This script lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
SELECT tg.name AS genre, COUNT(ts.genre_id) AS number_of_shows
FROM tv_genres AS tg
     JOIN tv_show_genres AS ts
     ON tg.id = ts.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
