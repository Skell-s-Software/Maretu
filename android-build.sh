#!/usr/bin/env bash
set -euo pipefail

# Activar la venv local si existe
if [ -f ".venv/bin/activate" ]; then
	# shellcheck disable=SC1091
	source .venv/bin/activate
fi

# Si hay un .env en la raíz del proyecto, cópialo a src/.env para que Flet
# lo incluya en el paquete (Flet empaqueta normalmente el contenido de `src`).
if [ -f ".env" ]; then
	mkdir -p src
	cp .env src/.env
	echo "Copied .env -> src/.env"
else
	# Si no existe .env, intentar crear src/.env a partir de variables de entorno
	if [ -n "${USUARIODB-}" ]; then
		mkdir -p src
		cat > src/.env <<EOF
USUARIODB=${USUARIODB}
PWUSUARIODB=${PWUSUARIODB}
URL=${URL}
PUERTO=${PUERTO}
BASE=${BASE}
EOF
		echo "Created src/.env from environment variables"
	else
		echo ".env not found and required env vars are empty. Proceeding without src/.env"
	fi
fi

# Ejecutar el empaquetado Android
flet build apk

# Limpiar el archivo temporal para no dejar credenciales en el árbol de trabajo
rm -f src/.env || true
echo "Build finished (src/.env removed)"