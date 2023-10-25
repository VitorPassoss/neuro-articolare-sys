import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { MenuComponent } from './menu/menu.component';
import { MainComponent } from './main/main.component';
import { AppRoutingModule } from '../app-routing.module';

import { InputTextModule } from 'primeng/inputtext';
import { ToastModule } from 'primeng/toast';
import { PasswordModule } from 'primeng/password';
import { ButtonModule } from 'primeng/button';
import { PanelModule } from 'primeng/panel';
import { BlockLoadingComponent } from '../shared/block-loading/block-loading.component';
import { SharedModule } from 'primeng/api';
import { MenuModule } from 'primeng/menu';
import { PanelMenuModule } from 'primeng/panelmenu';


@NgModule({
  declarations: [
    MenuComponent,
    MainComponent
  ],
  imports: [
    AppRoutingModule,
    CommonModule,
    FormsModule,
    InputTextModule,
    PasswordModule,
    ButtonModule,
    ToastModule,
    ReactiveFormsModule,
    PanelModule,
    BlockLoadingComponent, 
    SharedModule,
    MenuModule,
    PanelMenuModule
  ],
  exports: [
    AppRoutingModule
  ]
})
export class CoreModule { }
