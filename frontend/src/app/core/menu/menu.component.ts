import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit{

  constructor(
    private router: Router,
  ){}

    items:any = []

  logout() {
    localStorage.removeItem('access_token');
    this.router.navigate(['login']);
  }


  ngOnInit(): void {
    this.items = [
      {
          label: 'Navegação principal',
          items: [
              {
                  label: 'Update',
                  icon: 'pi pi-refresh',
                  command: () => {
                  }
              },
              {
                  label: 'Delete',
                  icon: 'pi pi-times',
                  command: () => {
                  }
              }
          ]
      },
      {
          label: 'Navigate',
          items: [
              {
                  label: 'Angular',
                  icon: 'pi pi-external-link',
                  url: 'http://angular.io'
              },
              {
                  label: 'Router',
                  icon: 'pi pi-upload',
                  routerLink: '/fileupload'
              }
          ]
      }
  ];
  }


  
}
