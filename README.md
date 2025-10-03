<h1>CAROL ALFONSO — Entrega Nivel Intermedio PRO .</h1>
CodExpress — Nivel Intermedio (Estructuras + POO)
<p><strong>Tiempo:</strong> 3 horas · <strong>Meta:</strong> completar <u>7 u 8 mini-retos</u> y, si te alcanza, una <u>app integrada (código 2900)</u> que reutilice tus propias <strong>clases y funciones</strong>. Lenguajes: <strong>Python</strong>, <strong>Java</strong> o <strong>C++</strong> (usando POO).</p>

<h2>Flujo de trabajo (fork &amp; PR)</h2>
<ol>
  <li>Haz <em>fork</em> y clona tu copia.</li>
  <li>Usa un <strong>&lt;ALIAS&gt;</strong> sin espacios ni acentos (tu usuario de GitHub o <code>nombre-apellido</code> en minúsculas).</li>
  <li>Para cada mini-reto: crea un archivo con <strong>formato exacto</strong> <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code> (ej.: <code>2004_maria-perez_v1.py</code> o <code>2004_maria-perez_v1.java</code>).</li>
  <li>Si haces la app: crea <code>2900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo ejecutar) y, si quieres, <code>src/</code> y <code>requirements.txt</code>.</li>
  <li>Abre un Pull Request a <code>main</code> titulado <strong>&lt;ALIAS&gt; — Entrega Nivel Intermedio PRO</strong>.</li>
</ol>

<hr />

<h2>Códigos</h2>
<ul>
  <li><strong>Mini-retos:</strong> 2001–2008 (elige 7 u 8)</li>
  <li><strong>App integrada:</strong> 2900 (<em>Organizer 1.0 — POO</em>)</li>
</ul>
<p><strong>Nombre de archivo obligatorio:</strong> <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code></p>

<hr />

<h2>Mini-retos (más desafiantes, con variantes “PLUS”)</h2>
<p>Usa <strong>solo librerías estándar</strong>. Al final de cada archivo agrega, en comentarios, <strong>3 pruebas</strong> (entrada → salida esperada). La salida se compara <strong>literalmente</strong>. Cuando se pida una estructura/clase, <u>debes implementarla</u>.</p>

