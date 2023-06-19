build:
	docker build -t cmd .
run:
	docker run -it -d -p 8000:80 -v /docker/data:/data -v /docker/nginxsite:/etc/nginx-site-enabled -v /docker/nginxlog:/var/log/nginx cmd
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)

