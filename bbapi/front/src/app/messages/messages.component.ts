import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})
export class MessagesComponent implements OnInit {
	messages=[];
	error:any;
  message;
  constructor(private api:ApiService) { 
  	this.getAllMessages();
  }

  ngOnInit(): void {
  }
  getAllMessages=()=>{
  	return this.api.getAllMessages().subscribe(
  		data=>{
  			this.messages=data;
  		}
  	)
  }
  deleteMessage(id:number){
    return this.api.deleteMessage(id).subscribe(
      data=>{
        this.getAllMessages();
          this.message=`Message ${id} deleted sucessfuly!`
      }
    );
  }
}
