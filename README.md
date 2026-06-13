# Proyecto-Python-HelpDesk-

Este sera el repositorio donde trabajaremos, abajo pondre comandos que seran utiles para que trabajemos lo mejor posible

LA PRIMERA VEZ QUE LEAN ESTO HAGAN LO SIGUIENTE:

en su PC creen o seleccionen una carpeta donde clonar este repositorio eso de hace asi:

1. Crear una carpeta para el proyecto.
2. Abrir una terminal dentro de esa carpeta.
3. Ejecutar:

git clone https://github.com/Ricardo-Flamenco/Proyecto-Python-HelpDesk.git
(para clonar)

Entrar a la carpeta con code . hacer ctrl + ñ y en la terminal hacer estos comandos

git init
(para que inicie git)

git remote add origin https://github.com/Ricardo-Flamenco/Proyecto-Python-HelpDesk.git
(necesario para otros comandos)

git config --global user.name "Su usuario de GitHub"
git config --global user.email "El correo con el que se han registrado en GitHub"
(necesario para otros comandos)

git checkout -b nombre-rama
(crean su rama, sustituir nombre-rama con su nombre)

git add .
(seleccionar todos los archivos en tu rama para el commit)
(Aclaro que saldran muchas letras amarillas parece error pero es normal asi que IGNOREN)

git commit -m "Mensaje aqui"
(crean un commit para poder guardar la rama el mensaje puede ser: "Creacion de una nueva rama")

git push -u origin nombre-rama
(paso final crea la rama)

SALDRA ALGO DE REGISTRARSE EN NAVEGADOR O EN CODE COMO SEA PERO REGISTRENSE.



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



#COMANDOS UTILES EXTRAS 

git log --oneline
muestra un historial de todos los commits por esto es importante ser descriptivo con los commits al lado de cada commit hay una ID 

git restore .
Deshace todos los cambios sin commit

git reset --hard ID_COMMIT
Hace que la rama quede como estaba cuando se hizo el commit (en ID_COMMIT ponga la ID del commit al que quieren volver)
Esto elimina cambios no guardados. Usarlo solo si están seguros.


