FROM alpine as base
RUN apk --no-cache add curl

RUN cd /opt; \
  curl -L https://github.com/kairosdb/kairosdb/releases/download/v1.3.0/kairosdb-1.3.0-1.tar.gz | \
  tar zxfp -



FROM openjdk:8-jre-slim-buster

WORKDIR /opt/kairosdb

COPY --from=base /opt/kairosdb .

EXPOSE 4242 8080

COPY kairosdb.conf conf/

CMD ./bin/kairosdb.sh run
