import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseurl = "http://102.130.121.230";
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json', 'Authorization': 'Token 529c813292935d8997787a64bbd0a9dc990a57ce099bc3e940a02387d10d6e8a'})

  constructor(private http: HttpClient) { }

  getAllMovies(): Observable<any>{
    return this.http.get(this.baseurl + '/api/dnc/', {headers: this.httpHeaders});
  }

  getOneMovie(id): Observable<any>{
    return this.http.get(this.baseurl + '/api/dnc/' + id + '/', {headers: this.httpHeaders});
  }

  updateDnc(movie): Observable<any>{
    const body = {name: movie.name, description: movie.description};
    console.log(body);
    return this.http.put(this.baseurl + '/api/dnc/' + movie.id + '/', body, {headers: this.httpHeaders});
  }

  createDnc(movie): Observable<any>{
    const body = {amount: movie.amount, quantity: movie.quantity, package: movie.package};
    console.log(body);
    return this.http.post(this.baseurl + '/api/order/38/checkout/', body, {headers: this.httpHeaders});
  }

  deleteDnc(id): Observable<any>{
    return this.http.delete(this.baseurl + '/api/dnc/' + id + '/', {headers: this.httpHeaders});
  }

}
