# Preoyecto-Python-HelpDesk-

Este sera el repositorio donde trabajaremos, abajo pondre comandos que seran utiles para que trabajemos lo mejor posible

LA PRIMERA VEZ QUE LEAN ESTO HAGAN LO SIGUIENTE:

en su PC creen o seleccionen una carpeta donde clonar este repositorio eso de hace asi:

1. Crear una carpeta para el proyecto.
2. Abrir una terminal dentro de esa carpeta.
3. Ejecutar:
git clone https://github.com/Ricardo-Flamenco/Preoyecto-Python-HelpDesk-.git

luego metanse a la carpeta y creen su rama personal con su nombre con estos comandos:
git checkout -b nombre-rama

despues suban la rama al repositorio:
git push -u origin nombre-rama

SI YA HICIERON LO ANTERIOR CADA VEZ QUE VAYAN A PROGRAMAR HAGAN LO SIGUIENTE:

metanse a su carpeta y actualizen el repositorio:
git pull

vayan a su rama personal:
git checkout nombre-rama
¡¡SIEMPRE HACER ESTO PARA NO TRABAJAR EN LA RAMA MAIN (PRINCIPAL)!!

si no estan seguros hagan:
git branch
les diran en que rama estan mediante un *

UNA VEZ TERMINADO DE PROGRAMAR HAGAN ESTO:

*Opcional* 
git status
es para ver los cambios

git add .
seleccionan todas las carpetas para subirlas

git commit -m "Descripción de los cambios"
commit hace un guardado porfavor ser lo mas breve y descriptivo con el mensaje para no hacer desorden

git push
suben los cambios al repositorio

UNA VEZ SU RAMA ESTE TERMINADA O SU PARTE YA SEA SEGURA ESTE ES EL PROCESO DE AGREGARLA AL MAIN:

git checkout main	
te mueve de tu rama a la rama main (principal).
git pull	
Actualiza main.
git merge nombre-rama
Une su rama a la principal

#COMANDOS UTILES EXTRAS 

git log --oneline
muestra un historial de todos los commits por esto es importante ser descriptivo con los commits al lado de cada commit hay una ID 

git restore .
Deshace todos los cambios sin commit

git reset --hard ID_COMMIT
Hace que la rama quede como estaba cuando se hizo el commit (en ID_COMMIT ponga la ID del commit al que quieren volver)
Esto elimina cambios no guardados. Usarlo solo si están seguros.


