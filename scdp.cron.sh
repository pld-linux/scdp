#!/bin/sh

SCDP_OPTS=""

if [ -f /etc/sysconfig/scdp ]; then
	. /etc/sysconfig/scdp
fi

if [ -n "$QUIET" ] && [ "$QUIET" = "YES" ]; then
	SCDP_OPTS="-q"
fi

if [ "${INTERFACES}" ]; then
	for int in ${INTERFACES}; do
		scdp ${SCDP_OPTS} -i ${int}
	done
else
	scdp ${SCDP_OPTS}
fi
