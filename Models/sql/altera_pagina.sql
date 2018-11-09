update tabela
set autor = <dtml-sqlvar autorform type=string>,
p1 = <dtml-sqlvar areatexto type=string>,
titulo = <dtml-sqlvar titulo type=string>,
titulopag = <dtml-sqlvar titulopag type=string>
where dbid = <dtml-sqlvar titulos type=int>