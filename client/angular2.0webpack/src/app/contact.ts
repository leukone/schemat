export class Contact {
    title: string;
    contactinfo: string;
    email: string;
    phone: string;
    image: string;

    constructor(title: string, contactinfo: string, email: string, phone: string, image: string) {
        this.title = title;
        this.contactinfo = contactinfo;
        this.email = email;
        this.phone = phone;
        this.image = image;
    }
}
