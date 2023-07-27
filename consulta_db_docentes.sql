-- #Realizando consulta de DOCENTES por DISCIPLINA DE INGRESSO
   SELECT servidores.matricula,
		   servidores.nome,
           categoria_servidores.categoria,
           disciplina_ingresso.disciplina,
           campi.campus
      COUNT(disciplina_ingresso.id) AS qtd_disciplina
      FROM servidores.servidores, categoria_servidores.categoria_servidores, disciplina_ingresso.disciplina_ingresso, campi.campi
    WHERE ategoria_servidores.categoria = 'docente'
INNER JOIN servidores.id_disciplina_ingresso ON servidores.id_disciplina_ingresso = disciplina_ingresso.id
  GROUP BY servidores.matricula,
		       categoria_servidores.categoria;
-- --------------------------------------