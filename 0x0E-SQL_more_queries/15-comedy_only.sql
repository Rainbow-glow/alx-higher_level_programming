-- Lists all comedy shows in the database hbtn_0d_tvshows.
-- Records are ordered by descending show title.
SELECT w.`title`
  FROM `tv_shows` AS w
       INNER JOIN `tv_show_genres` AS c
       ON w.`id` = c.`show_id`

       INNER JOIN `tv_genres` AS j
       ON j.`id` = c.`genre_id`
       WHERE j.`name` = "Comedy"
 ORDER BY w.`title`;
