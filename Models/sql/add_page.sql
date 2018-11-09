INSERT INTO tabela(titulo, titulopag, p1, autor)
VALUES(
<dtml-sqlvar titulo_geral type=string>,
<dtml-sqlvar titulo_pagina type=string>,
<dtml-sqlvar area_texto type=string>,
<dtml-sqlvar autor_pagina type=string>)
