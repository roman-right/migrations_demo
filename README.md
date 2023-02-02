## Insert data

```shell
python migrations_proof/insert_initial_data.py
```

## Run migration

```shell
beanie migrate -uri 'mongodb://beanie:beanie@localhost:27017' -db test_migrations_1 -p migrations
```