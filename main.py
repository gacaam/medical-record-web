from fastapi import FastAPI, Path, Query, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class MedicalRecord(BaseModel):
    patient_name : str
    gender : str
    date_of_birth : date
    diagnosis : str
    notes: Optional[str] = None

class UpdateMR(BaseModel):
    patient_name : Optional[str] = None
    gender : Optional[str] = None
    date_of_birth : Optional[date] = None
    diagnosis : Optional[str] = None
    notes: Optional[str] = None

medical_database = {}

@app.get("/")
def home():
     return HTMLResponse(content=open("static/index.html").read())

@app.get("/database")
def database_page():
    return HTMLResponse(content=open("static/database.html").read())

@app.get("/get-all-records")
def get_all_records():
    return medical_database

@app.get("/get-record/{patient_id}")
def get_record(patient_id : int = Path(..., description="The ID of the medical record to get")):
    return medical_database[patient_id]

@app.get("/get-by-patient-name/")
def get_record(patient_name : str = Query(None, title = "Patient Name")):
    for patient_id in medical_database:
        if medical_database[patient_id].patient_name == patient_name:
            return medical_database[patient_id]
    raise HTTPException(status_code=404, detail=f"Record with patient name '{patient_name}' not found.")

@app.get("/create-record-form")
def create_record_form():
    return HTMLResponse(content=open("static/create_record.html").read())

@app.post("/create-record/{patient_id}")
def create_record(patient_id : int, medical_record : MedicalRecord):
    if patient_id in medical_database:
        raise HTTPException(status_code=400, detail=f"Record with ID {patient_id} already exists.")

    medical_database[patient_id] = medical_record
    return medical_record.dict()

@app.get("/edit-record/{record_id}")
def edit_record_page(record_id: int):
    return HTMLResponse(content=open("static/edit_record.html").read())

@app.put("/update-record/{patient_id}")
def update_record(patient_id : int, new_data : UpdateMR):
    if patient_id not in medical_database:
        raise HTTPException(status_code=404, detail=f"Record with ID {patient_id} does not exist.")
    
    record = medical_database[patient_id]

    if new_data.patient_name is not None:
        record.patient_name = new_data.patient_name

    if new_data.gender is not None:
        record.gender = new_data.gender

    if new_data.date_of_birth is not None:
        record.date_of_birth = new_data.date_of_birth

    if new_data.diagnosis is not None:
        record.diagnosis = new_data.diagnosis

    if new_data.notes is not None:
        record.notes = new_data.notes

    return record.dict()

@app.delete("/delete-record")
def delete_record(patient_id : int = Query(..., description="The ID of the medical record to delete")):
    if patient_id not in medical_database:
        raise HTTPException(status_code=404, detail=f"Record with ID {patient_id} does not exist.")

    del medical_database[patient_id]
    return {"Success" : "Record deleted."}
