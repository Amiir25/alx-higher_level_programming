-- This SQL query displays the title of a tv show with
-- the id of its genre and NULL if it has no genre.
SELECT tv_shows.title,
COALESCE(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
