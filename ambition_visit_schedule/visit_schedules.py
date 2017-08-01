from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .visit_schedule import schedule1

app_label = 'ambition_subject'

visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    verbose_name='Ambition',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy')

visit_schedule1.add_schedule(schedule1)

site_visit_schedules.register(visit_schedule1)
