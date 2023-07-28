-- #Questao F) Consulta de Disciplina ingresso e quantidade por Campus  
  SELECT servidores.matricula,
		    servidores.nome,
        categoria_servidores.categoria,
        disciplina_ingresso.disciplina,
        campi.campus
      COUNT(disciplina_ingresso.id) AS qtd_disciplina
    FROM disciplina_ingresso 
INNER JOIN servidores ON servidores.id_disciplina_ingresso = disciplina_ingresso.id
INNER JOIN servidores ON servidores.campus = campi.campus
  GROUP BY disciplina_ingresso.id
        campi.campus;
-----------------------------------------------------------
