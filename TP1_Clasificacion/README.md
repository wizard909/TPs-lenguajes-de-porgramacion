# TP1 - Clasificación de los LP

**Alumno:** Facundo Cichero  
**Lenguajes asignados:** ReScript, Unison, Hylo, Inko, Gren.

En este trabajo práctico se clasifican 5 lenguajes de programación modernos de acuerdo a las categorías de la cátedra, volcando los datos analizados originalmente en la planilla de cálculo.

## Tabla de Clasificación

| LENGUAJE | AÑO | TIPO DE PARADIGMA | NIVEL ABSTRACCIÓN | DOMINIO | TIPO DE TRADUCTOR | ALMACENAMIENTO DE VARIABLES | GENERACIÓN | MANERA DE ABORDAR LA TAREA | LUGAR DE EJECUCIÓN | CONCURRENCIA | INTERACTIVIDAD DEL PROGRAMA | REALIZACIÓN VISUAL | PREDICCIÓN DEL SIGUIENTE ESTADO | CARACTERÍSTICAS ÚTILES O PRODUCTIVAS | DATO CURIOSO |
|----------|-----|-------------------|-------------------|---------|-------------------|-----------------------------|------------|----------------------------|--------------------|--------------|-----------------------------|--------------------|---------------------------------|--------------------------------------|--------------|
| **ReScript** | 2020 | Objetos, Funcional | Alto | Específico (desarrollo web) | Compilado | Dinámico | 4° | Declarativos | Cliente | Concurrente | Orientado a eventos | Textual | Deterministas | Útiles | Facebook utilizó BuckleScript —el antecesor directo de ReScript— para escribir el 50% del código de Messenger.com, además de desplegarlo en herramientas internas de WhatsApp e Instagram Web. |
| **Unison** | 2020 | Funcional | Alto | Específico (computación distribuida) | Compilado | Dinámico | 5° | Declarativos | Servidor | Concurrente | No orientado a eventos | Textual | Deterministas | Útiles | Cada función se identifica por el hash de su contenido y no por su nombre. Esto hace que el código nunca 'rompa' por renombrar algo y permite enviar funciones a ejecutarse en otras máquinas de forma transparente, logrando computación distribuida nativa. |
| **Hylo (ex Val)** | 2022 | Imperativo, Objetos | Alto | Sistemas | Compilado | Algol | 4° | Operativos | Cliente | Concurrente | No orientado a eventos | Textual | Deterministas | Útiles | Lo creó Dave Abrahams, el mismo que diseñó Swift en Apple. Curiosamente, el compilador de Hylo está escrito en Swift. Hasta 2023 se llamaba 'Val'. |
| **Inko** | 2015 | Objetos | Alto | General, Sistemas | Compilado | Dinámico | 4° | Operativos | Servidor | Concurrente | No orientado a eventos | Textual | Deterministas | Útiles | Originalmente era interpretado, con una máquina virtual escrita en Rust. En 2023 los autores la descartaron por completo y reescribieron el lenguaje como compilado a código máquina con LLVM. |
| **Gren** | 2022 | Funcional | Alto | General, Scripts | Compilado | Dinámico | 4° | Declarativos | Servidor, Cliente | No concurrente | Orientado a eventos | Textual | Deterministas | Útiles | Creado por Robin Heggelund Hansen en 2022 como un fork de Elm. Su nombre significa 'rama' en noruego. A diferencia de Elm que solo corre en el navegador, Gren también apunta a backend y CLIs, usando arrays inmutables en vez de listas enlazadas como estructura por defecto. |
