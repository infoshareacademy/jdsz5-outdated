CREATE TABLE station (
    id INTEGER PRIMARY KEY,
    name varchar,
    lat NUMERIC,
    long NUMERIC,
    dock_count integer,
    city varchar,
    installation_date varchar);

CREATE TABLE status (
    station_id INTEGER,
    bikes_available INTEGER,
    docks_available INTEGER,
    time varchar);

CREATE TABLE trip (
    id INTEGER PRIMARY KEY,
    duration INTEGER,
    start_date varchar,
    start_station_name varchar,
    start_station_id INTEGER,
    end_date varchar,
    end_station_name varchar,
    end_station_id INTEGER,
    bike_id INTEGER,
    subscription_type varchar,
    zip_code INTEGER);

CREATE TABLE weather (
    date varchar,
    max_temperature_f INTEGER,
    mean_temperature_f INTEGER,
    min_temperature_f INTEGER,
    max_dew_point_f INTEGER,
    mean_dew_point_f INTEGER,
    min_dew_point_f INTEGER,
    max_humidity INTEGER,
    mean_humidity INTEGER,
    min_humidity INTEGER,
    max_sea_level_pressure_inches numeric,
    mean_sea_level_pressure_inches NUMERIC,
    min_sea_level_pressure_inches NUMERIC,
    max_visibility_miles INTEGER,
    mean_visibility_miles INTEGER,
    min_visibility_miles INTEGER,
    max_wind_Speed_mph INTEGER,
    mean_wind_speed_mph INTEGER,
    max_gust_speed_mph INTEGER,
    precipitation_inches INTEGER,
    cloud_cover INTEGER,
    events varchar,
    wind_dir_degrees INTEGER,
    zip_code INTEGER);
   
   
   