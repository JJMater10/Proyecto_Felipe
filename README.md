# Marco teorico

## Python 
  El desarrollo de un CRUD (Create, Read, Update, Delete) se llevará a cabo utilizando el lenguaje Python.  Python es una herramienta poderosa y versátil en la programación, destacada por su claridad y legibilidad en el código. Este lenguaje, creado por Guido van Rossum en 1991, ha ganado popularidad en una variedad de campos, desde el desarrollo web hasta la inteligencia artificial. Su sintaxis amigable lo hace atractivo tanto para programadores novatos como experimentados. Con una amplia gama de bibliotecas y frameworks disponibles, Python facilita la construcción de diversas aplicaciones, simplificando tareas como análisis de datos, desarrollo de juegos y automatización de procesos.

## MongoDB Atlas
MongoDB Atlas proporciona la principal solución de base de datos del mundo para aplicaciones modernas como un servicio en la nube totalmente automatizado. Esta plataforma, creada y operada por el mismo equipo responsable de la base de datos, permite crear y gestionar bases de datos Mongo desde cualquier lugar del mundo.

Con MongoDB Atlas, la migración se simplifica enormemente, gracias a funciones avanzadas como clusters globales que permiten un acceso de baja latencia desde cualquier ubicación. La administración de bases de datos se vuelve sencilla, ya sea a través de la interfaz de usuario con unos pocos clics o mediante llamadas a la API, garantizando una infraestructura fiable y escalable.

La plataforma automatiza el proceso de aprovisionamiento, configuración e implementación de la infraestructura, asegurando que los equipos obtengan los recursos necesarios de la base de datos cuando los necesiten. Además, permite escalar recursos informáticos, de memoria y de almacenamiento con facilidad.

Los clústeres de MongoDB Atlas están diseñados para garantizar una alta disponibilidad y durabilidad, con clústeres de recuperación automática distribuidos geográficamente para evitar puntos únicos de falla. Además, las bases de datos se implementan en nubes privadas virtuales para garantizar el aislamiento de la red y la seguridad desde el principio.

La plataforma ofrece una optimización simplificada mediante gráficos que proporcionan una visibilidad profunda del clúster, rastreando docenas de métricas clave. Y con soporte para más de 50 regiones de la nube en servicios como Amazon Web Services, Microsoft Azure y Google Cloud Platform, MongoDB Atlas está disponible en una amplia gama de entornos de nube

### Herramientas de mongoDB Atlas

#### Replicación

MongoDB Atlas crea automáticamente un sistema de replicación con tres bases de datos: una principal y dos secundarias. Si la base de datos principal falla, una de las secundarias asume su función, garantizando la continuidad del servicio.

Para verificar la replicación, es necesario conectarse a la base de datos remota utilizando el shell de MongoDB. Para instalar el Shell, se puede descargar la versión 2.0.0 MSI desde la página oficial de MongoDB. Luego, se accede al cluster de la base de datos en la página de MongoDB y se elige el método de conexión deseado en "Connect". En este caso, se utilizará el metodo "Shell" de mongo. Se ejecuta la línea de comando proporcionada por MongoDB que es la siguinte:

`mongosh "mongodb+srv://cluster0.773wf9g.mongodb.net/" --apiVersion 1 --username <username>`

En una consola CMD o PowerShell, se remplaza el "username" con el usuario correspondiente. Se proporciona la contraseña cuando se solicite.

Una vez conectado, se puede revisar el estado de la replicación ejecutando el comando:

` rs.status()`

Este comando mostrará la cantidad de bases de datos (generalmente tres) involucradas en la replicación, así como sus roles (primario o secundario) en la jerarquía de replicación.

## Flask
Flask es un marco web ligero escrito en Python. Se considera un microframework porque ofrece una base básica para construir aplicaciones web, y puedes agregar características utilizando bibliotecas externas según sea necesario. Esto lo hace versátil y adecuado tanto para principiantes como para desarrolladores experimentados.

Algunas características clave de Flask:

