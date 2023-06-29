build:
	docker build -t nodejs .
run:
	docker run -it -d -p 8000:8000 --v /cd C:\Users\BIT\Documents\GitHub

alias h='history'
alias df='df -h'
alias egrep='egrep —color=auto'
alias fgrep='fgrep —color=auto'
alias grep='grep —color=auto'
alias ls='ls -asCF —color=auto'
alias ll='ls -alF —color=auto'

export PS1='[\[\e[1;31m\]\u\[\e[m\] \[\e[1;36m\]\w\[\e[m\]]\$ '

exec:
	docker exec -it nodejs /bin/bash
start:
	docker start nodejs
stop:
	docker stop nodejs
logs:
	docker logs nodejs
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)

