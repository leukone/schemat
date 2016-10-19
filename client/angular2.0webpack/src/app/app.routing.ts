import { ModuleWithProviders }  from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProjectsComponent } from './projects.component';
import { InfoComponent } from './info.component';
import { ContactComponent } from './contact.component';



const appRoutes: Routes = [
  {
    path: '',
    redirectTo: '/projects',
    pathMatch: 'full'
  },
  {
    path: 'info',
    component: InfoComponent
  },
   {
    path: 'projects',
    component: ProjectsComponent
  },
   {
    path: 'contact',
    component: ContactComponent
  },
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
