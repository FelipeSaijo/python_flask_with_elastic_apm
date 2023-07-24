# Elastic Stack APM

```bash
docker compose up -d
```

```bash
docker cp <CONTAINER-ID>:/usr/share/elasticsearch/config/certs .
```

```bash
curl --cacert ./certs/ca/ca.crt -XGET -u elastic 'https://localhost:9200/_cluster/health?pretty'
```

```bash
openssl x509 -fingerprint -sha256 -noout -in ./certs/ca/ca.crt | awk --field-separator="=" '{print $2}' | sed 's/://g'
```