from ambition_labs import chemistry_alt_panel, chemistry_panel, csf_chemistry_panel
from ambition_labs import pk_plasma_panel_t12, pk_plasma_panel_t23
from ambition_labs import pk_plasma_panel_t2, pk_plasma_panel_t4, pk_plasma_panel_t7
from ambition_labs import qpcr_blood_panel
from ambition_labs import serum_panel, plasma_buffycoat_panel, csf_pkpd_panel, wb_panel
from ambition_labs import viral_load_panel, cd4_panel, fbc_panel, csf_panel
from edc_visit_schedule import FormsCollection, Requisition

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
        panel=csf_pkpd_panel, required=True, additional=False),
    Requisition(
        show_order=70, model='ambition_subject.subjectrequisition',
        panel=wb_panel, required=True, additional=False),
    Requisition(
        show_order=80, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
    Requisition(
        show_order=90, model='ambition_subject.subjectrequisition',
        panel=serum_panel, required=True, additional=False),
    Requisition(
        show_order=100, model='ambition_subject.subjectrequisition',
        panel=plasma_buffycoat_panel, required=True, additional=False),
    Requisition(
        show_order=110, model='ambition_subject.subjectrequisition',
        panel=qpcr_blood_panel, required=True, additional=False),
    Requisition(
        show_order=120, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t2, required=True, additional=False),
    Requisition(
        show_order=130, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t4, required=True, additional=False),
    Requisition(
        show_order=140, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t7, required=True, additional=False),
    Requisition(
        show_order=150, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t12, required=True, additional=False),
    Requisition(
        show_order=160, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t23, required=True, additional=False),
)

requisitions_d3 = FormsCollection(
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=chemistry_panel, required=True, additional=False),
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=plasma_buffycoat_panel, required=True, additional=False),
    Requisition(
        show_order=30, model='ambition_subject.subjectrequisition',
        panel=qpcr_blood_panel, required=True, additional=False),
)

requisitions_other = FormsCollection(
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=chemistry_panel, required=True, additional=False),
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
        panel=csf_pkpd_panel, required=True, additional=False),
    Requisition(
        show_order=50, model='ambition_subject.subjectrequisition',
        panel=plasma_buffycoat_panel, required=True, additional=False),
    Requisition(
        show_order=60, model='ambition_subject.subjectrequisition',
        panel=qpcr_blood_panel, required=True, additional=False),
    Requisition(
        show_order=70, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t2, required=True, additional=False),
    Requisition(
        show_order=80, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t4, required=True, additional=False),
    Requisition(
        show_order=90, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t7, required=True, additional=False),
    Requisition(
        show_order=100, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t12, required=True, additional=False),
    Requisition(
        show_order=110, model='ambition_subject.subjectrequisition',
        panel=pk_plasma_panel_t23, required=True, additional=False),
)

requisitions_w4 = FormsCollection(
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
)
