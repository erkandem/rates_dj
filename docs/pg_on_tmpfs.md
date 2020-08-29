
https://severalnines.com/blog/benchmarking-postgresql-performance
https://vladmihalcea.com/how-to-run-integration-tests-at-warp-speed-with-docker-and-tmpfs/
docker pull postgres:13
docker run --name pg_tmpfs -p 5433:5432 --tmpfs /var/lib/postgresql/data:rw -e POSTGRES_PASSWORD=postgres -d postgres:13
docker run --name pg_hard -p 5434:5432 -e POSTGRES_PASSWORD=postgres -d postgres:13

$ pgbench -c 10 -T 60 -U postgres -h localhost -p 5433
Password:
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 1
query mode: simple
number of clients: 10
number of threads: 1
duration: 60 s
number of transactions actually processed: 89216
latency average = 6.726 ms
tps = 1486.706242 (including connections establishing)
tps = 1486.784502 (excluding connections establishing)

$ pgbench -c 10 -T 60 -U postgres -h localhost -p 5434
Password:
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 1
query mode: simple
number of clients: 10
number of threads: 1
duration: 60 s
number of transactions actually processed: 44598
latency average = 13.464 ms
tps = 742.721489 (including connections establishing)
tps = 742.781063 (excluding connections establishing)
