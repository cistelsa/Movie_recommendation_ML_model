![Alt text](source/img/banner_project.jpg)
## Proyecto MVP de Recomendación de Películas con Proceso Integral de Data Science
## CisFlix

Bienvenidos al repositorio del Proyecto MVP de Recomendación de Películas, un emocionante proyecto que abarca todo el ciclo de vida del Data Science, desde la etapa de Data Engineering hasta la creación de una plataforma interactiva de recomendación de películas. En este README, vamos a desglosar cada fase del proceso y resaltar las tecnologías y herramientas utilizadas para llevar a cabo este proyecto.

![Alt text](source/img/banner_data_engineering.jpg)

En la fase de Data Engineering, se estableció la base sólida para todo el proceso. Aquí se realizaron las tareas esenciales de extracción, transformación y carga de datos (ETL) utilizando Visual Studio Code y Microsoft Fabric. El proceso de ETL permitió la obtención de datos desde dos datasets que se encontraban en la nube de Google Drive y el cual se alimenta constantemente y su posterior transformación para su uso en el sistema de recomendación.

Además, se llevó a cabo una meticulosa normalización de tablas, lo que aseguró que los datos estén estructurados de manera coherente y lista para su análisis. La automatización de este proceso y el de ETL fue esencial para mantener la integridad de los datos en todo momento.

Uno de los aspectos destacados de esta fase fue la implementación de un sistema de cronjobs que no solo programaba y ejecutaba automáticamente flujos de trabajo, sino que también enviaba notificaciones por correo electrónico en caso de que se detectaran errores. Esta característica garantizó la continuidad del proceso y la detección temprana de problemas. Esto fué realizado en Microsoft Fabric - Data Factory - Data Engineering.

### FastAPI: Plataforma Interactiva de Recomendación

La fase siguiente del proyecto implicó la creación de una plataforma interactiva de recomendación de películas utilizando FastAPI, una moderna y eficiente herramienta para la construcción de APIs. FastAPI se conectó de manera fluida con HTML a través del motor de plantillas Jinja2, lo que permitió la generación dinámica de contenido web basado en los resultados del análisis de datos.

La integración de Uvicorn, un servidor web de alto rendimiento, aseguró que la plataforma fuera rápida y receptiva, brindando una experiencia fluida a los usuarios que buscan recomendaciones de películas personalizadas.

### Publicación y Colaboración

El repositorio de este proyecto se encuentra alojado en GitHub, lo que facilita la colaboración y el seguimiento de versiones. Además, se utilizó Render para la publicación de la plataforma interactiva en línea, lo que permitió que los usuarios accedieran fácilmente a las recomendaciones de películas generadas por el sistema.

### Soporte y Actualizaciones
Futuras Mejoras y Actualizaciones
Estamos comprometidos en continuar mejorando y expandiendo nuestro Proyecto MVP de Recomendación de Películas. Aquí hay un vistazo de lo que puedes esperar en términos de futuras mejoras y actualizaciones:

#### Mejoras en el Frontend
Nuestro equipo está dedicado a mejorar la experiencia del usuario en la plataforma de recomendación de películas. Estamos trabajando en implementar una interfaz de usuario más intuitiva y atractiva, que brinde una navegación más fluida y opciones de personalización para los usuarios. Además, estamos explorando formas de integrar elementos visuales que enriquezcan la experiencia de descubrimiento de películas.

#### Mejoras en el Código
La calidad del código es fundamental para mantener un proyecto sólido y escalable. Estamos continuamente revisando y optimizando nuestro código base para garantizar su eficiencia y legibilidad. También estamos explorando la incorporación de prácticas de desarrollo ágil y pruebas automatizadas para agilizar el proceso de desarrollo y minimizar errores.

#### Mejoras en el Proceso de ETL
Sabemos que una base de datos bien estructurada es esencial para ofrecer recomendaciones precisas. Estamos trabajando en mejorar aún más nuestro proceso de extracción, transformación y carga de datos (ETL) para optimizar la calidad y la velocidad de procesamiento de los datos. Esto incluye la exploración de nuevas fuentes de datos y la implementación de técnicas avanzadas de limpieza y transformación.

#### Actualización de Plataformas
El mundo tecnológico avanza rápidamente, y estamos comprometidos en mantener nuestro proyecto al día con las últimas herramientas y plataformas. Estamos evaluando la posibilidad de migrar a versiones más recientes de las tecnologías utilizadas, como FastAPI y otras herramientas clave, para aprovechar las últimas características y mejoras de rendimiento.

Agradecemos tu interés y apoyo en nuestro proyecto. Estas futuras mejoras y actualizaciones reflejan nuestro compromiso de proporcionar una plataforma de recomendación de películas cada vez más robusta y emocionante. ¡Mantente atento a nuestras actualizaciones y no dudes en compartir tus comentarios y sugerencias!

![Alt text](source/img/banner_data_analysis.jpg)

