FROM maxking/mailman-core:0.5

RUN apk add --no-cache postfix \
 && sed -i \
        -e 's|psql -P pager=off $DATABASE_URL -c .\\l.|pg_isready -d $DATABASE_URL|' \
        -e 's|/opt/mailman/mailman-extra.cfg|/etc/mailman/mailman-extra.cfg|g' \
        /usr/local/bin/docker-entrypoint.sh
