import {Component, OnInit, ViewEncapsulation, HostBinding } from '@angular/core';
import { Router } from '@angular/router';
import {Info} from './info';
import {InfoService} from './info.service';
import {
    trigger,
    style,
    transition,
    animate
} from '@angular/core';

@Component({
    selector: 'my-infos',
    animations: [
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
    encapsulation: ViewEncapsulation.None,
    templateUrl: 'info.component.html',
    styleUrls: ['projects.component.css'],
    providers: [InfoService]
})

export class InfoComponent implements OnInit {
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
    infos: Info[];

    constructor(
        private router: Router,
        private infoService: InfoService) {
    }
    ngOnInit(): void {
        this.getInfos();
    }

    getInfos(): void {
        this.infoService.getInfos()
        .then(
            infos => this.infos = infos,
            error =>  this.errorMessage = <any>error);
    }
}
