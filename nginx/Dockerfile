FROM nginx:1.21-alpine

# Remove default NGINX config
RUN rm /etc/nginx/conf.d/default.conf
# Provide our custom config
COPY nginx.conf /etc/nginx/conf.d

RUN mkdir -p /app/staticfiles