<table>
  <thead>
    <tr><th>Código</th><th>Nombre</th><th>Requisitos POO y reglas</th><th>Entrada/Salida</th><th>Archivo</th><th>Docs</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>2001</strong></td><td>ContactBook (CRUD, POO)</td><td>Clases: <code>Contact</code> y <code>ContactBook</code>. Alta/baja/búsqueda case-insensitive (nombre/email) y listado con orden estable <em>apellido,nombre</em>. Email duplicado → <code>ERROR:DUP</code>. <strong>PLUS:</strong> persistencia JSON de la lista y un índice por dominio de email <code>@dominio</code> para <code>LIST domain=gmail.com</code>.</td><td>Comandos stdin: <code>ADD nombre;apellido;email;tel</code> · <code>DEL email</code> · <code>FIND texto</code> · <code>LIST</code> (o <code>LIST domain=...</code>). LIST imprime <code>apellido,nombre &lt;email&gt; tel</code>.</td><td><code>2001_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/tutorial/classes.html">POO Py</a> · <a href="https://docs.oracle.com/javase/tutorial/java/IandI/">POO Java</a> · <a href="https://en.cppreference.com/w/cpp/language/classes">POO C++</a></td></tr>
    <tr><td><strong>2002</strong></td><td>Semester GPA (POO + precisión)</td><td>Clases: <code>Course</code> y <code>Semester</code>. Promedio ponderado con <strong>Decimal/BigDecimal</strong> (2 decimales, ROUND_HALF_UP). Duplicado por nombre → <code>ERROR:DUP</code>. <strong>PLUS:</strong> aceptar importación CSV simple desde stdin (<code>nombre,creditos,nota</code>) con <code>IMPORT</code> y reportar cuántas filas válidas/erróneas.</td><td>Comandos: <code>ADD nombre;creditos;nota</code> · <code>AVG</code> → <code>prom=XX.XX</code> · <code>LIST</code> (créditos desc, luego nombre) · <code>IMPORT</code>.</td><td><code>2002_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/library/decimal.html">Decimal</a> · <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/math/BigDecimal.html">BigDecimal</a></td></tr>
    <tr><td><strong>2003</strong></td><td>Stack&lt;T&gt; con MinStack/Undo</td><td>Clase genérica <code>Stack&lt;T&gt;</code> con <code>push/pop/peek/size</code> O(1). Vacía → <code>ERROR:EMPTY</code>. Documenta complejidad. <strong>PLUS (elige uno):</strong> (a) <em>MinStack</em> que devuelve mínimo en O(1) o (b) par <code>UndoStack/RedoStack</code> con <code>UNDO</code>/<code>REDO</code> sobre una pila principal.</td><td>Operaciones por línea: <code>PUSH x</code> · <code>POP</code> · <code>PEEK</code> · <code>SIZE</code> (+ <code>MIN</code> o <code>UNDO/REDO</code> si haces PLUS).</td><td><code>2003_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists">list.pop/append</a></td></tr>
    <tr><td><strong>2004</strong></td><td>Queue con métricas</td><td>Clase <code>Queue</code> implementada con <strong><code>deque</code>/<code>ArrayDeque</code>/<code>std::deque</code></strong>. <code>ENQUEUE id @timestamp</code>, <code>DEQUEUE @timestamp</code>. Reporta <em>wait_avg</em> y <em>len</em>. Vacía → <code>ERROR:EMPTY</code>. <strong>PLUS:</strong> <em>rate-limit</em> por ventana de 60s (máx K ops; K se pasa por <code>SETK K</code>).</td><td>Operaciones por línea. <code>STATS</code> imprime <code>len=L wait_avg=SEGUNDOS</code> (entero).</td><td><code>2004_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/library/collections.html#collections.deque">deque</a> · <a href="https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html">ArrayDeque</a></td></tr>
    <tr><td><strong>2005</strong></td><td>BiDictionary (bijección estricta)</td><td>Clase <code>BiDictionary</code> con dos mapas sincronizados (<em>es↔en</em>). <code>ADD es:en</code> (minúsculas normalizadas con <code>casefold</code>/<code>toLowerCase</code>), <code>?palabra</code>, <code>LIST</code> (ordenado por <em>es</em>). Reasignar palabra usada (en cualquier lado) → <code>ERROR:DUP</code>. <strong>PLUS:</strong> <code>BULKADD</code> (varias en un bloque): carga todo o nada; si hay conflicto imprime <code>ERROR:BULK</code> y no cambia estado.</td><td>Consulta imprime <code>es=... en=...</code> o <code>NOTFOUND</code>. <code>EXPORT</code> opcional a JSON.</td><td><code>2005_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/library/json.html">json</a></td></tr>
    <tr><td><strong>2006</strong></td><td>WordSearch PRO (8 direcciones)</td><td>Clase <code>Grid</code> con <code>find(word)</code>. Busca en 8 direcciones con orden fijo <code>N,NE,E,SE,S,SW,W,NW</code>. <strong>PLUS:</strong> aceptar una lista de palabras y devolver <u>todas</u> las ubicaciones en orden estable por palabra y por coordenada inicial.</td><td>Entrada: matriz A-Z (sin espacios), línea vacía, palabra(s). Salida: <code>r,c</code> del primer carácter o <code>NO</code>; en PLUS, múltiples líneas <code>palabra:r,c</code>.</td><td><code>2006_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/tutorial/controlflow.html#for-statements">for</a></td></tr>
    <tr><td><strong>2007</strong></td><td>Secuencias: interfaz/abstracta</td><td>Define interfaz <code>Sequence</code> (Java) o clase abstracta (Python <code>abc.ABC</code>) con <code>compute(n)</code>. Implementa <code>FibIter</code> (iterativa) y <code>FibFast</code> (<em>fast-doubling</em> o recursiva con <code>@lru_cache</code>/<em>memo</em>). <strong>PLUS:</strong> añade <code>Tribonacci</code> que implementa la misma interfaz. Imprime tiempo/llamadas.</td><td>Entrada: <code>n</code>. Salida: <code>fib_iter=...</code> <code>fib_fast=...</code> <code>t_ms=...</code> (<code>calls=...</code> si aplica). En PLUS: <code>trib=...</code>.</td><td><code>2007_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/library/abc.html">abc</a> · <a href="https://docs.python.org/3/library/functools.html#functools.lru_cache">lru_cache</a></td></tr>
    <tr><td><strong>2008</strong></td><td>Maze BFS con portales</td><td>Clase <code>Maze</code> con <code>shortestPath()</code>. Mapa con <code>#</code>=muro, <code>.</code>=libre, <code>S</code>=inicio, <code>E</code>=salida, y letras <code>A..Z</code> que representan <em>portales pareados</em> (mismo carácter = teletransporte O(1)). Vecinos en orden fijo U,D,L,R y luego teletransporte si aplica. <strong>PLUS:</strong> imprime también la ruta (U/D/L/R y <code>T</code> para teleporte).</td><td>Entrada: matriz rectangular. Salida base: <code>dist=K</code> (o <code>NO</code>). PLUS: línea adicional con la secuencia.</td><td><code>2008_&lt;ALIAS&gt;_v1.(py|java|cpp)</code></td><td><a href="https://docs.python.org/3/library/collections.html#collections.deque">deque</a></td></tr>
  </tbody>