- Simple y Fácil de Aprender: Flask tiene un diseño limpio y minimalista, lo que lo convierte en una excelente opción para comenzar con el desarrollo web en Python. Puedes entender rápidamente los fundamentos y comenzar a construir aplicaciones.
- Flexible y Escalable: La estructura modular de Flask te permite extender su funcionalidad con bibliotecas de terceros. Esto te permite crear aplicaciones web simples o complejas según tus necesidades.
- Open-Source y Gratuito: Flask es gratuito para usar y modificar, lo que lo convierte en una opción atractiva para proyectos personales y comerciales.

En esencia, Flask proporciona los bloques de construcción principales para aplicaciones web, y puedes personalizarlo con herramientas adicionales para satisfacer tus necesidades específicas.

## API
- Primero aclaremos que es un ** API **(interfaz de programación de aplicaciones) define las reglas que debes seguir para comunicarte con otros sistemas de software. Los desarrolladores exponen o crean APIs para que otras aplicaciones puedan comunicarse con sus aplicaciones de manera programática.

## REST
 REST es una interfaz que permite conectar sistemas utilizando el protocolo HTTP. Su función principal es obtener y generar datos y operaciones, devolviendo esos datos en formatos específicos como XML y JSON. En la actualidad, el formato más utilizado es JSON, debido a su ligereza y legibilidad en comparación con XML. La elección entre ambos formatos dependerá de la lógica y necesidades de cada proyecto. REST se basa en HTTP y utiliza los mismos verbos: GET, POST, PUT y DELETE. Esto lo convierte en una alternativa más sencilla a SOAP, una arquitectura más compleja que trabajaba exclusivamente con XML. REST simplifica el desarrollo de APIs al permitirnos almacenar la lógica de negocio en un BACKEND y servir datos a través de recursos URL y datos limitados 

## RESTFUL
Restful es una interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet que se adhiere a las restricciones del estilo arquitectónico REST y permite la interacción con servicios web RESTful
 - Representational State Transfer (REST) es una arquitectura de software que impone condiciones sobre cómo debe funcionar un API.
 - Inicialmente, REST se creó como una guía para gestionar la comunicación en una red compleja como Internet.
 - Puedes usar la arquitectura basada en REST para admitir una comunicación eficiente y confiable a gran escala.
 Así como REST es el estilo de Arquitectura, RESTful es la implementación de dicha arquitectura.
 - Entonces por simple sentido común un API RESTful es un API que fue diseñada usando la arquitectura REST. Así de sencillo estimados, no hay por qué complicarse más.
 
 - Los desarrolladores de APIs pueden diseñar APIs utilizando varias arquitecturas diferentes. Las APIs que siguen el estilo arquitectónico REST se llaman APIs REST. Los servicios web que implementan la arquitectura REST se denominan servicios web RESTful.
 Es como un puente entre clientes (personas o sistemas de software) y recursos en la web. Los recursos pueden ser imágenes, videos, texto, números o cualquier tipo de datos. Estos APIs permiten a las aplicaciones comunicarse de manera segura, confiable y eficiente a través de estándares de comunicación de software

## Postman
Postman es una herramienta popular utilizada por desarrolladores de software para probar, desarrollar y documentar APIs (Interfaz de Programación de Aplicaciones). Funciona como un cliente de API que permite enviar solicitudes HTTP a través de diferentes métodos (GET, POST, PUT, DELETE, etc.) y visualizar las respuestas de manera clara y organizada. Con Postman, los desarrolladores pueden crear y organizar colecciones de solicitudes, lo que facilita la automatización de pruebas, la colaboración en equipo y la documentación de APIs. También ofrece características avanzadas como la configuración de variables de entorno, pruebas automatizadas, autenticación, y la posibilidad de simular diferentes escenarios de uso de la API.

## CRUD
CRUD es un acrónimo que significa Create (Crear), Read (Leer), Update (Actualizar) y Delete (Eliminar).expand_more Se utiliza para describir las operaciones básicas que se pueden realizar en la mayoría de las bases de datos y sistemas de gestión de información.expand_more

En otras palabras, CRUD define las acciones fundamentales que permiten manipular datos:

- Crear: Agregar nuevos registros a la base de datos.expand_more Por ejemplo, añadir un nuevo usuario a un sistema de gestión de clientes.
- Leer: Obtener información de la base de datos.expand_more Esto puede implicar consultar un solo registro o realizar búsquedas más complejas.expand_more
- Actualizar: Modificar datos existentes en la base de datos. Por ejemplo, cambiar la dirección de un cliente en un sistema de pedidos.
- Eliminar: Borrar registros de la base de datos. Esto puede ser necesario para liberar espacio o eliminar información obsoleta.

