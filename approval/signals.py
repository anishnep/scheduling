import django.dispatch
request_approved= django.dispatch.Signal(providing_args=["work_request_id","status"])