</table>

<h3>Requisitos mínimos por mini-reto</h3>
<ul>
  <li><strong>E/S exacta</strong> (comparación literal).</li>
  <li><strong>3 pruebas</strong> (entrada → salida) en comentarios al final del archivo.</li>
  <li><strong>Solo librería estándar</strong>.</li>
  <li><strong>POO explícita</strong>: clases, métodos y cuando aplique, interfaz/abstracta.</li>
  <li><strong>Nomenclatura exacta</strong> del archivo. Nombre incorrecto: −5%.</li>
</ul>

<hr />

<h2>App integrada (2900) — Organizer 1.0 (POO)</h2>
<table>
  <thead><tr><th>Código</th><th>Debe reutilizar</th><th>Qué agrega</th><th>Entregables</th><th>Puntaje máx.</th></tr></thead>
  <tbody>
    <tr><td><strong>2900</strong></td><td>2001, 2002, 2003, 2004, 2005</td><td>Menú en consola que integra ContactBook, Semester, Stack (para <em>deshacer</em> CRUD) y Queue (turnos). Reuso real de tus clases (importa/instancia, no copies). Manejo consistente de errores.</td><td>Carpeta <code>2900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo correr, qué módulos integra) y, si quieres, <code>src/</code>.</td><td><strong>180</strong></td></tr>
  </tbody>
</table>
<ul>
  <li>Organiza en módulos/paquetes; evita “monolitos”.</li>
  <li>Incluye un diagrama textual de clases en el README.</li>
  <li>La opción “deshacer” debe usar tu <code>Stack</code> (2003). La cola (2004) debe ser <code>deque</code>/<code>ArrayDeque</code>/<code>std::deque</code>.</li>
</ul>

<hr />

<h2>Puntajes — Nivel Intermedio </h2>
<ul>
  <li><strong>Mini-reto (máx. 90 pts)</strong>: funciona (60%) · casos borde / 3 pruebas (20%) · diseño POO/claridad (10%) · defensa breve (10%).</li>
  <li><strong>App 2900 (máx. 180 pts)</strong>: integración (50%) · cohesión/reuso (20%) · manejo de errores (20%) · README (10%).</li>
</ul>

<h3>Bonificaciones creativas (opcionales, suman — tope +100 pts por equipo)</h3>
<ul>
  <li><strong>GUI real para 2900</strong> (Tkinter Python / Swing o JavaFX en Java / Qt o FLTK en C++): <strong>+30 pts</strong> (formularios para contactos, cursos y turnos; usa tus clases debajo).</li>
  <li><strong>TUI navegable</strong> (menús de texto tipo curses): <strong>+15 pts</strong>.</li>
  <li><strong>Persistencia</strong> en 2900 (guardar/cargar JSON o archivo plano sin romper la CLI): <strong>+15 pts</strong>.</li>
  <li><strong>Tests automatizados</strong> (unittest/JUnit/asserts) con ≥6 casos cubriendo errores y duplicados: <strong>+10 pts</strong>.</li>
  <li><strong>Import/Export robusto</strong> en 2005 con <em>merge</em> sin duplicados y reporte de conflictos: <strong>+10 pts</strong>.</li>
  <li><strong>PLUS implementados</strong> en al menos 3 mini-retos distintos: <strong>+20 pts</strong>.</li>
