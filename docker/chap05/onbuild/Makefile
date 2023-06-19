build-base:
	docker build -t web-base -f Dockerfile.base .
build:
	docker build -t photoview .
inspect:
	docker insepct --format="{{.Config.OnBuild}}" Web-base
run:
	docker run -it -d -p 8000:80 photoview 
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)

