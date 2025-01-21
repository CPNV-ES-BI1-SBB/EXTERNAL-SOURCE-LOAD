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
    departure_time TIMESTAMP NOT NULL,
    platform TEXT,
    sector TEXT
);

-- trains: insert trains from departures
CREATE TABLE trains (
    id SERIAL PRIMARY KEY,
    departure_id INT NOT NULL REFERENCES departures(id),
    train_type TEXT,    -- match to 'g" in cff api
    train_line TEXT   -- match to  "l" in cff api
);