</ul>
<p><em>Nota:</em> Evita dependencias pesadas. Si tu GUI no compila en mesa, adjunta capturas/GIF + binario. La bonificación se evalúa como demo siempre que la lógica sea la tuya.</p>

<hr />

<h2>Anti-IA desde la consigna (verificación integrada)</h2>
<ul>
  <li><strong>Estructuras/clases obligatorias</strong> (ej.: <code>deque/ArrayDeque/std::deque</code> en 2004; interfaz/abstracta en 2007).</li>
  <li><strong>Orden y formato deterministas</strong> (direcciones fijas en 2006; vecinos U,D,L,R en 2008; mensajes exactos <code>ERROR:DUP</code>, <code>ERROR:EMPTY</code>).</li>
  <li><strong>Precisión controlada</strong> con Decimal/BigDecimal en 2002.</li>
  <li><strong>Defensa y edición en vivo</strong> (≤2 min): se pedirá ajustar formato o añadir un caso borde.</li>
</ul>

<hr />

<h2>Checklist final</h2>
<ul>
  <li>7 u 8 mini-retos con nombres correctos: <code>200x_&lt;ALIAS&gt;_vN.(py|java|cpp)</code>.</li>
  <li>3 pruebas en comentarios por archivo.</li>
  <li>Si hiciste la app: <code>2900_&lt;ALIAS&gt;_app/</code> + <code>README.md</code> + menú funcional (o GUI/TUI si tomaste bonificación).</li>
  <li>PR: <code>&lt;ALIAS&gt; — Entrega Nivel Intermedio PRO</code>.</li>
</ul>

<h2>Documentación</h2>
<p><a href="https://docs.python.org/3/">Python</a> · <a href="https://docs.oracle.com/javase/8/docs/">Java</a> · <a href="https://en.cppreference.com/w/">C++</a> · <a href="https://docs.python.org/3/library/collections.html#collections.deque">deque (Py)</a> · <a href="https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html">ArrayDeque (Java)</a> · <a href="https://docs.python.org/3/library/abc.html">abc</a> · <a href="https://docs.python.org/3/library/functools.html#functools.lru_cache">lru_cache</a> · <a href="https://docs.python.org/3/library/json.html">json</a></p>
clases y funciones</strong>.</p>

<h2>Flujo de trabajo (fork &amp; PR)</h2>
<ol>
  <li>Haz <em>fork</em> de este repo y clónalo.</li>
  <li>Usa un <strong>&lt;ALIAS&gt;</strong> sin espacios ni acentos: tu usuario de GitHub o <code>nombre-apellido</code> en minúsculas.</li>
  <li>Para cada mini-reto crea un archivo con <strong>formato exacto</strong>: <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code> (ej.: <code>2004_maria-perez_v1.py</code> o <code>2004_maria-perez_v1.java</code>).</li>
  <li>Si construyes la app, crea <code>2900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo ejecutar), y si quieres <code>src/</code> y <code>requirements.txt</code>.</li>
  <li>Abre un Pull Request a <code>main</code> con título: <strong>&lt;ALIAS&gt; — Entrega Nivel Intermedio</strong>.</li>
</ol>

<hr/>

<h2>Códigos (Nivel Intermedio)</h2>
<ul>
  <li><strong>Mini-retos:</strong> 2001–2008 (elige 7 u 8).</li>
  <li><strong>App integrada:</strong> 2900 (<em>Organizer 1.0 — POO</em>).</li>
</ul>
<p><strong>Nombre de archivo obligatorio:</strong> <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code></p>

<hr/>

<h2>Mini-retos (entrega 7 u 8)</h2>
<p>Lenguajes permitidos: <strong>Python</strong>, <strong>Java</strong> o <strong>C++</strong> (usando POO). Usa <strong>solo librerías estándar</strong>. Al final de cada archivo agrega, en comentarios, <strong>3 pruebas</strong> (entrada → salida esperada). La salida se compara <strong>literalmente</strong> (cuida espacios y saltos de línea). Cuando se pida una estructura o clase, <u>debes implementarla</u>.</p>

