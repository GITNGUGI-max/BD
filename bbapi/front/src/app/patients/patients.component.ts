import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
@Component({
  selector: 'app-patients',
  templateUrl: './patients.component.html',
  styleUrls: ['./patients.component.css']
})
export class PatientsComponent implements OnInit {
	patients=[];
	message;
  constructor(private api:ApiService) {
  	this.getAllPatients();
   }

  ngOnInit(): void {
  }
  getAllPatients=()=>{
  	return this.api.getAllPatients().subscribe(
  		data=>{
  			this.patients=data;
  		},
  		error=>{
  			alert(error);
  		}
  	)
  }
  deletePatient(id:number){
    return this.api.deletePatient(id).subscribe(
      data=>{
        this.getAllPatients();
          this.message=`Patient ${id} deleted sucessfuly!`
      }
    );
  }
}
