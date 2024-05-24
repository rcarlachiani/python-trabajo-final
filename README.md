<h2>Carlachiani Rodrigo - Proyecto Final - Python #54135</h2>

La app consiste en una disquería virtual en donde podremos acceder a ella como administrador, o como cliente.

Demo: [https://www.youtube.com/watch?v=F6EdjRW6CbE](https://www.youtube.com/watch?v=3cPxkNIPN-w)

Funcionalidades cliente:

- Registrar cliente/usuario
- Realizar el login del usuario
- Editar el perfil cliente/usuario
- Ver el catálogo de productos
- Ver el detalle de los productos
- Generar órdenes de compra
- Dar de baja órdenes de compra
- Visualizar órdenes de compra asociadas al cliente/usuario

Funcionalidades administrador:

- Realizar el login del usuario
- Ver el listado de clientes/usuarios
- Ver el detalle de un cliente/usuario
- Editar cliente/usuario
- Ver el catálogo de productos
- Agregar formatos de discos
- Agregar géneros musicales
- Agregar productos
- Editar productos
- Eliminar productos
- Ver el detalle de los productos
- Dar de baja órdenes de compra
- Visualizar todas las órdenes de compra

Se encuentra creado el usuario administrador, el cual es:

- User: admin
- Pass: admin2024

Y un usuario cliente:

- User: user
- Pass: coder2024

<h2>Instrucciones para levantar la app</h2>

- $ git clone
- $ python -m venv .venv <br>
(Si 'python' no funciona, prueba 'python3')
- $ .\venv\Scripts\activate (Windows)
- $ source .venv/bin/activate (Linux/macOs)
- $ pip install -r requirements.txt
(Si 'pip' no funciona, prueba 'pip3')
- $ cd project
- $ python manage.py runserver
