-- Database: ifrn_servidores

-- DROP DATABASE IF EXISTS ifrn_servidores;

CREATE DATABASE ifrn_servidores
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE "SERVIDORES"(
    "matricula" BOOLEAN NOT NULL,
    "id_categoria_servidores" SERIAL NOT NULL,
    "id_cargo_servidores" SERIAL NOT NULL,
    "id_setor_siape" SERIAL NOT NULL,
    "id_disciplina_ingresso" SERIAL NOT NULL,
    "id_setor_suap" SERIAL NOT NULL,
    "nome" VARCHAR(50) NOT NULL,
    "funcao" VARCHAR(30) NOT NULL,
    "jornada_trabalho" CHAR(20) NOT NULL,
    "telefones_institucionais" BIGINT NOT NULL,
    "curriculo_lattes" CHAR(150) NOT NULL,
    "campus" VARCHAR(20) NOT NULL,
    "url_foto_75x100" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "SERVIDORES" ADD PRIMARY KEY("matricula");
CREATE TABLE "CATEGORIA_SERVIDORES"(
    "id" SERIAL NOT NULL,
    "categoria" CHAR(20) NOT NULL
);
ALTER TABLE
    "CATEGORIA_SERVIDORES" ADD PRIMARY KEY("id");
CREATE TABLE "CAMPI"(
    "campus" VARCHAR(20) NOT NULL,
    "nome_completo" VARCHAR(50) NOT NULL
);
ALTER TABLE
    "CAMPI" ADD PRIMARY KEY("campus");
CREATE TABLE "DISCIPLINA_INGRESSO"(
    "id" SERIAL NOT NULL,
    "disciplina" VARCHAR(60) NOT NULL
);
ALTER TABLE
    "DISCIPLINA_INGRESSO" ADD PRIMARY KEY("id");
CREATE TABLE "SETORES_SIAPE"(
    "id" SERIAL NOT NULL,
    "nome_setor" CHAR(25) NOT NULL
);
ALTER TABLE
    "SETORES_SIAPE" ADD PRIMARY KEY("id");
CREATE TABLE "CARGO_SERVIDORES"(
    "id" SERIAL NOT NULL,
    "cargo" VARCHAR(30) NOT NULL
);
ALTER TABLE
    "CARGO_SERVIDORES" ADD PRIMARY KEY("id");

CREATE TABLE "SETORES_SUAP"(
    "id" SERIAL NOT NULL,
    "nome_setor" CHAR(35) NOT NULL
);
ALTER TABLE
    "SETORES_SUAP" ADD PRIMARY KEY("id");
ALTER TABLE
    "SERVIDORES" ADD CONSTRAINT "servidores_id_categoria_servidores_foreign" FOREIGN KEY("id_categoria_servidores") REFERENCES "CATEGORIA_SERVIDORES"("id");
ALTER TABLE
    "SERVIDORES" ADD CONSTRAINT "servidores_id_setor_suap_foreign" FOREIGN KEY("id_setor_suap") REFERENCES "SETOR_SUAP"("id");
ALTER TABLE
    "SERVIDORES" ADD CONSTRAINT "servidores_id_cargo_servidores_foreign" FOREIGN KEY("id_cargo_servidores") REFERENCES "CARGO_SERVIDORES"("id");
ALTER TABLE
    "SERVIDORES" ADD CONSTRAINT "servidores_campus_foreign" FOREIGN KEY("campus") REFERENCES "CAMPI"("campus");
ALTER TABLE
    "SERVIDORES" ADD CONSTRAINT "servidores_id_setor_siape_foreign" FOREIGN KEY("id_setor_siape") REFERENCES "SETOR_SIAPE"("id");
ALTER TABLE
    "SERVIDORES" ADD CONSTRAINT "servidores_id_disciplina_ingresso_foreign" FOREIGN KEY("id_disciplina_ingresso") REFERENCES "DISCIPLINA_INGRESSO"("id");