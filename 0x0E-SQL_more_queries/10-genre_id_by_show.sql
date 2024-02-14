-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT c.`title`, j.`genre_id`
  FROM `tv_shows` AS c
        INNER JOIN `tv_show_genres` AS j
	ON c.`id` = j.`show_id`
 ORDER BY c.`title`, j.`genre_id`;
