from time import sleep
import asyncio
from panoramisk import Manager

from celery import shared_task
from celery_progress.backend import ProgressRecorder


manager = Manager(loop=asyncio.get_event_loop(), host='127.0.0.1', username='taurai', password='password')


@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    # try:
    #     manager.loop.run_forever()
    # except KeyboardInterrupt:
    #     manager.loop.close()
    for i in range(115):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 115, f'On {i}')
    main().delay()
    return 'Done'


@manager.register_event('*')
def callback(manager, message):
    if "FullyBooted" not in message.event:
        """This will print every event, but the FullyBooted events as these
        will continuously spam your screen"""
        print(message)


@shared_task(bind=True)
def main():
    try:
        manager.loop.run_forever()
    except KeyboardInterrupt:
        manager.loop.close()


if __name__ == '__main__':
    main()