Las operaciones CRUD son esenciales para la gestión de cualquier base de datos, y se encuentran presentes en una amplia variedad de aplicaciones, desde software empresarial hasta sitios web.

## JavaScript
JavaScript es un lenguaje de programación que los desarrolladores utilizan para hacer páginas web interactivas. Desde actualizar fuentes de redes sociales a mostrar animaciones y mapas interactivos, las funciones de JavaScript pueden mejorar la experiencia del usuario de un sitio web. Como lenguaje de scripting del lado del servidor, se trata de una de las principales tecnologías de la World Wide Web. Por ejemplo, al navegar por Internet, en cualquier momento en el que vea un carrusel de imágenes, un menú desplegable “click-to-show” (clic para mostrar), o cambien de manera dinámica los elementos de color en una página web, estará viendo los efectos de JavaScript.


# Metodologia
La implementación de un sistema de CRUD con Python, Flask, MongoDB y RESTful implica un enfoque paso a paso que abarca desde la planificación inicial hasta el despliegue final del sistema. En primer lugar, se lleva a cabo un análisis detallado de los requisitos del proyecto para comprender completamente las necesidades de los usuarios y del sistema. Esto implica identificar qué datos se manejarán, qué operaciones CRUD serán necesarias y cómo se accederá a la API, ya sea a través de un navegador web o mediante solicitudes HTTP.

Una vez establecidos los requisitos, se procede a configurar el entorno de desarrollo. Esto implica la instalación y configuración de todas las herramientas necesarias, como Python, Flask y MongoDB. Se establece una conexión con la base de datos MongoDB y se definen los modelos de datos necesarios para representar la estructura de la información que se almacenará. Luego, se crea una aplicación Flask, donde se configuran las rutas y los controladores para manejar las solicitudes HTTP entrantes, como GET, POST, PUT y DELETE, correspondientes a las operaciones CRUD.

A medida que se implementan las operaciones CRUD para cada recurso, es fundamental asegurar la validación de datos para garantizar la integridad y consistencia de la información almacenada. Esto puede implicar verificar la validez de los datos antes de realizar operaciones de creación o actualización, así como también establecer restricciones de integridad referencial si es necesario. Además, se sigue de cerca los principios de diseño RESTful para garantizar una interfaz de API coherente y fácil de usar.

Una vez que la implementación está completa, se llevan a cabo pruebas exhaustivas para asegurar que todas las funciones se ejecuten como se esperaba y que la API sea estable y confiable. Esto puede implicar la realización de pruebas unitarias, pruebas de integración y pruebas de aceptación, y finalmente, se documenta la API de manera adecuada

Una vez desplegado, el sistema estará listo para su uso por parte de los usuarios finales, proporcionando una solución robusta y escalable para la gestión de datos mediante operaciones CRUD.

## Guia de instalación 

### Python

