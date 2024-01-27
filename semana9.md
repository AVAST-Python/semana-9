

# Introducción a Python

## Semana 9
<!-- .element style="text-align:center" -->

![alt text](./img/logo2.png) <!-- .element style="margin-left: auto; margin-right: auto; display: block" -->

---

# Pandas

Aprieta la flecha de abajo si vas a hacer el proyecto Pandas

Enlaces:
- [Introducción a Pandas](https://aprendepython.es/pypi/datascience/pandas/)
- [Fichero para procesar](./salary_survey_2021.csv.zip)
- [Limpieza de datos en Pandas](https://realpython.com/python-data-cleaning-numpy-pandas/)

--

# Limpieza de datos

Cuando vas a trabajar con datos, esto es lo que esperas tener:

![alt text](./img/good_gift.webp) <!-- .element style="margin-left: auto; margin-right: auto; display: block; width: 40%" -->

Pero esto es lo que sueles tener:

![alt text](./img/messy_gift.webp) <!-- .element style="margin-left: auto; margin-right: auto; display: block; width: 40%" -->

--

# Ejercicio

Este es el conjunto de datos con el que te toca trabajar: [Fichero para procesar](./salary_survey_2021.csv.zip) ([vista previa](https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/edit?resourcekey&pli=1#gid=1625408792))

Esto es lo que tienes que responder:
- ¿Dónde ganan más las mujeres: en Europa o en América?
- ¿Cual es el salario medio de un hombre asiático con 5 años de experiencia que trabaje en el Estados Unidos?

Tendrás que limpiar los datos primero:
- Examina los datos, puedes usar una hoja de cálculo
- Revisa valores "raros" y cosas incoherentes
- Decide qué tienes que modificar
- Realiza las modificaciones usando pandas
- Bienvenido al Mundo Real<sup>©</sup>

En la siguiente página tienes algunos enlaces con información y ejemplos.

--

# Ejemplos e información

- https://realpython.com/python-data-cleaning-numpy-pandas/
- https://www.linkedin.com/pulse/limpieza-de-datos-con-python-un-ejemplo-completo-para-luis-jos%C3%A9
- Proyectos de práctica: https://www.datawars.io/articles/12-free-data-science-projects-to-practice-python-and-pandas

---

# Una aguja en el pajar
#### (continuacion) <!-- .element style="text-align: center; margin-bottom: 40px" -->

Repaso:
- ¿Os acordáis cómo definir una función y cómo llamarla?
- ¿Cómo sabremos si la función está bien?
- ¿Os acordáis de qué era un array?
- ¿Cómo hacíamos para repetir algo varias veces?

-----

**¿Puedes encontrar la aguja en el pajar?**

Escribe una función que tome un array lleno de basura pero que contenga una "aguja"

Después de que tu función encuentre la aguja debería devolver un mensaje (como una cadena) que diga:

`"encontró la aguja en la posición"` más el índice que encontró la aguja.

Ejemplo:
`["heno", "chatarra", "heno", "heno", "másChatarra", "aguja", "chatarraal azar"]` --> `"encontró la aguja en la posición 5"`

<div></div> <!-- .element style="height: 200px" -->

[Enlace Kata](https://www.codewars.com/kata/56676e8fabd2d1ff3000000c)


---

# Ordenamiento pseudoalfabético

> He preparado un programa que ordena los números del 1 al 100 en orden alfabético
> es decir: primero los que empiezan por 1, luego por 2, etc. Los que empiezan
> por el mismo dígito los reordena por el dígito que viene a continuación. Así,
> los números quedarían: 1, 10, 100, 11, 12...

¿En qué números coincide el orden numérico con el alfabético?


---

# ¿Cómo de buena eres realmente?

Había un examen en tu clase y lo has aprobado. ¡Enhorabuena!

Pero eres una persona ambiciosa. Quieres saber si eres mejor que el alumno medio de tu clase.

Recibes las puntuaciones de los exámenes de tus compañeros. Ahora calcula la media y compara tu puntuación.
Devuelve `True` si eres mejor, si no, `False`.

<div></div> <!-- .element style="height: 200px" -->

[Enlace Kata](https://www.codewars.com/kata/5601409514fc93442500010b)
