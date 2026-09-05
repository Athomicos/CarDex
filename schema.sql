CREATE TABLE coches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    version TEXT NOT NULL,
    año_inicio INTEGER,
    año_fin INTEGER,
    potencia_cv INTEGER,
    motor TEXT,
    velocidad_maxima REAL,
    otros_specs TEXT
);

CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);


CREATE TABLE avistamientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    coche_id INTEGER NOT NULL,
    fecha DATETIME,
    ubicacion TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (coche_id) REFERENCES coches(id)
    UNIQUE (usuario_id, coche_id)
);

CREATE TABLE fotos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    avistamiento_id INTEGER NOT NULL,
    foto_path TEXT NOT NULL,
    FOREIGN KEY (avistamiento_id) REFERENCES avistamientos(id)
);

-- Add cars information
INSERT INTO coches (marca, modelo, version, año_inicio, año_fin, potencia_cv, motor, velocidad_maxima, otros_specs) VALUES
('Seat', 'León', '1.5 TSI FR', 2020, NULL, 150, '1.5L turbo gasolina', 216, 'FR es nivel deportivo, un escalón por debajo del Cupra'),
('Volkswagen', 'Golf 8', 'GTI', 2020, NULL, 245, '2.0 TSI turbo', 250, 'Primera GTI con perfiles de conducción digitales'),
('Renault', 'Clio V', 'TCe 100', 2019, NULL, 100, '1.0L turbo 3 cilindros', 187, 'Motor de solo 3 cilindros'),
('Peugeot', '208 II', 'GT Line', 2019, NULL, 130, '1.2L PureTech turbo 3 cilindros', 205, 'Existe versión eléctrica e-208 con carrocería idéntica'),
('Toyota', 'Corolla', 'Hybrid', 2019, NULL, 122, '1.8L híbrido no enchufable', 180, 'No confundir con híbrido enchufable, no existe esa versión'),
('BMW', 'Serie 3', '320d', 2019, NULL, 190, '2.0L diésel turbo', 235, 'Diésel: ojo con restricciones ZBE en fotos de ciudad'),
('Audi', 'A3 Sportback', '35 TFSI', 2020, NULL, 150, '1.5L turbo gasolina', 216, 'Comparte plataforma MQB con el Golf y el León'),
('Mercedes-Benz', 'Clase A', 'A200', 2018, NULL, 163, '1.3L turbo gasolina', 224, 'Motor codesarrollado con Renault'),
('Dacia', 'Sandero Stepway', 'TCe 100', 2020, NULL, 100, '1.0L turbo 3 cilindros', 169, 'Aspecto SUV pero tracción delantera normal, no 4x4'),
('Ford', 'Fiesta', 'ST-Line', 2017, 2023, 125, '1.0L EcoBoost turbo', 189, 'Descatalogado en 2023, ya no se fabrica'),
('Opel', 'Corsa F', 'GS Line', 2019, NULL, 100, '1.2 turbo gasolina', 191, 'Misma plataforma que el 208 (grupo Stellantis)'),
('Hyundai', 'Tucson', 'N Line', 2020, NULL, 150, '1.6 diésel turbo', 188, 'N Line es solo estético, no la versión "N" de alto rendimiento -- elegido motor diésel entre varios posibles'),
('Kia', 'Sportage', 'GT-Line', 2021, NULL, 150, '1.6 diésel turbo', 187, 'Comparte plataforma con el Tucson -- elegido motor diésel entre varios posibles'),
('Nissan', 'Qashqai', 'Tekna', 2021, NULL, 158, '1.3L mild-hybrid turbo', 203, 'Esta generación ya no ofrece diésel'),
('Fiat', '500', 'Dolcevita', 2007, 2024, 70, '1.0L mild-hybrid gasolina', 155, 'El 500e eléctrico es un modelo aparte, no una versión de este'),
('Citroën', 'C3', 'Shine', 2016, NULL, 110, '1.2 PureTech turbo', 188, 'Facelift en 2020 cambió el diseño'),
('Tesla', 'Model 3', 'Long Range', 2017, NULL, 498, 'Eléctrico doble motor', 233, 'Cifras muy distintas antes/después del rediseño "Highland" (2023-24) -- especifica año si importa'),
('Volvo', 'XC40', 'R-Design', 2018, NULL, 190, '2.0L turbo gasolina (T4)', 200, 'Existe XC40 Recharge 100% eléctrico con el mismo nombre'),
('Mini', 'Cooper', 'S', 2014, 2024, 178, '2.0L turbo gasolina', 235, 'Generación F5x, sustituida en 2024'),
('Skoda', 'Octavia', 'RS', 2020, NULL, 245, '2.0 TSI turbo gasolina', 250, 'Existe también RS diésel (200CV/232km/h) -- elegido gasolina como versión de referencia');