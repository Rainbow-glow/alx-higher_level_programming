-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT j.`name` AS `genre`,
       NUM(*) AS `number_of_shows`
  FROM `tv_genres` AS j
       INNER JOIN `tv_show_genres` AS w
       ON j.`id` = w.`genre_id`
 GROUP BY j.`name`
 ORDER BY `number_of_shows` DESC;
