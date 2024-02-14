-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT w.`title`, j.`name`
  FROM `tv_shows` AS w
       LEFT JOIN `tv_show_genres` AS c
       ON w.`id` = c.`show_id`

       LEFT JOIN `tv_genres` AS j
       ON c.`genre_id` = j.`id`
 ORDER BY w.`title`, j.`name`;
