export class Info {
    ident: number;
    title: string;
    info: string;
    image: string;

    constructor(ident: number, title: string, info: string, image: string) {
        this.ident = ident;
        this.title = title;
        this.info = info;
        this.image = image;
    }
}
