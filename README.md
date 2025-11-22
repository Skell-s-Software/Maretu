# Skell's Maretu

![Static Badge](https://badgers.space/badge/Python/+3.14/blue)
![Static Badge](https://badgers.space/badge/Library/DJango/darkgreen)
![Static Badge](https://badgers.space/badge/DataBase/MariaDB/green)
![Static Badge](https://badgers.space/badge/License/MIT/orange)
![Static Badge](https://badgers.space/github/release/Skell-s-Software/Maretu)

> Powered by badgers.space

## ¿Qué es "Skell's MARETU"?

> ¡Trabaja cómodo, trabaja fácil, trabaja mejor con MARETU!

"Skell's MARETU" es la "evolución" del concepto de "Skell's ADO", priorizando el rendimiento y la seguridad para maxificar la productividad y control.

## ¿Por qué "Skell's MARETU"?

Durante el transcurso de desarrollo de "Skell's ADO" se presentaron diversas problemáticas ocasionadas por la naturaleza de la librería de interfaz web (streamlit) y su mantenibilidad, al tratarse de una librería diseñada mayormente para uso personal y prototipado, su escalabilidad a nivel comercial se dificultaría en gran medida si no se modificaba internamente a la misma o se manipulaba su renderizado, era más conveniente tomar el concepto de ADO y redefinirlo mediante DJango para poseer un control total, rendimiento y seguridad aún mayor al ofrecido por Streamlit.

ADO ha sido desarrollada en solitario, así que su infraestructura estaba muy poco documentada, o al menos no correctamente así que la mantenibilidad y legibilidad del código para otros programadores era muy complicada como para poder desarrollar sobre lo existente sin conflictos ni complicaciones.

A continuación a comparativa estimada de ADO con lo que pretende alcanzar MARETU
```mermaid
---
title: "Comparativa con ADO"
---
radar-beta
  axis e["Escalabilidad"], m["Mantenibilidad"], s["Seguridad"], v["Velocidad"], r["Rendimiento"]
  curve a["ADO"]{7, 2, 5, 6, 5}
  curve b["Maretu"]{9, 7, 8, 7.5, 6.5}
  max 8
  min 0
