-- #Realizando consulta de DOCENTES por DISCIPLINA DE INGRESSO ---- QUESTAO E)
   SELECT  servidores.matricula,
		      servidores.nome,
          categoria_servidores.categoria,
          disciplina_ingresso.disciplina,
          campi.campus
      COUNT(disciplina_ingresso.id) AS qtd_disciplina
      FROM servidores, categoria_servidores, disciplina_ingresso, campi
    WHERE categoria_servidores.categoria = 'docente'
INNER JOIN servidores ON servidores.id_disciplina_ingresso = disciplina_ingresso.id
  GROUP BY servidores.matricula,
		    categoria_servidores.categoria
        disciplina_ingresso.disciplina;
-- --------------------------------------