-- models/marts/fct_activities_stats.sql
select
  type,
  date_trunc('month', start_date_local) as mois,
  count(*) as nb_activites,
  round(sum(distance_km)::numeric, 2) as total_km,
  round(sum(duration_min)::numeric, 1) as total_minutes,
  round(avg(vitesse_kmh)::numeric, 2) as vitesse_moyenne,
  round(avg(average_heartrate)::numeric, 1) as frequence_cardiaque_moyenne,
  round(avg(suffer_score)::numeric, 1) as suffer_score_moyen,
  round(avg(average_temp)::numeric, 1) as temperature_moyenne,
  sum(kudos_count) as total_kudos,
  sum(achievement_count) as total_achievements
from {{ ref('stg_activities') }}
group by 1, 2
order by 2 desc, 1