<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Nombre</th>
      <th>Qué se espera (POO y verificación)</th>
      <th>Entrada / Salida</th>
      <th>Archivo</th>
      <th>Docs</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>2001</strong></td><td>Agenda de contactos (CRUD, POO)</td><td>Clase <code>Contact</code> (nombre, apellido, email, tel) + clase <code>ContactBook</code> con <code>add</code>, <code>delete</code>, <code>find</code>, <code>list</code>. Búsqueda case-insensitive por nombre o email. Orden estable por <em>apellido, nombre</em>. Email duplicado → <code>ERROR:DUP</code>. En Java: sobrescribe <code>equals/hashCode</code> por email; en Python/C++ documenta la clave única.</td><td>Comandos por stdin: <code>ADD nombre;apellido;email;tel</code> · <code>DEL email</code> · <code>FIND texto</code> · <code>LIST</code>. LIST: <code>apellido,nombre &lt;email&gt; tel</code>.</td><td><code>2001_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/tutorial/classes.html">POO Python</a> · <a href="https://docs.oracle.com/javase/tutorial/java/IandI/">POO Java</a></td></tr>
    <tr><td><strong>2002</strong></td><td>Agenda académica (POO + promedio ponderado)</td><td>Clase <code>Course</code> (nombre, créditos, nota) y clase <code>Semester</code> con <code>add</code>, <code>avg</code>, <code>list</code>. Promedio ponderado con <strong>Decimal/BigDecimal</strong> (2 decimales, ROUND_HALF_UP). Duplicados por nombre → <code>ERROR:DUP</code>. LIST: créditos desc, luego nombre.</td><td>Comandos: <code>ADD nombre;creditos;nota</code> · <code>AVG</code> → <code>prom=XX.XX</code> · <code>LIST</code>.</td><td><code>2002_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/library/decimal.html">decimal</a> · <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/math/BigDecimal.html">BigDecimal</a></td></tr>
    <tr><td><strong>2003</strong></td><td>Pila genérica (<code>Stack&lt;T&gt;</code>)</td><td>Clase <code>Stack&lt;T&gt;</code> con <code>push</code>, <code>pop</code>, <code>peek</code>, <code>size</code>. O(1) por operación (lista al final / <code>std::vector</code>). Vacía en pop/peek → <code>ERROR:EMPTY</code>. Documenta complejidad en docstring/Javadoc.</td><td>Una operación por línea: <code>PUSH x</code> · <code>POP</code> · <code>PEEK</code> · <code>SIZE</code>. Imprime resultado de POP/PEEK/SIZE.</td><td><code>2003_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/tutorial/datastructures.html#more-on-lists">list.pop/append</a> · <a href="https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html">Stack</a></td></tr>
    <tr><td><strong>2004</strong></td><td>Cola (<code>Queue</code>) con deque</td><td>Clase <code>Queue</code> con <code>enqueue</code>, <code>dequeue</code>, <code>front</code>, <code>length</code>. Implementación obligatoria con <code>collections.deque</code> (Python) / <code>ArrayDeque</code> (Java) / <code>std::deque</code> (C++). Vacía en dequeue/front → <code>ERROR:EMPTY</code>. No se acepta <code>list.pop(0)</code> por costo O(n).</td><td>Comandos: <code>ENQUEUE x</code> · <code>DEQUEUE</code> · <code>FRONT</code> · <code>LENGTH</code>. Imprime resultado de DEQUEUE/FRONT/LENGTH.</td><td><code>2004_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/library/collections.html#collections.deque">deque</a> · <a href="https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html">ArrayDeque</a></td></tr>
    <tr><td><strong>2005</strong></td><td>Diccionario ES↔EN (bidireccional, POO)</td><td>Clase <code>BiDictionary</code> con dos mapas sincronizados (es→en y en→es). Comandos: <code>ADD es:en</code> (minúsculas); <code>?palabra</code> consulta en ambas direcciones; <code>LIST</code> ordenado por clave <em>es</em>; <code>EXPORT</code> opcional a JSON. Reasignar palabra usada (en cualquier lado) → <code>ERROR:DUP</code>. Normaliza con <code>casefold()</code> (Py) / <code>toLowerCase()</code> (Java).</td><td>Consulta: <code>es=... en=...</code> o <code>NOTFOUND</code>.</td><td><code>2005_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#mapping-types-dict">dict</a> · <a href="https://docs.python.org/3/library/json.html">json</a></td></tr>
    <tr><td><strong>2006</strong></td><td>Sopa de letras (WordSearch)</td><td>Clase <code>Grid</code> con método <code>find(word)</code> que busca en 8 direcciones (N, NE, E, SE, S, SW, W, NW). Devuelve primera coincidencia siguiendo barrido por filas. Coordenadas 0-based.</td><td>Entrada: matriz A-Z (sin espacios), línea vacía, palabra. Salida: <code>r,c</code> o <code>NO</code>.</td><td><code>2006_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/library/itertools.html">itertools</a></td></tr>
    <tr><td><strong>2007</strong></td><td>Fibonacci por interfaz/clase abstracta</td><td>Define interfaz <code>Sequence</code> (Java) o clase abstracta (Python <code>abc.ABC</code>) con <code>compute(n)</code>. Implementa <code>RecursiveFib</code> con memoización (<code>@lru_cache</code>/<em>map</em>) y <code>IterativeFib</code>. Deben coincidir; imprime <code>calls=</code> de la recursiva. 0 ≤ n ≤ 45.</td><td>Entrada: <code>n</code>. Salida: <code>rec=... it=... calls=...</code>.</td><td><code>2007_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/library/abc.html">abc</a> · <a href="https://docs.python.org/3/library/functools.html#functools.lru_cache">lru_cache</a></td></tr>
    <tr><td><strong>2008</strong></td><td>Laberinto (Maze BFS, POO)</td><td>Clase <code>Maze</code> que parsea mapa (<code>#</code>=muro, <code>.</code>=libre, <code>S</code>=inicio, <code>E</code>=salida) y <code>shortestPath()</code> con BFS. Imprime <code>dist=K</code> y ruta con movimientos en orden fijo U,D,L,R. Si no hay camino: <code>NO</code>.</td><td>Entrada: matriz rectangular. Salida: <code>dist=K</code> y, en la siguiente línea, la secuencia; o <code>NO</code>.</td><td><code>2008_&lt;ALIAS&gt;_v1.py</code> / <code>.java</code> / <code>.cpp</code></td><td><a href="https://docs.python.org/3/library/collections.html#collections.deque">deque</a> · <a href="https://en.cppreference.com/w/cpp/container/deque">std::deque</a></td></tr>
  </tbody>
</table>

<h3>Requisitos mínimos por mini-reto</h3>
<ul>
  <li><strong>E/S exacta</strong>: la comparación es literal.</li>
  <li><strong>3 pruebas</strong> (entrada → salida) en comentarios al final del archivo.</li>
  <li><strong>Solo librería estándar</strong>.</li>
  <li><strong>POO explícita</strong>: clases, métodos y, cuando se pida, interfaz/abstracta.</li>
  <li><strong>Nomenclatura exacta</strong> del archivo. Nombre incorrecto: −5%.</li>
</ul>

<hr/>

<h2>App integrada (2900) — Organizer 1.0 (POO)</h2>
<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Debe reutilizar</th>
      <th>Qué agrega</th>
      <th>Entregables</th>
      <th>Puntaje máx.</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>2900</strong></td><td>2001, 2002, 2003, 2004, 2005</td><td>Un <strong>menú en consola</strong> que integra ContactBook, Semester, <em>Stack</em> (para “deshacer” CRUD) y <em>Queue</em> (turnos). Reuso real de tus clases (importa/instancia, no copies). Manejo básico de errores con mensajes consistentes.</td><td>Carpeta <code>2900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo correr, qué módulos integra) y, si quieres, <code>src/</code>.</td><td><strong>180</strong></td></tr>
  </tbody>
