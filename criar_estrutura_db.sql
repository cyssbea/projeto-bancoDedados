CREATE TABLE "CATEGORIA_SERVIDORES"(
    "id" SERIAL NOT NULL,
    "categoria" CHAR(255) NOT NULL
);
ALTER TABLE
    "CATEGORIA_SERVIDORES" ADD PRIMARY KEY("id");
CREATE TABLE "CAMPI"(
    "campus" VARCHAR(255) NOT NULL,
    "nome_completo" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "CAMPI" ADD PRIMARY KEY("campus");
CREATE TABLE "DISCIPLINA_INGRESSO"(
    "id" SERIAL NOT NULL,
    "disciplina" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "DISCIPLINA_INGRESSO" ADD PRIMARY KEY("id");
CREATE TABLE "SETOR_SIAPE"(
    "id" SERIAL NOT NULL,
    "nome_setor" CHAR(255) NOT NULL
);
ALTER TABLE
    "SETOR_SIAPE" ADD PRIMARY KEY("id");
CREATE TABLE "CARGO_SERVIDORES"(
    "id" SERIAL NOT NULL,
    "cargo" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "CARGO_SERVIDORES" ADD PRIMARY KEY("id");
CREATE TABLE "SERVIDORES"(
    "matricula" BOOLEAN NOT NULL,
    "id_categoria_servidores" SERIAL NOT NULL,
    "id_cargo_servidores" SERIAL NOT NULL,
    "id_setor_siape" SERIAL NOT NULL,
    "id_disciplina_ingresso" SERIAL NOT NULL,
    "id_setor_suap" SERIAL NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "funcao" VARCHAR(255) NOT NULL,
    "jornada_trabalho" CHAR(255) NOT NULL,
    "telefones_institucionais" BIGINT NOT NULL,
    "curriculo_lattes" CHAR(255) NOT NULL,
    "campus" VARCHAR(255) NOT NULL,
    "url_foto_75x100" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "SERVIDORES" ADD PRIMARY KEY("matricula");
CREATE TABLE "SETOR_SUAP"(
    "id" SERIAL NOT NULL,
    "nome_setor" CHAR(255) NOT NULL
);
ALTER TABLE
    "SETOR_SUAP" ADD PRIMARY KEY("id");
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