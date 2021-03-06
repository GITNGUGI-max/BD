import { Component, OnInit } from '@angular/core';
import {UserService} from '../user.service';
import {Router} from '@angular/router';
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  error:any;
  constructor(private userService:UserService, private router:Router){
    }
  
  ngOnInit(){}
  signup(username:string, email:string, password1:string, password2:string){
    this.userService.signUp(username, email, password1, password2).subscribe(
        success=>this.router.navigate(['home']),
        error => this.error =error
    );
  }
  
  
  
  

}
