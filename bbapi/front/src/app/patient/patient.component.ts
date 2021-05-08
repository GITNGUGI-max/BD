import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent implements OnInit {
  patient =[];
  counties=[];
  subCounties=[];
  selectedPatient;
  constructor(private api:ApiService) { 
    this.getCounties();
    this.getSubCounties();
    this.selectedPatient = { id:-1, patientName:'',
        hospitalName:'',
        county:'',
        subCounty:'',
        doctor:'',
        contactName:'',
        email:'',
        contactDate:'',
        requiredDate:'',
        bloodGroup:'',
        bloodUnits:'',
        contactOne:'',
        contactTwo:'',
        reason:'',
        // status:'',
        // image:''
    };
  }
  getCounties=()=>{
    return this.api.getAllCounties().subscribe(
      data=>{
        this.counties=data;

      },
      error=>{
        console.log(error);
      }
    );
  }
  getSubCounties=()=>{
    return this.api.getAllSubCounties().subscribe(
      data=>{
        this.subCounties=data;

      },
      error=>{
        console.log(error);
      }
    );
  }
  

  ngOnInit(): void {
  }

  onSubmit(){
   return this.api.registerPatient(this.selectedPatient).subscribe(
      data=>{
        this.patient.push(data);
      }
    )
  }
}
