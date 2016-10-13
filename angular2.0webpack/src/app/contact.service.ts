import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import { Contact } from './contact';
import 'rxjs/add/operator/toPromise';


@Injectable()
export class ContactService {

    private contactUrl = 'http://127.0.0.1:8000/contactinfo/?format=json';  // URL to web api

    constructor(private http: Http) { }

    getContact(): Promise<Contact> {
    return this.http.get(this.contactUrl)
                    .toPromise()
                    .then(response => response.json())
                    .catch(this.handleError);
  }
    private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }


}
