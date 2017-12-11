from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..constants import DAY1, DAY3, DAY5, DAY7, DAY14, DAY12, DAY10
from ..constants import WEEK16, WEEK10, WEEK8, WEEK6, WEEK4
from .crfs import (
    crfs_d5, crfs_d1, crfs_d3, crfs_d7, crfs_d10, crfs_d12, crfs_d14,
    crfs_w4, crfs_w6, crfs_w8, crfs_w10, crfs_w16, crfs_unscheduled)
from .requisitions import (requisitions, requisitions_d1, requisitions_d3,
                           requisitions_d7, requisitions_w4, requisitions_d14,
                           requisitions_other)

# schedule for new participants
schedule = Schedule(
    name='schedule',
    title='Ambition',
    enrollment_model='ambition_subject.enrollment',
    disenrollment_model='ambition_subject.disenrollment',
)

visit0 = Visit(
    code=DAY1,
    title='Day 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    crfs=crfs_d1,
    requisitions=requisitions_d1,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='7-day clinic',
    allow_unscheduled=True,
)

visit1 = Visit(
    code=DAY3,
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d3,
    crfs=crfs_d3,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='7-day clinic',
)

visit2 = Visit(
    code=DAY5,
    title='Day 5',
    timepoint=2,
    rbase=relativedelta(days=4),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_other,
    crfs=crfs_d5,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='7-day clinic',
)

visit3 = Visit(
    code=DAY7,
    title='Day 7',
    timepoint=3,
    rbase=relativedelta(days=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d7,
    crfs=crfs_d7,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='7-day clinic',
)

visit4 = Visit(
    code=DAY10,
    title='Day 10',
    timepoint=4,
    rbase=relativedelta(days=9),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_other,
    crfs=crfs_d10,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='7-day clinic',
)

visit5 = Visit(
    code=DAY12,
    title='Day 12',
    timepoint=5,
    rbase=relativedelta(days=11),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_other,
    crfs=crfs_d12,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='7-day clinic'
)

visit6 = Visit(
    code=DAY14,
    title='Day 14',
    timepoint=6,
    rbase=relativedelta(days=13),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_d14,
    crfs=crfs_d14,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='7-day clinic',
    allow_unscheduled=True)

visit7 = Visit(
    code=WEEK4,
    title='Week 4',
    timepoint=7,
    rbase=relativedelta(weeks=4),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_w4,
    crfs=crfs_w4,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='5-day clinic',
    allow_unscheduled=True)

visit8 = Visit(
    code=WEEK6,
    title='Week 6',
    timepoint=8,
    rbase=relativedelta(weeks=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w6,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='5-day clinic',
    allow_unscheduled=True)

visit9 = Visit(
    code=WEEK8,
    title='Week 8',
    timepoint=9,
    rbase=relativedelta(weeks=8),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w8,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='5-day clinic',
    allow_unscheduled=True)

visit10 = Visit(
    code=WEEK10,
    title='Week 10',
    timepoint=10,
    rbase=relativedelta(weeks=10),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w10,
    crfs_unscheduled=crfs_unscheduled,
    requisitions_unscheduled=requisitions,
    facility_name='5-day clinic',
    allow_unscheduled=True)

visit16 = Visit(
    code=WEEK16,
    title='Week 16',
    timepoint=16,
    rbase=relativedelta(weeks=16),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crfs_w16,
    crfs_unscheduled=crfs_unscheduled,
    facility_name='5-day clinic',
    requisitions_unscheduled=requisitions,
)

schedule.add_visit(visit=visit0)
schedule.add_visit(visit=visit1)
schedule.add_visit(visit=visit2)
schedule.add_visit(visit=visit3)
schedule.add_visit(visit=visit4)
schedule.add_visit(visit=visit5)
schedule.add_visit(visit=visit6)
schedule.add_visit(visit=visit7)
schedule.add_visit(visit=visit8)
schedule.add_visit(visit=visit9)
schedule.add_visit(visit=visit10)
schedule.add_visit(visit=visit16)
