-- #Realizando consulta de Campi do IFRN ---- QUESTAO D)
   SELECT campi.campus AS sigla,
		   categoria_servidores.categoria,
		   servidores.matricula,
		   COUNT(servidores.id_categoria_servidores) AS qtd_categoria_serv
      FROM servidores
INNER JOIN categoria_servidores ON servidores.id_categoria_servidores = categoria_servidores.id_categoria_servidores
INNER JOIN servidores ON servidores.campus = campi.campus
   GROUP BY servidores.matricula,
		campi.campus,
		categoria_servidores.categoria;
-- --------------------------------------