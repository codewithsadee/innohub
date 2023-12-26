# Use the official Nginx image as the base image
FROM nginx:latest

# Copy the static HTML files to the default Nginx web root directory
COPY ./ /usr/share/nginx/html

# Expose port 80, which is the default port for Nginx
EXPOSE 80

# Command to start Nginx when the container is run
CMD ["nginx", "-g", "daemon off;"]
