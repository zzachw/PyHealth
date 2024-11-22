# from .drug_recommendation import (
#     drug_recommendation_eicu_fn,
#     drug_recommendation_mimic3_fn,
#     drug_recommendation_mimic4_fn,
#     drug_recommendation_omop_fn,
# )
# from .cardiology_detect import (
#     cardiology_isAR_fn,
#     cardiology_isBBBFB_fn,
#     cardiology_isAD_fn,
#     cardiology_isCD_fn,
#     cardiology_isWA_fn,
# )
# from .temple_university_EEG_tasks import (
#     EEG_isAbnormal_fn, EEG_events_fn,
# )
# from .length_of_stay_prediction import (
#     length_of_stay_prediction_eicu_fn,
#     length_of_stay_prediction_mimic3_fn,
#     length_of_stay_prediction_mimic4_fn,
#     length_of_stay_prediction_omop_fn,
# )
from .mortality_prediction import (
    mimic3_48_ihm,
    mortality_prediction_eicu_fn,
    mortality_prediction_eicu_fn2,
    mortality_prediction_mimic3_fn,
    mortality_prediction_mimic4_fn,
    mortality_prediction_omop_fn,
)
# from .readmission_prediction import (
#     readmission_prediction_eicu_fn,
#     readmission_prediction_eicu_fn2,
#     readmission_prediction_mimic3_fn,
#     readmission_prediction_mimic4_fn,
#     readmission_prediction_omop_fn,
# )
# from .sleep_staging import (
#     sleep_staging_sleepedf_fn,
#     sleep_staging_isruc_fn,
#     sleep_staging_shhs_fn,
# )
# from .patient_linkage import patient_linkage_mimic3_fn
from .covid19_cxr_classification import COVID19CXRClassification
from .medical_transcriptions_classification import MedicalTranscriptionsClassification
from .sleep_staging_v2 import SleepStagingSleepEDF
from .mortality_prediction_v2 import Mortality30DaysMIMIC4, MIMIC3_48_IHM