</table>
<ul>
  <li>Organiza tus clases en módulos/paquetes; evita “monolitos”.</li>
  <li>Incluye un diagrama textual de clases en el README.</li>
  <li>La opción “deshacer” debe usar tu <code>Stack</code> (2003). La cola (2004) debe ser <code>deque</code>/<code>ArrayDeque</code>/<code>std::deque</code>.</li>
</ul>

<hr/>

<h2>Puntajes — Nivel Intermedio</h2>
<ul>
  <li><strong>Mini-reto (máx. 90 pts)</strong>: funciona (60%) · casos borde / 3 pruebas (20%) · diseño POO/claridad (10%) · defensa breve (10%).</li>
  <li><strong>App 2900 (máx. 180 pts)</strong>: integración (50%) · cohesión/reuso (20%) · manejo de errores (20%) · README (10%).</li>
</ul>

<h3>Bonificaciones creativas (opcionales, suman puntos)</h3>
<p>Se suman al total del equipo: <strong>tope +80 pts</strong>. No sustituyen los requisitos de base.</p>
<ul>
  <li><strong>GUI real</strong> para la app 2900 (ventanas y formularios para Contactos, Cursos y Turnos) con <em>Tkinter</em> (Python, estándar) o <em>Swing</em>/<em>JavaFX</em> (Java) o <em>Qt/FLTK</em> (C++): <strong>+30 pts</strong>. Debe respetar la lógica de tus clases y permitir alta/baja/consulta.</li>
  <li><strong>TUI mejorada</strong> (interfaz de texto con menús/navegación, p. ej., <em>curses</em> en Python): <strong>+15 pts</strong>.</li>
  <li><strong>Persistencia simple</strong> (guardar/cargar contactos y cursos en JSON o archivo plano, sin romper la CLI): <strong>+15 pts</strong>.</li>
  <li><strong>Tests automatizados</strong> (Python <em>unittest</em> / Java <em>JUnit</em> / C++ simple con asserts) con al menos 6 casos que cubran errores y duplicados: <strong>+10 pts</strong>.</li>
  <li><strong>Export/Import</strong> en 2005 (BiDictionary) a JSON con validación y merge sin duplicados: <strong>+10 pts</strong>.</li>
