# Backend con Django

Ejercicios, proyectos y notas de mi formación en desarrollo backend:
fundamentos, Flask, Django, servicios web, despliegue en servidores
remotos y contenedores.

## Stack

Python · Flask · Django · SQL · Docker

## Estructura

Una carpeta por módulo. Cada una incluye un `notas.md` con lo aprendido,
los problemas que encontré y los comandos o fragmentos de código clave.

## Progreso

- [ ] 01 · ¿Qué hace realmente un backend?
- [ ] 02 · Conceptos básicos
- [ ] 03 · Base de datos
- [ ] 04 · Flask
- [ ] 05 · Django
- [ ] 06 · Django nivel 2
- [ ] 07 · Django nivel 3
- [ ] 08 · Servicios web
- [ ] 09 · Servidores remotos
- [ ] 10 · Automatización de servidores remotos
- [ ] 11 · Contenedores
- [ ] 12 · Cierre

## Cómo levantar un proyecto de este repo

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # completar SECRET_KEY
python manage.py migrate
python manage.py runserver
```
