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