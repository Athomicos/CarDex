CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    version TEXT NOT NULL,
    year_start INTEGER,
    year_end INTEGER,
    horsepower INTEGER,
    engine TEXT,
    top_speed REAL,
    other_specs TEXT
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT UNIQUE,
    password_hash TEXT NOT NULL
);

CREATE TABLE sightings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    date DATETIME,
    location TEXT,
    photo_path TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (car_id) REFERENCES cars(id),
    UNIQUE (user_id, car_id)
);

-- Add cars information
INSERT INTO cars (brand, model, version, year_start, year_end, horsepower, engine, top_speed, other_specs) VALUES
('Seat', 'León', '1.5 TSI FR', 2020, NULL, 150, '1.5L turbo gasoline', 216, 'FR is the sporty trim, one step below Cupra'),
('Volkswagen', 'Golf 8', 'GTI', 2020, NULL, 245, '2.0 TSI turbo', 250, 'First GTI with digital driving profiles'),
('Renault', 'Clio V', 'TCe 100', 2019, NULL, 100, '1.0L turbo 3-cyl', 187, '3-cylinder engine only'),
('Peugeot', '208 II', 'GT Line', 2019, NULL, 130, '1.2L PureTech turbo 3-cyl', 205, 'Electric e-208 shares the same body'),
('Toyota', 'Corolla', 'Hybrid', 2019, NULL, 122, '1.8L hybrid, not plug-in', 180, 'No plug-in variant exists for this generation'),
('BMW', 'Serie 3', '320d', 2019, NULL, 190, '2.0L diesel turbo', 235, 'Diesel: watch for low-emission zone restrictions in city photos'),
('Audi', 'A3 Sportback', '35 TFSI', 2020, NULL, 150, '1.5L turbo gasoline', 216, 'Shares MQB platform with Golf and León'),
('Mercedes-Benz', 'Clase A', 'A200', 2018, NULL, 163, '1.3L turbo gasoline', 224, 'Engine co-developed with Renault'),
('Dacia', 'Sandero Stepway', 'TCe 100', 2020, NULL, 100, '1.0L turbo 3-cyl', 169, 'SUV look but standard FWD, not 4x4'),
('Ford', 'Fiesta', 'ST-Line', 2017, 2023, 125, '1.0L EcoBoost turbo', 189, 'Discontinued in 2023, no longer produced'),
('Opel', 'Corsa F', 'GS Line', 2019, NULL, 100, '1.2 turbo gasoline', 191, 'Same platform as the 208 (Stellantis group)'),
('Hyundai', 'Tucson', 'N Line', 2020, NULL, 150, '1.6 diesel turbo', 188, 'N Line is cosmetic only, not the high-performance "N"; diesel chosen among several options'),
('Kia', 'Sportage', 'GT-Line', 2021, NULL, 150, '1.6 diesel turbo', 187, 'Shares platform with Tucson; diesel chosen among several options'),
('Nissan', 'Qashqai', 'Tekna', 2021, NULL, 158, '1.3L mild-hybrid turbo', 203, 'This generation no longer offers diesel'),
('Fiat', '500', 'Dolcevita', 2007, 2024, 70, '1.0L mild-hybrid gasoline', 155, 'The 500e electric is a separate model, not a trim of this one'),
('Citroën', 'C3', 'Shine', 2016, NULL, 110, '1.2 PureTech turbo', 188, 'Facelift in 2020 changed the design'),
('Tesla', 'Model 3', 'Long Range', 2017, NULL, 498, 'Electric dual motor', 233, 'Figures changed significantly after the "Highland" refresh (2023-24)'),
('Volvo', 'XC40', 'R-Design', 2018, NULL, 190, '2.0L turbo gasoline (T4)', 200, 'XC40 Recharge fully electric shares the same name'),
('Mini', 'Cooper', 'S', 2014, 2024, 178, '2.0L turbo gasoline', 235, 'F5x generation, replaced in 2024'),
('Skoda', 'Octavia', 'RS', 2020, NULL, 245, '2.0 TSI turbo gasoline', 250, 'RS diesel (200hp/232km/h) also exists -- gasoline chosen as reference');

INSERT INTO cars (brand, model, version, year_start, year_end, horsepower, engine, top_speed, other_specs) VALUES
('Seat', 'Alhambra', '2.0 TDI Style', 2015, NULL, 150, '2.0L diesel turbo', 199.0, 'Popular 7-seat MPV, shares platform with VW Sharan');