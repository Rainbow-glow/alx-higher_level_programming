-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Displays NULL for shows without genres.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT c.`title`, j.`genre_id`
  FROM `tv_shows` AS c
       LEFT JOIN `tv_show_genres` AS j
       ON c.`id` = j.`show_id`
 ORDER BY c.`title`, j.`genre_id`;
