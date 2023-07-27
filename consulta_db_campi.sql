-- #Realizando consulta de Campi do IFRN
   SELECT campi.* AS sigla,
		   categoria_servidores.categoria,
		   servidores.matricula,
		   COUNT(servidores.id_categoria_servidores) AS qtd_categoria_serv
      FROM servidores.servidores
INNER JOIN servidores.campus ON servidores.campus = campi.campus
   GROUP BY servidores.campus,
		campi.campus;
-- --------------------------------------
