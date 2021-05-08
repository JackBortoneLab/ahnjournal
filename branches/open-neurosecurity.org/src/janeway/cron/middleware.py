from cron import models
from django.conf import settings


class CronMiddleware(object):

    @staticmethod
    def process_request(request):
        """ This middleware class calls the Cron runner to process scheduled tasks (like emails)

        :param request: the current request
        :return: None
        """
        if not settings.DEBUG:
            try:
                models.CronTask.run_tasks()
            except BaseException:
                pass
        else:
            models.CronTask.run_tasks()
