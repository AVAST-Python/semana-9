

# Introducción a Python

## Semana 7
<!-- .element style="text-align:center" -->

![alt text](./img/logo2.png) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->

---

# Pandas

Aprieta la flecha de abajo si vas a hacer el proyecto Pandas

Enlaces:
- [Introducción a Pandas](https://aprendepython.es/pypi/datascience/pandas/)

--

# Previo: instalar las dependencias

```bash
pip install pandas
# Si vas a usar Excel:
pip install xlwt openpyxl xlsxwriter xlrd
```
<!-- .element style="font-size: 1em" -->

- Debes trabajar con Python 3. Testealo con `python --version`
- Muy recomendable usar `venv`, pero eso para otro día
- [`pandas`](https://pandas.pydata.org/) es la librería principal para manejo de datos. Tiene "tol power".
- El resto son librerías para acceder a ficheros Excel

--

# Ejercicio

Dado [este conjunto de datos](./Netflix_stock_price.zip), calcula lo siguiente:
- Qué día se ha negociado mayor volumen
- Que día de la semana tiene de media mayor volumen
- Qué día de la semana han tenido las acciones más variación de precio (entre high y low)
- En qué més ha habido mayor variación de precio (diferencia entre el precio de apertura del mes y el precio de cierre)

Primero de todo, deberás cargarlo del CSV

No vale usar Excel para calcularlo, pero sí para comprobarlo.


--

# Pistas

- <details>
<summary>Ojo al cargar los datos</summary>
Piensa qué columna vas a utilizar como índice. Tienes ejemplos de carga en el documento.
</details>
- <details>
<summary>Día de la semana</summary>
<ul>
<li>Puedes transformar el índice a datetime:<br>
<code>df.index = pd.to_datetime(df.index)</code>
<li>Puedes obtener el día de la semana con <code>df.index.weekday</code> y guardarlo en otra columna.
¿Qué valores está guardando?
<li>Se pueden agrupar datos con <code>groupby</code>
</ul>
</details>

---

# ¿Estás tocando el banjo?
#### (continuacion) <!-- .element style="text-align: center; margin-bottom: 40px" -->

Crea una función que responda a la pregunta "¿Tocas el banjo?".

Si tu nombre empieza por la letra "R" o "r" minúscula, ¡estás tocando el banjo!

La función toma un nombre como único argumento y devuelve una de las siguientes cadenas:
- nombre + " toca el banjo"
- nombre + " no toca el banjo"

Los nombres dados son siempre cadenas válidas.

<div></div> <!-- .element style="height: 200px" -->

[Enlace Kata](https://www.codewars.com/kata/53af2b8861023f1d88000832)


---

# ¿Cómo de buena eres realmente?

Había un examen en tu clase y lo has aprobado. ¡Enhorabuena!

Pero eres una persona ambiciosa. Quieres saber si eres mejor que el alumno medio de tu clase.

Recibes las puntuaciones de los exámenes de tus compañeros. Ahora calcula la media y compara tu puntuación.
Devuelve `True` si eres mejor, si no, `False`.

<div></div> <!-- .element style="height: 200px" -->

[Enlace Kata](https://www.codewars.com/kata/5601409514fc93442500010b)

---

# Una aguja en el pajar

¿Puedes encontrar la aguja en el pajar?

Escribe una función que tome un array lleno de basura pero que contenga una "aguja"

Después de que tu función encuentre la aguja debería devolver un mensaje (como una cadena) que diga:

"encontró la aguja en la posición " más el índice que encontró la aguja.

Ejemplo:
`["heno", "chatarra", "heno", "heno", "másChatarra", "aguja", "chatarraal azar"]` --> `"encontró la aguja en la posición 5"`

<div></div> <!-- .element style="height: 200px" -->

[Enlace Kata](https://www.codewars.com/kata/56676e8fabd2d1ff3000000c)
