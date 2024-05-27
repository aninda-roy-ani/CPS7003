from database.mongodb_database import get_mongo_client

from services.patient_service import PatientService
from services.diagnosis_service import DiagnosisService
from services.treatment_plan_service import TreatmentPlanService
from services.treatment_team_assignment_service import TreatmentTeamAssignmentService
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def print_diagnosis_report(report):
    print("Patient Info:")
    print(f"ID: {report['patient_info']['patient_id']}")
    print(f"Name: {report['patient_info']['patient_name']}")
    print(f"Date of Birth: {report['patient_info']['date_of_birth']}")
    print(f"Gender: {report['patient_info']['gender']}")
    print(f"Contact No: {report['patient_info']['contact_no']}")
    print(f"Address: {report['patient_info']['address']}")

    print("\nDiagnosis:")
    for diagnosis in report['diagnosis']:
        print(f"  Diagnosis ID: {diagnosis['diagnosis_id']}")
        print(f"  Details: {diagnosis['diagnosis_details']}")
        print(f"  Date: {diagnosis['diagnosis_date']}")
        print(f"  Result: {diagnosis.get('result', 'N/A')}")

        print("\n  Treatment Plans:")
        for plan in diagnosis['treatment_plans']:
            print(f"    Treatment ID: {plan['treatment_id']}")
            print(f"    Details: {plan['treatment_details']}")
            print(f"    Start Date: {plan['start_date']}")
            print(f"    End Date: {plan['end_date']}")

            print("\n    Assigned Teams:")
            for team in plan['assigned_teams']:
                print(f"      Name: {team['name']}")
                print(f"      Role: {team['role']}")

    print("\nNote:")
    print(report.get('note', 'N/A'))


class DiagnosisReportService:
    def __init__(self):
        self.patient = PatientService()
        self.diagnosis = DiagnosisService()
        self.plan = TreatmentPlanService()
        self.assignment = TreatmentTeamAssignmentService()
        self.mongo_db = get_mongo_client()
        self.diagnosis_report_collection = self.mongo_db['Diagnosis_Report_Collection']

    def check_pending_reports(self):
        patients = self.patient.retrieve_all_patients()
        pending_patients_id = []
        for p in patients:
            diagnoses = self.diagnosis.retrieve_diagnoses_by_patient_id(p.patient_id)
            plans = self.plan.retrieve_treatment_plan_by_patient_id(p.patient_id)
            assignments = self.assignment.retrieve_assignment_by_patient_id(p.patient_id)
            if diagnoses and plans and assignments:
                if p.patient_id not in self.check_available_reports():
                    pending_patients_id.append(p.patient_id)
        return pending_patients_id

    def save_new_report(self, patient_id):
        try:
            report = self.diagnosis_report_collection.find_one({"patient_info.patient_id": patient_id})
            if report:
                data = self.patient.retrieve_patient_diagnostic_details(patient_id)
                data['_id'] = report['_id']
                self.diagnosis_report_collection.replace_one({"patient_info.patient_id": patient_id}, data)
            logging.info(f"Patient diagnosis report saved: {patient_id}")
        except Exception as e:
            logger.error(e)

    def check_available_reports(self):
        try:
            reports = list(self.diagnosis_report_collection.find())
            patient_ids = []
            for report in reports:
                patient_ids.append(report['patient_info']['patient_id'])
            return patient_ids
        except Exception as e:
            logger.error("Error while fetching diagnosis reports: {}".format(str(e)))
            return None

    def print_diagnosis_report(self, patient_id):
        try:
            report = self.diagnosis_report_collection.find_one({"patient_info.patient_id": patient_id})
            if report:
                print_diagnosis_report(report)
            else:
                logger.error(f"No diagnosis report found with patient ID: {patient_id}")
        except Exception as e:
            logger.error("Error while fetching diagnosis reports: {}".format(str(e)))


if __name__ == "__main__":
    #patient_id = 2
    #save_data_to_mongodb(patient_id)
    #reports = fetch_diagnosis_reports_by_patient_id(patient_id)
    #for report in reports:
    #    print_diagnosis_report(report)
    x = DiagnosisReportService()
    print(x.check_available_reports())
    print(x.check_pending_reports())
    x.save_new_report(1)
    x.print_diagnosis_report(1)

