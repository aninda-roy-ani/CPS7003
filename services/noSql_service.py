from pymongo import MongoClient
from services.patient_service import PatientService
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB setup
mongo_client = MongoClient('mongodb://localhost:27017/')  # Adjust the connection string as needed
mongo_db = mongo_client['healthcare_db']
diagnosis_report_collection = mongo_db['Diagnosis_Report']


def save_data_to_mongodb(patient_id):
    try:
        patient = PatientService()
        diagnosis_report_collection.insert_one(patient.retrieve_patient_diagnostic_details(patient_id))
    except Exception as e:
        logger.error(e)


def fetch_all_diagnosis_reports():
    try:
        reports = list(diagnosis_report_collection.find())
        logger.info("Fetched all diagnosis reports successfully")
        return reports
    except Exception as e:
        logger.error("Error while fetching diagnosis reports: {}".format(str(e)))
        return []


def fetch_diagnosis_reports_by_patient_id(patient_id):
    try:
        reports = list(diagnosis_report_collection.find({"patient_info.patient_id": patient_id}))
        logger.info(f"Fetched diagnosis reports for Patient ID {patient_id} successfully")
        return reports
    except Exception as e:
        logger.error("Error while fetching diagnosis reports: {}".format(str(e)))
        return []


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

        print("  Treatment Plans:")
        for plan in diagnosis['treatment_plans']:
            print(f"    Treatment ID: {plan['treatment_id']}")
            print(f"    Details: {plan['treatment_details']}")
            print(f"    Start Date: {plan['start_date']}")
            print(f"    End Date: {plan['end_date']}")

            print("    Assigned Teams:")
            for team in plan['assigned_teams']:
                print(f"      Name: {team['name']}")
                print(f"      Role: {team['role']}")

    print("\nNote:")
    print(report.get('note', 'N/A'))


if __name__ == "__main__":
    patient_id = 1
    save_data_to_mongodb(patient_id)
    reports = fetch_diagnosis_reports_by_patient_id(patient_id)
    for report in reports:
        print_diagnosis_report(report)
