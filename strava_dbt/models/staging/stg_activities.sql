-- models/staging/stg_activities.sql

select
  id as activity_id,
  name,
  start_date_local::timestamp,
  distance / 1000.0 as distance_km,
  moving_time / 60.0 as duration_min,
  average_speed * 3.6 as vitesse_kmh,
  type,
  sport_type,
  total_elevation_gain,
  has_heartrate,
  average_heartrate,
  max_heartrate,
  kilojoules,
  suffer_score,
  achievement_count,
  kudos_count,
  average_temp,
  elapsed_time / 60.0 as elapsed_minutes
from public.activities
