import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
@Component({
  selector: 'app-counties',
  templateUrl: './counties.component.html',
  styleUrls: ['./counties.component.css']
})
export class CountiesComponent implements OnInit {
    counties = [];	
  constructor(private api:ApiService) {
  	this.getCounties();
   }

  ngOnInit(): void {
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
}
