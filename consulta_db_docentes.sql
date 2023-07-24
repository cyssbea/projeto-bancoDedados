-- #Realizando consulta de DOCENTES por DISCIPLINA DE INGRESSO
   SELECT servidores.matricula,
		   servidores.nome,
           categoria_servidores.categoria,
           disciplina_ingresso.disciplina
      FROM servidores.servidores, categoria_servidores.categoria_servidores, disciplina_ingresso.disciplina_ingresso
    WHERE categoria_servidores.categoria = 'docente'
    AND servidores.id_disciplina_ingresso = disciplina_ingresso.id
    --#INNER JOIN categoria_servidores.categoria ON categoria_servidores.categoria = 'docente'
    --#INNER JOIN servidores.id_disciplina_ingresso ON servidores.id_disciplina_ingresso = disciplina_ingresso.id
  GROUP BY servidores.matricula,
		       categoria_servidores.categoria;
-- --------------------------------------