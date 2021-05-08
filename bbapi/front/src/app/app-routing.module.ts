import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HttpClientModule} from '@angular/common/http';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { DonorComponent } from './donor/donor.component';
import { PatientComponent } from './patient/patient.component';
import { AdminComponent } from './admin/admin.component';
import { ContactComponent } from './contact/contact.component';
import { LoginComponent } from './login/login.component';
import { CountiesComponent } from './counties/counties.component';
import { SubCountiesComponent } from './sub-counties/sub-counties.component';
import { PatientsComponent } from './patients/patients.component';
import { DonorsComponent } from './donors/donors.component';
import { MessagesComponent } from './messages/messages.component';
import { ConnectComponent } from './connect/connect.component';

import { SignupComponent } from './signup/signup.component';
import {AuthGuard} from './user.service';


const routes: Routes = [{ path: '', redirectTo: 'home', pathMatch: 'full' },
{ path: 'home', component:HomeComponent },
{ path: 'about', component:AboutComponent },
{ path: 'donor', component:DonorComponent, canActivate:[AuthGuard]},
{ path: 'patient', component: PatientComponent, canActivate:[AuthGuard] },
{ path: 'contact', component: ContactComponent, canActivate:[AuthGuard]},
{ path: 'connect', component: ConnectComponent, canActivate:[AuthGuard]},
{ path: 'admin', component: AdminComponent, canActivate:[AuthGuard]},
{ path: 'login', component: LoginComponent},
{ path: 'counties', component: CountiesComponent},
{ path: 'sub-counties', component: SubCountiesComponent},
{ path: 'patients', component: PatientsComponent},
{ path: 'donors', component: DonorsComponent},
{ path: 'messages', component: MessagesComponent},
{ path: 'sign-up', component: SignupComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {

 }
