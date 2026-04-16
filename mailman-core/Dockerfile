FROM maxking/mailman-core:0.5

COPY mailman-provision.sh /usr/local/bin/
COPY postmap /usr/sbin/

RUN sed -i \
        -e 's|psql -P pager=off $DATABASE_URL -c .\\l.|pg_isready -d $DATABASE_URL|' \
        -e 's|/opt/mailman/mailman-extra.cfg|/etc/mailman/mailman-extra.cfg|g' \
        -e 's|exec \$@|/usr/local/bin/mailman-provision.sh\nexec $@|' \
        /usr/local/bin/docker-entrypoint.sh
