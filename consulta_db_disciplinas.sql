  SELECT servidores.matricula,
		     servidores.nome,
         categoria_servidores.categoria,
         disciplina_ingresso.disciplina,
         campi.campus
      COUNT(disciplina_ingresso.id) AS qtd_disciplina
    FROM disciplina_ingresso.disciplina_ingresso 
INNER JOIN servidores.id_disciplina_ingresso ON servidores.id_disciplina_ingresso = campi.campus
  GROUP BY disciplina_ingresso.id
           campi.campus;