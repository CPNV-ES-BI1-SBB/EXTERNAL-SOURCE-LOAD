-- stations: insert stations
CREATE TABLE stations (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    long FLOAT NOT NULL,
    lat FLOAT NOT NULL
);

-- departures: insert departures from stations
CREATE TABLE departures (
    id SERIAL PRIMARY KEY,
    station_id INT NOT NULL REFERENCES stations(id),
    destination_station_name TEXT NOT NULL,
    via_station_names TEXT,
    departure_time TIMESTAMP NOT NULL,
    platform TEXT,
    sector TEXT
);

-- trains: insert trains from departures
CREATE TABLE trains (
    id SERIAL PRIMARY KEY,
    departure_id INT NOT NULL REFERENCES departures(id),
    type VARCHAR(10),    -- match to 'g" in cff api
    line VARCHAR(10)   -- match to  "l" in cff api
);

