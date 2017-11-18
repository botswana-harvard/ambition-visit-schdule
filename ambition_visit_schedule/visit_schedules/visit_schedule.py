from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule

app_label = 'ambition_subject'

visit_schedule = VisitSchedule(
    name='visit_schedule',
    verbose_name='Ambition',
    app_label='ambition_subject',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=None)

visit_schedule.add_schedule(schedule)

site_visit_schedules.register(visit_schedule)
