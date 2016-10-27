export class Project {
    ident: number;
    title: string;
    desc: string;
    image: string;
    gallery1:string;
    gallery2:string;
    gallery3:string;
    gallery4:string;
    gallery5:string;
    gallery6:string;


    constructor (ident: number, title: string, desc: string, image: string, gallery1:string, gallery2:string, gallery3:string, gallery4:string, gallery5:string, gallery6:string) {
        this.ident = ident;
        this.title = title;
        this.desc = desc;
        this.image = image;
        this.gallery1 = gallery1;
        this.gallery2 = gallery2;
        this.gallery3 = gallery3;
        this.gallery4 = gallery4;
        this.gallery5 = gallery5;
        this.gallery6 = gallery6;
    }
}
