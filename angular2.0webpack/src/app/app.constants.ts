import { Injectable } from '@angular/core';

@Injectable()
export class Configuration {
    public Server: string = 'http://127.0.0.1:8000/';
    public ApiUrl: string = '/?format=json';
}