- Descarga el archivo ejecutable desde la página oficial de Python. [Link](https://www.python.org/downloads/)
<p align="center">
  <img width="50%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/6e00c290-ecb4-4bee-8322-9aabdde9a182">
</p>

- Ejecuta el archivo descargado.
<p align="center">
  <img width="50%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/e9e87899-6bd4-4fd4-9fc7-d5ecf4341798">
</p>

- Haz clic en "install now".
<p align="center">
  <img width="50%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/1960b49b-7c3a-4d06-b0df-8d487ace9ca3">
</p>

- Espera a que finalice el proceso de instalación.
<p align="center">
  <img width="50%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/5170562a-e03d-48f9-a556-9d6e5f0d283b">
</p>

- Después de completar la instalación, haz clic en "close".
<p align="center">
  <img width="50%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/574c66de-0f67-4636-bdaa-324e1880dc00">
</p>

- Python ha sido correctamente instalado en el dispositivo. 


### Creación de base de datos en MongoDB Atlas 

- Nos dirigimos a la página de MongoDB Atlas e iniciamos sesión. [MongoDB Atlas](https://www.mongodb.com/es/atlas/database "MongoDB Atlas")
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/252669b4-b9b7-4d22-a6a6-61d7899a11b4" width="60%">
<p\>

- Ingresamos con nuestra cuenta de Google o de Github.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/038eed0e-3a1d-49ef-bff4-30280e886ce4" width="60%" />
<p\>

- Ya logueados nos redirige a esta página donde se ubican los proyectos y damos click a New project.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/092a8227-11ab-452c-8196-04459a8aba45" width="60%" />
<p\>

- Nos pedirá que le demos un nombre al proyecto y si usted quiere agregar una etiqueta pero eso es opcional y damos click en Next.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/8fc53cb1-32e4-446a-99e9-c31ff6324ed1" width="60%"  />
<p\>

- Nos da la opción si deseamos agregar a alguien más al proyecto para eso se deberá ingresar el correo de la persona que queremos agregar y abajo seleccionamos qué rol tendrá en el proyecto y le damos en Create Project.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/29e2f4e8-4d62-4263-a9f5-f2465317b46f" width="60%" />
<p\>

- Después damos click en Create para crear nuestra base de datos.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/fd1ac5d8-1b2c-443e-8aa6-a56d4bcf5a9e" width="60%"  />
<p\>

- Seleccionamos la opción Free.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/58baf8ba-0ea4-4c1d-aad8-4835bd858c03" width="60%"  />
<p\>

- Le damos nombre a nuestra base de datos, si queremos cambiar nuestro proveedor lo podemos hacer como también nuestra región donde se conecta nuestra base de datos y damos click en Create Deployment.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/6f619bb4-b1d3-4607-bb56-82541b6b9a3d" width="60%" />
<p\>

- Después nos pedirá un nombre de usuario y su respectiva contraseña y damos click en Create Database User.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/01267ff6-11a6-46de-b931-7aa05bf5c148" width="60%"  />
<p\>

- Después vamos a seleccionar el método conexión entonces le damos click en Chose a connection method.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/1f4188ef-7584-497e-9242-44b00f3052af" width="60%" />
<p\>

- Escogemos la opción Drivers
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/6bc7b288-dfef-46e4-9a97-5a9744fad966" width="60%"  />
<p\>

- Seleccionamos el tipo de lenguaje de código que estamos usando en nuestro proyecto en nuestro caso Python.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/0ff21230-b6d9-4ca4-bd20-7612f17c15ee" width="60%"  />
<p\>

- Y abajo nos proporcionará el código de conexión para agregarlo en nuestro proyecto, y reemplazamos el usuario y la contraseña.
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151104/1a4d001b-1eae-406a-9965-fbf4bcb050bc" width="60%"  />
<p\>

Y asi es como se crea una base de datos en MongoDB Atlas y tambien como conectarla con nuestro proyecto.

### Comandos principales para poder ejecutar el API 

Los siguientes comandos se pueden instalar por medio del terminal de Visual Studio Code o por el cmd: 

-  `pip install flask` : Instala el framework Flask, que es utilizado para construir aplicaciones web en Python.

-  `pip install pymongo` : Instala el paquete Certifi, que proporciona certificados de raíz de confianza para la verificación de conexiones SSL/TLS.

-  `pip install certifi` : Instala el controlador oficial de MongoDB para Python, permitiendo interactuar con bases de datos MongoDB desde Python.

-  `pip install pymongo[srv]`: Instala pymongo junto con el soporte para la conexión a MongoDB utilizando la URI de conexión SRV, que es una forma de conexión recomendada para los servicios de MongoDB en la nube.

### Instalación Postman
- Ve al sitio web oficial de Postman:. [Link](https://www.postman.com/)
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/0b5da409-e623-4acc-9bfa-5949476d6951" />
<p\>
	
- Espera hasta que la descarga se complete 
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/3f034a40-1965-44a3-bba4-d242f1ea0554" />
<p\>
	
- Se descargará un archivo de instalación ejecutable de Postman en tu computadora. Por lo general, este archivo tendrá una extensión ".exe".
una vez termine iremos a la carpeta que guardamos el archivo en nuestro caso lo guardamos en descargas por defecto
 
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/e6680168-ca48-491f-aaa0-6edd00f35e0e" />
<p\>

- Una vez terminado el proceso damos clik en ejecutar y el programa se comenzará a instalar 
y a ejecutar, Haz doble clic en el archivo de instalación de Postman (con extensión .exe) para comenzar el proceso de instalación.
 
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/36fdd694-6e3a-4f01-a129-23f88d025904" />
<p\>

- Una vez completada la instalación, puedes iniciar Postman desde el menú de inicio o desde el acceso directo creado en el escritorio, si elegiste esta opción durante la instalación.
luego se procede a ingresar con el correo electrónico si ya tienes cuenta o sino crea una cuenta nueva en postman 
 
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/2680d998-b243-498f-a2df-7a4635bf832e" />
<p\>

- Aparece el siguiente cuadro 
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/5bef7328-5552-451b-ba7d-47258aa476f5" />
<p\>

- Luego le das en los permisos para poder empezar a ejecutar postman  
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/d9d37a66-29b6-4427-9723-bac94fb8d264" />
<p\>

- Y al finalizar abrira una ventana y podras empezar a utilizar postman para tu proyecto  
<p align="center">
<img src="https://github.com/JJMater10/Proyecto_Felipe/assets/163372160/6dfdf93e-e86b-422a-8f8e-297e4b1b79e7" />
<p\>


### Rutas de Postman

#### Agregar clientes:

Para crear un cliente, se utilizará el método "POST". Se debe agregar la ruta del servidor en la parte superior, especificando la tabla donde se añadirá el cliente. En "key", se ingresarán los campos de la tabla, y en "value", los datos del cliente. Por último, se presiona "send" en la esquina superior derecha para guardar el cliente en la base de datos. 

<p align="center">
  <img width="60%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/d57ad0c2-d554-4352-b878-a03e83482c50">
</p>

En la parte inferior, se puede observar la correcta guardado del cliente.

#### Ver clientes:

Para visualizar los clientes guardados en la base de datos, se utilizará el método "GET". Se debe ingresar la ruta del servidor (y de la tabla, si es necesario), luego se presiona "send" en la esquina superior derecha.

<p align="center">
  <img width="60%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/e2d9b734-a871-4b7a-a4ce-105bd8f4ccb4">
</p>

En la parte inferior, se pueden observar los clientes guardados en la base de datos.

#### Editar clientes:

Para editar un cliente, se utilizará el método "POST". Se agrega la ruta del servidor seguida de "edit" y el nombre del cliente que se desea editar. Luego, en "key", se añaden los campos de la tabla, y en "value", los nuevos datos del cliente. Por último, se presiona "send" en la esquina superior derecha para guardar los cambios del cliente en la base de datos.

<p align="center">
  <img width="60%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/a30858da-8f36-414c-b8bd-e346fd0bfad6">
</p>

En la parte inferior, se observa la correcta actualización de los datos del cliente.

#### Eliminar cliente:

Para eliminar un cliente, se utilizará el método "DELETE". Se agrega la ruta del servidor seguida de "edit" y el nombre del cliente que se desea eliminar. Luego, se presiona "send" en la esquina superior derecha.

<p align="center">
  <img width="60%" src="https://github.com/JJMater10/Proyecto_Felipe/assets/89151037/cf2f0c8c-3d7f-4831-99ad-a462a5552298">
</p>

En la parte inferior, se puede observar que ya no hay ningún cliente guardado en la base de datos.

### ¿Por qué Postman no puede ser utilizado para convertir una base de datos primaria en secundaria?
Postman no puede usarse para modificar la configuración de acceso IP en MongoDB Atlas. En MongoDB Atlas, las conexiones de cliente a la base de datos están restringidas por la lista de acceso IP del proyecto, que incluye direcciones IP individuales o rangos de direcciones CIDR. Si deseas bloquear el acceso desde una IP específica, debes eliminar esa entrada de la lista de acceso IP en la configuración de tu proyecto en MongoDB Atlas.

## Explicación del codigo
- CRUD de Clientes en Python con Flask y MongoDB
 Describe en detalle el CRUD (Create, Read, Update, Delete) de clientes implementado en Python utilizando Flask como framework web y MongoDB como base de datos. La aplicación permite agregar, editar y eliminar clientes, y muestra una lista de clientes en una página web

 - Archivos Relevantes
    - app.py: Este archivo es el principal y define la aplicación Flask. Contiene las rutas para las operaciones CRUD.
   -  database.py: Establece la conexión con la base de datos MongoDB.
    - cliente.py: Define la clase Cliente.
   -  index.html: Es la plantilla HTML para la interfaz de usuario.
   
 - Estructura de la Aplicación
   - Modelo:
La clase Cliente en cliente.py representa el modelo de datos para los clientes.
Cada instancia de Cliente tiene atributos como nombre, apellido y edad.
El método toDBCollection() convierte los atributos en un diccionario para su almacenamiento en la base de datos.
   - Controlador:
app.py define las rutas y las funciones para manejar las operaciones CRUD.
Las rutas incluyen:
     - /: Muestra la lista de clientes.
     - /clientes (método POST): Agrega un nuevo cliente.
     - /delete/<string:cliente_nombre> (método DELETE): Elimina un cliente.
     - /edit/<string:cliente_nombre> (método POST): Edita un cliente.

 - Vista:
      - index.html es la plantilla HTML para la interfaz de usuario.
      - Muestra un formulario para agregar clientes y una lista de clientes existentes.
      - Los datos se presentan en una tabla.
      - Conexión a la Base de Datos: database.py establece una conexión con MongoDB utilizando la URI proporcionada. La base de datos se nombra \"dbb_clientes_app\".

 - Ruta Principal (/):
    - La función home() obtiene la lista de clientes desde la base de datos. Si la solicitud proviene de Postman, devuelve JSON; de lo contrario, renderiza el template HTML.
    - Los ObjectId se convierten a strings para facilitar la visualización.

  - Agregar Cliente (/clientes):
     - La función addCliente() obtiene los datos del formulario (nombre, apellido, edad).
     - Crea un objeto Cliente con los datos proporcionados.
     - Inserta el cliente en la colección de clientes.
     - Redirige a la página principal.

  - Eliminar Cliente (/delete/<string:cliente_nombre>):
     - La función delete(cliente_nombre) elimina un cliente según el nombre proporcionado.
	 - Redirige a la página principal.
	 - Editar Cliente (/edit/<string:cliente_nombre>):
	 - La función edit(cliente_nombre) obtiene los datos del formulario (nombre, apellido, edad). 
	 - Actualiza los datos del cliente con el nombre proporcionado.
	 - Redirige a la página principal.

  - Interfaz de Usuario

     - La página principal muestra una lista de clientes.
     - El formulario permite agregar nuevos clientes.
     - Cada cliente tiene opciones para editar o eliminar.

  - Tecnologías Utilizadas
     - Python
     - Flask (framework web) - MongoDB (base de datos)
     - Bootstrap (para estilos en la interfaz)

# Bibliografia
-  e-dea-co(sin fecha). MongoDB Atlas. [Link](https://www.e-dea.co/mongodb-atlas-base-de-datos-multicloud#:~:text=MongoDB%20Atlas%20es%20una%20base,Todo "Link")
- Assembler Institute. (sin fecha). ¿Qué es Postman? [Link](https://assemblerinstitute.com/blog/que-es-postman/ "Link")
- Codecademy. (sin fecha). ¿Qué es CRUD? [Link](https://www.codecademy.com/article/what-is-crud "Link")
- Analytics Vidhya. (2021, octubre 10). Flask Python: Guía completa para principiantes. [Link](https://flask.palletsprojects.com/ "Link")
- ¿Qué es una API de RESTful? - Explicación de API de RESTful[Link](https://aws.amazon.com/es/what-is/restful-api/_"Link")
- API Description Languages, ¡Que es un API? [Link](https://www.astera.com/type/blog/rest-api-definition/ "Link")
- IBM. (sin fecha) ,RestFul, [Link](https://www.ibm.com/topics/rest-apis "Link")
- Rest(sin fecha). ¿que es rest?. [Link](https://openwebinars.net/blog/que-es-rest-conoce-su-potencia/ "Link")
- aws amazon. (sin fecha), ¿Qué es JavaScript (JS)? [Link](https://aws.amazon.com/es/what-is/javascript/ "Link")
