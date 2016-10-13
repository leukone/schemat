import { Component, OnInit, ViewEncapsulation } from '@angular/core';
import { Router } from '@angular/router';
import { Project } from './project';
import { ProjectService } from './project.service';

@Component({
  selector: 'my-app',
  templateUrl: 'app.component.html',
  /* The element here always has the state "in" when it
   * is present. We animate two transitions: From void
   * to in and from in to void, to achieve an animated
   * enter and leave transition. The element enters from
   * the left and leaves to the right using translateX,
   * and fades in/out using opacity. We use different easings
   * for enter and leave.
   */
   encapsulation: ViewEncapsulation.None,
   styleUrls: ['./app.component.css'],
 })


export class AppComponent implements OnInit {

  projects: Project[] = [];
  public slides: Project[] = [];

  constructor(
    private router: Router,
    private projectService: ProjectService) {}

  ngOnInit(): void {
    this.projectService.getProjects()
    .then(projects => this.projects = projects,
      projects => this.slides = projects);
  }
}
