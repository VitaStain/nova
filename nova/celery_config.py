from nova.settings import env

broker_connection_retry_on_startup = True
broker_url = env("BROKER_URL")
broker_connection_max_retries = 5

timezone = "UTC"

worker_concurrency = 2
task_track_started = True
