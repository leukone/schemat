import {Component, OnInit, ViewEncapsulation, HostBinding } from '@angular/core';
import { Router } from '@angular/router';
import {Contact} from './contact';
import {ContactService} from './contact.service';
import {
  trigger,
  style,
  transition,
  animate
} from '@angular/core';

@Component({
     host: {
     '[@routeAnimation]': 'true',
     '[style.display]': "'block'",
     '[style.position]': "'absolute'",
     '[style.top]': '0'
  },
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
    selector: 'my-contact',
    encapsulation: ViewEncapsulation.None,
    templateUrl: 'contact.component.html',
    providers: [ContactService]
})

export class ContactComponent implements OnInit {

    errorMessage: string;
    contact: Contact;

    constructor(
    private router: Router,
    private contactService: ContactService) {
    }
    ngOnInit(): void {
        this.getContact();
    }

     getContact(): void {
       this.contactService
                     .getContact()
                     .then(
                       contact => this.contact = contact,
                       error =>  this.errorMessage = <any>error);
  }
}
