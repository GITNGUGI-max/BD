import { Component, OnInit } from '@angular/core';
import {UserService} from '../user.service';
import {throwError} from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
 
  error: any;
  constructor(public userService:UserService,
    private router: Router,){

  }

  ngOnInit(){
    
  }
  login(username: string, password: string) {
    this.userService.login(username, password).subscribe(
      success => this.router.navigate(['home']),
      error => alert(' Invalid user details, do you have an account?')
    );
  }
  logout(){
   return this.userService.logout();
  }
 
}
