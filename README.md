# Monitoring Python Flask with Elastic APM

## APM Server with fingerprint authentication

```bash
docker cp <CONTAINER-ID>:/usr/share/elasticsearch/config/certs .
```

```bash
curl --cacert ./certs/ca/ca.crt -XGET -u "elastic:qualquercoisa123" 'https://localhost:9200/_cluster/health?pretty'
```

```bash
grep -v ^- ./certs/ca/ca.crt  | base64 -d | sha256sum
```

``` bash
command: >
       apm-server -e
         -E apm-server.rum.enabled=true
         -E setup.kibana.host=kibana:5601
         -E setup.template.settings.index.number_of_replicas=0
         -E apm-server.kibana.enabled=true
         -E apm-server.kibana.host=kibana:5601
         -E output.elasticsearch.hosts=["https://elasticsearch:9200"]
         -E output.elasticsearch.username="elastic"
         -E output.elasticsearch.password="qualquercoisa123"
         -E output.elasticsearch.ssl.verification_mode=none
         -E output.elasticsearch.ssl.ca_trusted_fingerprint="8844ffffd9cba687a2b9aa5a59e0e5aadf5cee56491b8895b6dd3641a6ac26f4"
```

## APM Server with API Key authentication

```bash
  # JSON
  {
  "id":"na6nlIkBCEq0ntCvXg1K",
  "name":"teste-apm",
  "api_key":"lksevi72RUKKGndSiKJDLg",
  "encoded":"bmE2bmxJa0JDRXEwbnRDdlhnMUs6bGtzZXZpNzJSVUtLR25kU2lLSkRMZw=="
   }

  # Base64
  echo "VkhrMmw0a0JwMlFRZW9NbTducmk6R09tVU52SWhSWEs4TE8zTl9OU2ZHZw==" | base64 --decode
```

``` bash
output.elasticsearch.api_key="<id:api_key>"
```

``` bash
command: >
       apm-server -e
         -E apm-server.rum.enabled=true
         -E setup.kibana.host=kibana:5601
         -E setup.template.settings.index.number_of_replicas=0
         -E apm-server.kibana.enabled=true
         -E apm-server.kibana.host=kibana:5601
         -E output.elasticsearch.hosts=["https://elasticsearch:9200"]
         -E output.elasticsearch.username="elastic"
         -E output.elasticsearch.password="qualquercoisa123"
         -E output.elasticsearch.ssl.verification_mode=none
         -E output.elasticsearch.api_key="na6nlIkBCEq0ntCvXg1K:lksevi72RUKKGndSiKJDLg"
```