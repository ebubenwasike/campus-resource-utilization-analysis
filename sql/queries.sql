-- 1. Total usage by location
SELECT location, COUNT(*) AS total_usage
FROM cleaned_usage
GROUP BY location
ORDER BY total_usage DESC;

-- 2. Usage by time of day
SELECT time_of_day, COUNT(*) AS usage_count
FROM cleaned_usage
GROUP BY time_of_day
ORDER BY usage_count DESC;

-- 3. Peak vs non-peak usage
SELECT is_peak, COUNT(*) AS usage_count
FROM cleaned_usage
GROUP BY is_peak;

-- 4. Average duration by location
SELECT location, AVG(duration) AS avg_duration
FROM cleaned_usage
GROUP BY location
ORDER BY avg_duration DESC;

-- 5. Busiest hour of the day
SELECT hour, COUNT(*) AS usage_count
FROM cleaned_usage
GROUP BY hour
ORDER BY usage_count DESC;
