import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';
import {Router} from '@angular/router';
@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
  sender=[];
  selectedSender;	
  constructor(private api:ApiService, private router:Router) {
  	this.selectedSender={id:-1, sender:'', senderName:'', senderEmail:'', contact:'', sentDate:'', message:''};
   }

  ngOnInit(): void {
  
  }

  onSubmit(){
	return this.api.sendMessage(this.selectedSender).subscribe(
		data=>{
			alert('Message sent successivly!');
		},
    success=>{
       this.router.navigate(['home'])
    }
	)  
  }
}
