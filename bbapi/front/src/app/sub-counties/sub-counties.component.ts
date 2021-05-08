import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
@Component({
  selector: 'app-sub-counties',
  templateUrl: './sub-counties.component.html',
  styleUrls: ['./sub-counties.component.css']
})
export class SubCountiesComponent implements OnInit {
	 subCounties=[];

  constructor(private api:ApiService) {
  	this.getSubCounties();
   }

  ngOnInit(): void {
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
}
