import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Info } from './info';


@Injectable()
export class InfoService {

    private infoUrl = 'http://127.0.0.1:8000/info/?format=json';

    constructor(private http: Http) { }


    getInfos(): Promise<Info[]> {
      return this.http.get(this.infoUrl)
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
