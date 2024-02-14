-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT j.`name`
  FROM `tv_genres` AS j
       INNER JOIN `tv_show_genres` AS c
       ON j.`id` = c.`genre_id`

       INNER JOIN `tv_shows` AS w
       ON w.`id` = c.`show_id`
       WHERE w.`title` = "Dexter"
 ORDER BY j.`name`;
