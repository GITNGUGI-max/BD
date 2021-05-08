import { Component, OnInit, Input } from '@angular/core';
import {ApiService} from '../api.service';
import { Donor } from '../donor';
@Component({
  selector: 'app-donors',
  templateUrl: './donors.component.html',
  styleUrls: ['./donors.component.css']
})
export class DonorsComponent implements OnInit {
  donors=[];
  message;
  @Input() donor: Donor;
  constructor(private api:ApiService) {
  	this.getAllDonors();
    this.message;
    
   }

  ngOnInit(): void {
  }

  getAllDonors=()=>{
  	return this.api.getAllDonors().subscribe(
  		data=>{
  			this.donors=data;
  		},
  		error=>{
  			alert(error);
  		}
  	)
  }
  deleteDonor(id:number) {
    this.api.deleteDonor(id)
      .subscribe(
        data => {
          this.getAllDonors();
          this.message=`Donor ${id} deleted sucessfuly!`
          
        },
        error => console.log(error));
  }
  onClick(){
    
  }
}
