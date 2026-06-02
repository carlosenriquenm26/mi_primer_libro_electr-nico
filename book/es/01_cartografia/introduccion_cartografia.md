# Introducción a la Cartografía Geológica

```{admonition} Objetivos de aprendizaje
:class: important

Al finalizar este capítulo, serás capaz de:
1. Comprender la importancia de la cartografía geológica en las ciencias de la Tierra.
2. Identificar y medir la orientación espacial de los planos geológicos (rumbo, dirección de buzamiento y buzamiento).
3. Interpretar la simbología básica en un mapa geológico.
4. Resolver problemas conceptuales sencillos sobre la disposición espacial del terreno.
```

---

## 1. ¿Qué es un Mapa Geológico?

Un **mapa geológico** es la representación bidimensional, a escala, de la distribución espacial de las diferentes unidades de roca (o sedimentos) que afloran en la superficie terrestre, así como de las estructuras geológicas que las afectan (pliegues, fallas, discordancias).

A diferencia de un mapa topográfico convencional, un mapa geológico proporciona una proyección de la **tercera dimensión** hacia el subsuelo mediante la interpretación de la geometría de los contactos.

---

## 2. Orientación de Planos: Rumbo, Buzamiento y Dirección de Buzamiento

Para caracterizar estructuralmente cualquier plano en geología (como un estrato de roca o una falla), se utilizan tres parámetros angulares medidos con la brújula de geólogo:

*   **Rumbo (Dirección del estrato):** Ángulo horizontal entre el norte magnético y la línea de intersección del plano geológico con un plano horizontal virtual.
*   **Buzamiento (Inclinación):** El ángulo de máxima pendiente medido verticalmente entre el plano horizontal y el plano geológico. Varía entre $0^\circ$ (horizontal) y $90^\circ$ (vertical).
*   **Dirección de buzamiento (Sentido de inclinación):** Dirección de la proyección horizontal de la línea de máxima pendiente. Es siempre perpendicular al rumbo ($90^\circ$ a la derecha o izquierda).

### Relación matemática del Buzamiento Aparente

Si medimos la inclinación en una dirección que no es perpendicular al rumbo, obtendremos un **buzamiento aparente** ($\alpha$), el cual siempre es menor o igual que el **buzamiento real** ($\beta$). La relación matemática viene dada por:

$$
\tan(\alpha) = \tan(\beta) \cdot \sin(\theta)
$$

Donde:
*   $\alpha$ es el buzamiento aparente.
*   $\beta$ es el buzamiento real.
*   $\theta$ es el ángulo horizontal entre la dirección del rumbo y la dirección en la que se mide el buzamiento aparente.

---

## 3. Tipos de Contactos Geológicos

La relación geométrica entre diferentes unidades rocosas define el tipo de contacto. A continuación se esquematizan las relaciones de contactos más habituales:

Como muestra la {numref}`fig-diagrama-01-cartografia-introduccion-cartografia-01`, el diagrama queda versionado como imagen estática.

```{figure} ../../_static/generated/diagrams/es/01_cartografia_introduccion_cartografia_01.svg
:name: fig-diagrama-01-cartografia-introduccion-cartografia-01
:alt: Diagrama generado desde código
:width: 90%
:align: center

Diagrama generado desde código.
```

---

## 4. La Ley de las "V" en Cartografía

Una de las reglas fundamentales para interpretar la disposición espacial de los estratos a partir de su traza en superficie es la **Ley de las V**:

> *Cuando un estrato inclinado cruza un valle topográfico, la traza de su contacto dibuja una forma de **V** cuya punta señala en la dirección del buzamiento del plano (salvo contadas excepciones donde la pendiente del valle es mayor que el buzamiento).*

*   **Estratos Horizontales:** Las trazas de los contactos son paralelas a las curvas de nivel topográficas.
*   **Estratos Verticales:** Las trazas de los contactos se representan como líneas rectas sobre el mapa, ignorando por completo la topografía del terreno.

---

## 5. Ejercicios de Autoevaluación

```{admonition} Pregunta conceptual: Buzamiento Aparente
:class: tip, dropdown

**Enunciado:** Si un estrato tiene un buzamiento real de $30^\circ$ en dirección Este, ¿cuál será su buzamiento aparente si lo observamos en un corte del terreno orientado exactamente en dirección Norte-Sur?

**Solución:**
Dado que el rumbo del estrato es Norte-Sur (perpendicular a la dirección de buzamiento Este), la dirección de observación (Norte-Sur) es paralela al rumbo del estrato.
El ángulo $\theta$ entre la dirección del rumbo y la dirección de observación es $0^\circ$.

Aplicando la fórmula:
$$
\tan(\alpha) = \tan(30^\circ) \cdot \sin(0^\circ) = 0 \implies \alpha = 0^\circ
$$

Por lo tanto, en un plano de corte paralelo al rumbo, el estrato se observará completamente horizontal (buzamiento aparente de $0^\circ$).
```

---

## 6. Futura Batería de Ejercicios Prácticos

En las próximas actualizaciones de este libro interactivo, se incorporarán herramientas computacionales y cuadernos ejecutables de Python para resolver:

1.  **Problema de los tres puntos:** Cálculo de la dirección y buzamiento de un plano a partir de tres cotas conocidas.
2.  **Generación de Perfiles Geológicos:** Construcción automatizada de secciones transversales a partir del perfil topográfico y las trazas del mapa.
3.  **Líneas de contorno estructural:** Trazado automático de contactos mediante interpolación espacial.
