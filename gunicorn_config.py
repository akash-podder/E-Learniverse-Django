# gunicorn_config.py
import multiprocessing

bind = '0.0.0.0:7777'
# workers = multiprocessing.cpu_count() * 2 + 1