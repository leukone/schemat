import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';
import 'rxjs/add/operator/map';

import { Project } from './project';
import { Configuration } from './app.constants';


@Injectable()
export class ProjectService {

    constructor(private http: Http, private configuration: Configuration ) { }


    getProjects(): Promise<Project[]> {
      return this.http.get(`${this.configuration.Server}projectsapi`)
                    .toPromise()
                    .then(response => response.json())
                    .catch(this.handleError);
  }

    getProject(ident: number): Promise<Project> {
      return this.getProjects()
             .then(projects => projects.find(project => project.ident === ident));
    }
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}
