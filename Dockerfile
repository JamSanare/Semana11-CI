# Imagen de la aplicación TiendaDemo: sitio estático servido con nginx.
FROM nginx:1.27-alpine

COPY app/ /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=5s --timeout=3s --retries=12 \
  CMD wget -qO- http://127.0.0.1/tienda_demo.html >/dev/null || exit 1
