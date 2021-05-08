import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {UserService} from './user.service';
import{HttpClient, HttpHeaders} from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl="http://127.0.0.1:8000/api";
  
  constructor(private http: HttpClient, public userService:UserService) { }
  httpHeaders=new HttpHeaders({'Content-Type':'application/json', 'Authorization':'JWT' + this.userService.token});
  getAllCounties():Observable<any>{
  	return this.http.get(this.baseurl +'/counties/', {headers:this.httpHeaders});
  }
  getAllPatients():Observable<any>{
    return this.http.get(this.baseurl +'/patients/', {headers:this.httpHeaders});
  }
  getAllDonors():Observable<any>{
    return this.http.get(this.baseurl +'/donors/', {headers:this.httpHeaders});
  }
  getAllMessages():Observable<any>{
    return this.http.get(this.baseurl +'/messages/', {headers:this.httpHeaders});
  }
  getOneDonor(id):Observable<any>{
    return this.http.get(this.baseurl +'/donors/' + id + '/', {headers:this.httpHeaders});
  }
  getAllSubCounties():Observable<any>{
  	return this.http.get(this.baseurl +'/sub_counties/', {headers:this.httpHeaders});
  }
  
   register(donor):Observable<any>{
    const body={donorName:donor.donorName,
    parentName:donor.parentName,
    gender:donor.gender,
    dateOfBirth:donor.dateOfBirth,
    bloodGroup:donor.bloodGroup,
    weight:donor.weight,
    email:donor.email,
    county:donor.county,
    subCounty:donor.subCounty,
    location:donor.location,
    contactOne:donor.contactOne,
    contactTwo:donor.contactTwo,
    voluntary:donor.voluntary,
    newDonor:donor.newDonor,
    lastDonated:donor.lastDonated,
    // image:donor.image
    
   }
    return this.http.post(this.baseurl+'/donors/', body, {headers:this.httpHeaders} );
  }
  registerPatient(patient):Observable<any>{
    const body={patientName:patient.patientName,
    hospitalName:patient.hospitalName,
    county:patient.county,
    subCounty:patient.subCounty,
    doctor:patient.doctor,
    contactName:patient.contactName,
    email:patient.email,
    contactDate:patient.contactDate,
    requiredDate:patient.requiredDate,
    bloodUnits:patient.bloodUnits,
    bloodGroup:patient.bloodGroup,
    contactOne:patient.contactOne,
    contactTwo:patient.contactTwo,
    reason:patient.reason,
    // status:patient.status,
    // image:patient.image
   }
    return this.http.post(this.baseurl+'/patients/', body, {headers:this.httpHeaders} );
  }

  sendMessage(sender):Observable<any>{
   const body ={
      sender:sender.sender,
      senderName:sender.senderName,
      senderEmail:sender.senderEmail,
      contact:sender.contact,
      sentDate:sender.sentDate,
      message:sender.message,
      
   }
    return this.http.post(this.baseurl+'/messages/', body, {headers:this.httpHeaders} );
  }
  deleteDonor(id:number): Observable<void> {
    return this.http.delete<void>(`${this.baseurl}/donors/${id}`);
  }
  deletePatient(id:number): Observable<void> {
    return this.http.delete<void>(`${this.baseurl}/patients/${id}`);
  }
  deleteMessage(id:number): Observable<void> {
    return this.http.delete<void>(`${this.baseurl}/messages/${id}`);
  }
}
