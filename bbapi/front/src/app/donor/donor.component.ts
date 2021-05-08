import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
@Component({
  selector: 'app-donor',
  templateUrl: './donor.component.html',
  styleUrls: ['./donor.component.css']
})
export class DonorComponent implements OnInit {

  counties = [];
  subCounties=[];
  donor=[];
  selectedDonor;
  
  
  constructor(private api:ApiService) {
      this.getCounties();
      this.getSubCounties();
      this.selectedDonor = { id:-1, donorName:'',
        parentName:'',
        gender:'',
        dateOfBirth:'',
        bloodGroup:'',
        weight:'',
        email:'',
        county:'',
        subCounty:'',
        location:'',
        contactOne:'',
        contactTwo:'',
        voluntary:'',
        newDonor:'',
        lastDonated:'',
        // image:''
      
     
    };}
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
  
  ngOnInit(){

  }
  
  onSubmit(){
    return this.api.register(this.selectedDonor).subscribe(
      data=>{
        console.log(this.selectedDonor.value);
      }
    )
  }

}
