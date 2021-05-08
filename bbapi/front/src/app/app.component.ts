import { Component } from '@angular/core';
import {UserService} from './user.service';
import {Router} from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'front';


  constructor(public userService:UserService, private router:Router){

  }
  login(username: string, password: string) {
    this.userService.login(username, password).subscribe(
      success => this.router.navigate(['home']),
      
    );
  }
  
  logout(){
   this.userService.logout();
   

  }
}
