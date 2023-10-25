import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit{

  items:any = []

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
}
