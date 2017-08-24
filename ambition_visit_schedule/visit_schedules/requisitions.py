from edc_visit_schedule import FormsCollection, Requisition

from ambition_labs.labs import viral_load_panel, cd4_panel, fbc_panel, csf_panel
from ambition_labs.labs import chemistry_alt_panel, chemistry_panel, csf_chemistry_panel

requisitions = FormsCollection(Requisition(
    show_order=50, model='ambition_subject.subjectrequisition',
    panel=chemistry_panel, required=False, additional=False),)

requisitions_d1 = FormsCollection(
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=viral_load_panel, required=False, additional=False),
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=cd4_panel, required=False, additional=False),
    Requisition(
        show_order=30, model='ambition_subject.subjectrequisition',
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=40, model='ambition_subject.subjectrequisition',
        panel=csf_panel, required=True, additional=False),
    Requisition(
        show_order=50, model='ambition_subject.subjectrequisition',
        panel=csf_chemistry_panel, required=True, additional=False),
    Requisition(
        show_order=60, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
)

requisitions_d3 = FormsCollection(
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=chemistry_panel),
)

requisitions_d7 = FormsCollection(
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=30, model='ambition_subject.subjectrequisition',
        panel=csf_panel, required=True, additional=False),
    Requisition(
        show_order=40, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
)

requisitions_w4 = FormsCollection(
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
)
