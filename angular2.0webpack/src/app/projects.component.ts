import {Component, OnInit, Input, ViewEncapsulation, HostBinding} from '@angular/core';
import {
  trigger,
  state,
  style,
  transition,
  animate
} from '@angular/core';
import {PageScrollConfig} from 'ng2-page-scroll';
import {EasingLogic} from 'ng2-page-scroll';
import { Router } from '@angular/router';
import {Project} from './project';
import {ProjectService} from './project.service';


@Component({
    animations: [
    trigger('visibilityChanged', [
      state('true' , style({ opacity: 1, transform: 'scale(1.0)' })),
      state('false', style({ opacity: 0, transform: 'scale(0.0)'  })),
      transition('1 => 0', animate('300ms')),
      transition('0 => 1', animate('900ms'))
    ]),
    trigger('routeAnimation', [

      transition('void => *', [
        style({transform: 'translateX(-100%)'}),
        animate('1.2s')
      ]),
      transition('* => void', [
        animate('1.2s', style({transform: 'translateX(100%)'}))
      ])
    ])
    ],
    selector: 'as-my-projects',
    encapsulation: ViewEncapsulation.None,
    templateUrl: 'projects.component.html',
    styles: [`
    .selected {
      color: red;
    }
.carousel-indicators li {
  width: 12px;
    height: 12px;
    margin: 30px;
    background-color: none;
    border-radius: 0;
    -ms-transform: rotate(45deg); /* IE 9 */
    -webkit-transform: rotate(45deg); /* Chrome, Safari, Opera */
    transform: rotate(45deg);
    border: 1px solid #fff;
        border-top-width: 1px;
        border-right-width: 1px;
        border-bottom-width: 1px;
        border-left-width: 1px;
        border-top-style: solid;
        border-right-style: solid;
        border-bottom-style: solid;
        border-left-style: solid;
        border-top-color: rgb(255, 255, 255);
        border-right-color: rgb(255, 255, 255);
        border-bottom-color: rgb(255, 255, 255);
        border-left-color: rgb(255, 255, 255);
        -moz-border-top-colors: none;
        -moz-border-right-colors: none;
        -moz-border-bottom-colors: none;
        -moz-border-left-colors: none;
        border-image-source: none;
        border-image-slice: 100% 100% 100% 100%;
        border-image-width: 1 1 1 1;
        border-image-outset: 0 0 0 0;
        border-image-repeat: stretch stretch;
    background-color: rgba(0, 0, 0, 0);
    color: transparent;
}

a {
  z-index: 20;
}
.carousel-indicators li:hover {
  cursor:pointer !important;
}


.carousel-indicators li.selected {
        border-top-width: 4px;
        border-right-width: 4px;
        border-bottom-width: 4px;
        border-left-width: 4px;
    }`],
})

export class ProjectsComponent implements OnInit {

    @HostBinding('@routeAnimation') get routeAnimation() {
      return true;
    }

    @HostBinding('style.display') get display() {
      return 'block';
    }

    @HostBinding('style.position') get position() {
      return 'absolute';
    }
    @HostBinding('style.width') get width() {
      return '100%';
    }
    @HostBinding('style.height') get height() {
      return '100%';
    }
    @HostBinding('style.top') get top() {
      return '0';
    }

  errorMessage: string;
  projects: Project[];
  selectedProject: Project;
  items = [1, 2, 3];
  visibility = 'shown';
  @Input() isVisible: boolean = true;

  constructor(
    private router: Router,
    private projectService: ProjectService) {
   }

  public array: number[] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

  public myEasing: EasingLogic = {
        ease: (t: number, b: number, c: number, d: number): number => {
            // easeInOutExpo easing
            if (t === 0) return b;
            if (t === d) return b + c;
            if ((t /= d / 2) < 1) return c / 2 * Math.pow(2, 10 * (t - 1)) + b;
            return c / 2 * (-Math.pow(2, -10 * --t) + 2) + b;
        }
  };


  getProjects(): void {
         this.projectService
               .getProjects()
               .then(projects => this.projects = projects,
                     error =>  this.errorMessage = <any>error);
  }

    ngOnInit(): void {
      this.getProjects();
    }


  onSelect(project: Project): void {
         this.selectedProject = project;
       }



  gotoDetail(): void {
    this.router.navigate(['/detail', this.selectedProject.ident]);
  }


}
