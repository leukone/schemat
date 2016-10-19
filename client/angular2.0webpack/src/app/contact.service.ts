import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import { Contact } from './contact';
import 'rxjs/add/operator/toPromise';
import { Configuration } from './app.constants';



@Injectable()
export class ContactService {
  // URL to web api

    constructor(private http: Http,  private configuration: Configuration ) { }

    getContact(): Promise<Contact> {
    return this.http.get(`${this.configuration.Server}contactapi`)
                    .toPromise()
                    .then(response => response.json())
                    .catch(this.handleError);
  }
    private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }


}
