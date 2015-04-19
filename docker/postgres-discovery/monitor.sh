json=$(cat << END
{
    "hostname": "${POSTGRES_HOSTNAME}", 
    "ipv4_addr": "${COREOS_PRIVATE_IPV4}", 
    "username": "${POSTGRES_USERNAME}", 
    "password": "${POSTGRES_PASSWORD}", 
    "port": ${POSTGRES_PORT},
    "database": "${POSTGRES_DATABASE}"
}
END
)

while true; do
    psql -lqt -h ${COREOS_PRIVATE_IPV4} -U ${POSTGRES_USERNAME} | \
        cut -d \| -f 1 | grep -qw ${POSTGRES_DATABASE};

    if [ $? -eq 0 ]; then
        etcdctl --peers http://172.17.42.1:4001 set \
            /services/postgres "${json}" --ttl 30;
    else
        etcdctl --peers http://172.17.42.1:4001 rm /services/postgres;
    fi;
    sleep 20;
done
