# hackaton_zyan_kitkat
[Portada de power point+mostrar equipo+planning]
Introduccion de proyecto funcionamiento

En nuestro proyecto hemos diseñado un termómetro social llamado Zyan, en honor a la cultura que se tiene en BBVA alrededor del color azul. Zyan es un procesador de lenguaje natural y con la información extraída en esta ocasión de Twitter acerca de lo que opina la sociedad sobre el BBVA y sus acciones frente a la Covid Zyan va a ayudarnos a tomar medidas rápidas e inmediatas requeridas por la sociedad actualmente y también para cuando el BBVA realice su informe anual en este 2020, pues hemos diseñado que los datos se representen gráficamente y se puedan customizar las variables que se quieran representar. (40 seg)

[página de aws donde está alojado el bucket con las credenciales y nombre del proyecto]
Todo lo hemos conectado con AWS -> como pueden ver en lo que les muestro
y es un proceso completamente automático -> corriendo todo este script (20 seg)

Consideramos que para la efectiva escucha social Zyan necesita basarse en una buena recogida de datos la cual tenemos a nuestro alcance garcias a internet y Amazon Web Services nos proporciona muchas herramientas para esto. Incluso podemos llegar a hacer que Zyan aprenda con esta buena base a través de Machine Learning con la data extraída. (15 seg)

[Script de Jupyter -> hacer scrowl sobre algunos comentarios #]
Para tener una buena data con la que Zyan pueda darnos un análisis de lo que sucede en este momento, hemos considerado muchos parámetros como:
el idioma, todos los sinónimos de BBVA, sinónimos y referentes de temática COVID, clasificación automática de las áreas del negocio bancario en que se insertan los comentarios, el análisis de sentimientos, la localización geográfica, la fecha..

algunos de los cuales hemos dejado temporalmente desactivados para que sean activados cuando BBVA quiera lanzarse a la recogida del big data propuesto para Zyan. (56 seg)

[Bloc de notas de Jupyter]
En este momento, esto es lo que ha comenzado a hacer Zyan desde su bucket en aws:

[Ir ejecutando script mencionando: usamos tweepy para la descarga de comentarios, ejecutamos la api con los parámetros que vamos a utilizar para esta demo, guardamos clasificada la data, hacemos un análisis de sentimientos, representamos por fecha y sentimiento los tweets sobre las opiniones que hay frente al covid y damos una idea en una nube de palabras de lo qe sucede]

[power point mostrar algunas representaciones gráficas y nubes]
