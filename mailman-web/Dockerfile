FROM maxking/mailman-web:0.5

RUN sed -i 's|psql -P pager=off $DATABASE_URL -c .\\l.|pg_isready -d $DATABASE_URL|' \
        /usr/local/bin/docker-entrypoint.sh
