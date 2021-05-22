SELECT name, SUBSTRING(ts, 12, 2) AS hour, MAX(high) AS high
FROM "sta9760-db"."03"
GROUP BY name, substring(ts, 12, 2)
ORDER BY name, substring(ts, 12, 2);
