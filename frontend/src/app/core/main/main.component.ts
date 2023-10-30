import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit{


  items:any = []
  isOpen:boolean = true

  constructor(
    private router: Router,
  ) {}
  ngOnInit(): void {
      this.items = [
        {
          label: 'Equipe',
          icon: 'pi pi-users',
          items: [
            {
              label: 'Usuarios',
              icon: 'pi pi-circle'
            },
            {
              label: 'Colaboradores',
              icon: 'pi pi-circle'
            }
          ]
        }
      ]

  }

  navigateTo(locate:string){
    this.router.navigate([`/${locate}`])
  }

  handleMenu() {
    this.isOpen = !this.isOpen;
    
  }

}
