# Elastic Stack APM

```bash
docker compose up -d
```

```bash
docker cp <CONTAINER-ID>:/usr/share/elasticsearch/config/certs .
```

```bash
curl --cacert ./certs/ca/ca.crt -XGET -u "elastic:qualquercoisa123" 'https://localhost:9200/_cluster/health?pretty'
```

``` bash
curl -X POST -H 'Content-Type: application/json' --cacert ./certs/ca/ca.crt -u "elastic:qualquercoisa123" -d '{"name": "my-api-key","role_descriptors": {} }' https://localhost:9200/
```

```bash
grep -v ^- ./certs/ca/ca.crt  | base64 -d | sha256sum
```