- Crear repositorio en github
- Luego inicializar repositorio local

```
git init
```

- Agregar el repositorio remoto

```
git remote add origin https://github.com/rcaichihua/cotizacion_scraping.git
```

- Agregar el stage

```
git add .
```

- Un dato, se agrega el sigueinte comando para deshacer un commit en donde despues del ~ se agrega el numero de commit a deshacer pero solo se hace si no se hizo el push al origin ademas al poner --soft se deshace el commit pero sin borrar los cambios que se hayan hecho en cada commit, por ejemplo si seshago hasta 20 commits con --soft los cambiso realizados en los 20 commits se quedan.

```
git reset --soft HEAD~1
```

-Luego de hacer puros git reset hasta llegar al primer commit y se desea eliminar el primer commit porque al llegar al commit 1 no se va poder deshacer con el git reset normal se va tener que ejecutar el siguiete comando para poner tu proyecto como si nunca hubieses lebvantado un solo commit.

```
git update-ref -d HEAD
```

-ahora hay que hacer el commit y el push al origin

```
git commit -m "Se agrega el primer commit."
```

-ahora se hace el primer push pero en el caso no te deje realizar el push al origin, en ese caso hay que hacer un force.

```
git push origin main --force
```
