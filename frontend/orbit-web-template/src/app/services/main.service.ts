import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MainService {
  url = 'http://127.0.0.1:5000'

  constructor(private httpClient : HttpClient) {
   }


  public getFromBackend(){

    this.httpClient
      .get<any>(this.url)
      .subscribe((response) => {
        return response
      });

   }
}
