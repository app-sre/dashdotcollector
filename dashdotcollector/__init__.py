from dashdotcollector.core.app import app
from dashdotcollector.tasks import imagemanifestvuln


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(schedule=10.0,
                             sig=imagemanifestvuln.run.s(),
                             name='imagemanifestvul')
