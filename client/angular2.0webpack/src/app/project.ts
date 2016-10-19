export class Project {
    ident: number;
    title: string;
    desc: string;
    projectName: string;
    image: string;

    constructor (ident: number, title: string, desc: string, projectName: string, image: string) {
        this.ident = ident;
        this.title = title;
        this.desc = desc;
        this.projectName = projectName;
        this.image = image;
    }
}
