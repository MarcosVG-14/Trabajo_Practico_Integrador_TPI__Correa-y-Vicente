# Trabajo-Pr-ctico-Integrador-TPI---Correa-y-Vicente
# Biblioteca de Países & Gestión de Datos Continentales
Este es una aplicación interactiva desarrollada en Python y ejecutada a través de la consola, diseñado especialmente para almacenar, administrar, filtrar, ordenar y analizar información geopolítica y estadística básica de diferentes países del mundo.
El programa utiliza una interfaz visual adaptada a la terminal mediante el uso de recuadros de texto decorativos (caracteres ASCII), garantizando una experiencia de usuario intuitiva, prolija y ordenada.

## Características Principales
El sistema ofrece un menú completo con 7 acciones para una gestión eficiente de los datos:

1. **Añadir Países:** Permite registrar múltiples países en una sola carga. Captura de forma validada el nombre del país, su población, su superficie (en km2) y el continente al que pertenece. Cuenta con control de duplicados para evitar registros repetidos.
2. **Actualizar Datos:** Modifica la población, la superficie o ambos campos de cualquier país ya registrado en el sistema.
3. **Buscar un País:** Localiza un país específico ingresando su nombre completo o las primeras letras de este (búsqueda parcial).
4. **Filtrado Avanzado:** Filtra los datos del sistema en tres variantes posibles:
   * Por continente.
   * Por rango numérico de población (mínimo y máximo).
   * Por rango numérico de superficie (mínimo y máximo).
5. **Ordenamiento Personalizado:** Organiza el listado completo de los países de forma Ascendente o Descendente en base a:
   * Nombre alfabético.
   * Cantidad de población.
   * Extensión de superficie.
6. **Reporte Estadístico Global:** Genera un análisis matemático instantáneo con:
   * Identificación del país con mayor y menor población mundial.
   * Promedio general de población y superficie de toda la base de datos.
   * Conteo exacto de la cantidad de países registrados por cada continente mediante estructuras de diccionarios.
7. **Persistencia de Datos:** Carga automática al iniciar y guardado seguro en cada modificación mediante un sistema de archivos local (`guardar_archivo` y `cargar_archivo`).
## 🛠️ Requisitos del Sistema y Estructura
El proyecto está modularizado para mantener un código limpio y escalable. Para funcionar correctamente, requiere que los siguientes archivos estén presentes en el mismo directorio de trabajo:
* **`main.py` (o tu archivo ejecutable):** Contiene la lógica del bucle principal `menu()`.
* **`funciones_programa.py`:** Contiene las funciones del núcleo operativo (`agregar_pais`, `actualizar_datos`, `buscar_por_nombre`, `filtar_paises`, `ordenar_paises`, `calculo_estadisticas`).
* **`funciones_paralelas.py`:** Contiene las funciones complementarias que se utilizan en el programa principal: funciones de validación de entradas (`validar_texto`, `validar_entero`, `validar_flotante`), controles de interfaz (`limpiado_consola`, `continuar`), verificación de estados (`lista_vacía`) e interacción de archivos (`guardar_archivo`, `cargar_archivo`, `imprimir_diccionario`).

## Instrucciones de Uso (Paso a Paso)
Al iniciar el programa, serás recibido por el menú principal interactivo en la terminal.
### 1. Cómo añadir un país al sistema
1. Selecciona la opción **`1`** en el menú principal.
2. El sistema te preguntará cuántos países deseas cargar. Ingresa un número entero o presiona **`S`** si deseas arrepentirte y regresar.
3. Para cada país, introduce su nombre. *Nota: Si dejas el campo vacío y presionas 'Enter', saltarás el registro actual.*
4. Si el país ya fue cargado previamente, el sistema te lo advertirá y cancelará la duplicación regresando al menú.
5. Si es nuevo, introduce de forma sucesiva su población y superficie. Las funciones de validación evitarán que ingreses letras o valores erróneos.
6. Elige el continente seleccionando un número del **1 al 6** (América, Europa, África, Asia, Oceanía o Antártida).
7. Al finalizar, el país se guardará automáticamente en el disco rígido.
### 2. Cómo actualizar los datos de un país existente
1. Selecciona la opción **`2`**.
2. Escribe el nombre del país que deseas modificar. El sistema no distingue entre mayúsculas y minúsculas (`capitalize`).
3. Si el país existe, aparecerá un submenú en pantalla:
   * Presiona **`1`** para cambiar solo la Población.
   * Presiona **`2`** para cambiar solo la Superficie.
   * Presiona **`3`** para modificar Ambos Campos.
   * Presiona **`4`** para cancelar la operación y salir sin aplicar cambios.
4. Tras ingresar los nuevos datos válidos, los cambios impactarán inmediatamente en el archivo de guardado.
### 3. Cómo buscar un país por su nombre
1. Selecciona la opción **`3`**.
2. Introduce el nombre (o las letras iniciales) del país que buscas.
3. Si el sistema encuentra una coincidencia (por ejemplo, escribir "Ar" para buscar "Argentina"), se llamará a la función `mostrar_paises()` para renderizar los datos estructurados en pantalla de forma prolija.
### 4. Cómo filtrar la base de datos
1. Selecciona la opción **`4`**.
2. Ingresa al menú interactivo de filtrado y elige tu criterio (**1**, **2** o **3**).
3. Si filtras por población o superficie, define un límite mínimo y un límite máximo. El sistema procesará la lista de manera inteligente mediante comprensiones de listas (`list comprehensions`) y te mostrará en consola únicamente los países que se ubiquen dentro de ese rango cerrado.
### 5. Cómo ordenar los listados de visualización
1. Selecciona la opción **`5`**.
2. Elige la variable bajo la cual quieres ordenar (**1** para Nombre, **2** para Población, **3** para Superficie).
3. Inmediatamente después, el sistema te solicitará el sentido del orden: escribe **`A`** para un orden ascendente (de menor a mayor / de la A a la Z) o **`D`** para un orden descendente.
4. La lista ordenada se desplegará instantáneamente en pantalla sin alterar la base de datos original del archivo.
### 6. Cómo revisar las estadísticas generales del sistema
1. Selecciona la opción **`6`**.
2. Se imprimirá un cuadro formal con el título **`REPORTE ESTADÍSTICO GLOBAL`**.
3. Podrás leer los valores absolutos máximos y mínimos, los promedios calculados dinámicamente y una tabla final detallada indicando cuántos países tiene registrados el sistema por cada continente en ese momento.
