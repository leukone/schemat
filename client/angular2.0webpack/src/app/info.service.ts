import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Info } from './info';
import { Configuration } from './app.constants'

@Injectable()
export class InfoService {


    constructor(private http: Http, private configuration: Configuration ) { }


    getInfos(): Promise<Info[]> {
      return this.http.get(`${this.configuration.Server}infoapi`)
                    .toPromise()
                    .then(response => response.json())
                    .catch(this.handleError);
  }

    getInfo(ident: number): Promise<Info> {
      return this.getInfos()
             .then(infos => infos.find(info => info.ident === ident));
    }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

}
