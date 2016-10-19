import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

// Imports for loading & configuring the in-memory web api

import {Ng2PageScrollModule} from 'ng2-page-scroll';

import { AppComponent }         from './app.component';
import { ProjectsComponent }      from './projects.component';
import { ProjectService }          from './project.service';
import { InfoComponent }  from './info.component';
import { InfoService }          from './info.service';

import { ContactComponent }  from './contact.component';
import { ContactService }          from './contact.service';
import { routing }              from './app.routing';
import { Configuration } from './app.constants';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    Ng2PageScrollModule,
    routing
  ],
  declarations: [
    AppComponent,
    ProjectsComponent,
    InfoComponent,
    ContactComponent,
  ],
  providers: [
    ProjectService,
    InfoService,
    ContactService,
    Configuration,
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule {
}
