#!/bin/sh
set -e

postconf -e "myhostname=${SERVER_HOSTNAME:-localhost}"
postconf -e "relayhost=[${RELAYHOST:-localhost}]:${RELAYHOST_PORT:-25}"

exec postfix start-fg
