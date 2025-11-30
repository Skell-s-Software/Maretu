--
-- Archivo: DEBUG_USUARIOS.sql
-- Propósito: Crear la tabla 'debug' con datos similares a un entorno real.
--

-- 1. Comando para ELIMINAR la tabla si ya existe.
DROP TABLE IF EXISTS debug;

-- 2. Comando para CREAR la tabla 'debug'.
CREATE TABLE debug (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    rol VARCHAR(50) DEFAULT 'USUARIO',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Comandos para INSERTAR los datos de prueba.
INSERT INTO debug (nombre, email, activo, rol) VALUES 
('Alice Johnson', 'alice.j@ejemplo.com', TRUE, 'ADMIN');

INSERT INTO debug (nombre, email, activo, rol) VALUES 
('Bob Smith', 'bob.s@ejemplo.com', TRUE, 'EDITOR');

INSERT INTO debug (nombre, email, activo, rol) VALUES 
('Charlie Brown', 'charlie.b@ejemplo.com', FALSE, 'USUARIO');

INSERT INTO debug (nombre, email, activo, rol) VALUES 
('Diana Prince', 'diana.p@ejemplo.com', TRUE, 'USUARIO');