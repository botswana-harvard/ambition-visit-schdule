from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule
from .week10_schedule import schedule1

app_label = 'ambition_subject'

visit_schedule = VisitSchedule(
    name='visit_schedule',
    verbose_name='Ambition',
    app_label='ambition_subject',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=None)

visit_schedule.add_schedule(schedule)

visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    verbose_name='Ambition',
    app_label='ambition_subject',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=None)

visit_schedule.add_schedule(schedule1)

site_visit_schedules.register(visit_schedule)