</ul>
<p><em>Notas:</em> Evita dependencias pesadas. Si usas JavaFX/Qt y no compila en mesa, adjunta GIF o capturas + binario/ejecutable; la bonificación se evalúa como “demo” siempre que la lógica siga siendo la tuya.</p>

<hr/>

<h2>Requisitos de precisión y anti-IA desde la consigna</h2>
<ul>
  <li><strong>Estructuras/clases obligatorias</strong> cuando se indiquen (ej.: <code>ArrayDeque/deque</code> en 2004; interfaz/abstracta en 2007).</li>
  <li><strong>Orden y formato deterministas</strong> (ej.: direcciones fijas en 2006, vecinos U,D,L,R en 2008).</li>
  <li><strong>Gramática de comandos exacta</strong> y mensajes de error literales (<code>ERROR:DUP</code>, <code>ERROR:EMPTY</code>).</li>
  <li><strong>Complejidad documentada</strong> en docstring/Javadoc de 2003/2004.</li>
</ul>
<p>En la revisión se puede pedir una <strong>edición en vivo (≤2 min)</strong> para ajustar formato, añadir caso borde o modificar una clase. Debes poder hacerlo sin rehacer todo.</p>

<hr/>

<h2>Checklist final</h2>
<ul>
  <li>7 u 8 mini-retos con nombres correctos: <code>200x_&lt;ALIAS&gt;_vN.(py|java|cpp)</code>.</li>
  <li>3 pruebas en comentarios por archivo.</li>
  <li>Si hiciste la app: carpeta <code>2900_&lt;ALIAS&gt;_app/</code> + <code>README.md</code> + menú funcional (o GUI/TUI si aplicaste bonificación).</li>
  <li>Pull Request: <code>&lt;ALIAS&gt; — Entrega Nivel Intermedio</code>.</li>
</ul>

<h2>Documentación</h2>
<p><a href="https://docs.python.org/3/">Python</a> · <a href="https://docs.oracle.com/javase/8/docs/">Java</a> · <a href="https://en.cppreference.com/w/">C++</a> · <a href="https://docs.python.org/3/library/collections.html#collections.deque">deque (Py)</a> · <a href="https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html">ArrayDeque (Java)</a> · <a href="https://docs.python.org/3/library/abc.html">abc</a> · <a href="https://docs.python.org/3/library/functools.html#functools.lru_cache">lru_cache</a> · <a href="https://docs.python.org/3/library/json.html">json</a></p>
