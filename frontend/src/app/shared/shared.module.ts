import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TabViewModule } from 'primeng/tabview';

import { PanelModule } from 'primeng/panel';
import {ButtonModule} from 'primeng/button';
import { TableModule } from 'primeng/table';
import { DialogModule } from 'primeng/dialog';
import { InputTextModule } from 'primeng/inputtext';

import { InputNumberModule } from 'primeng/inputnumber';
import { DropdownModule } from 'primeng/dropdown';
import { MessageService } from 'primeng/api';
import { ReactiveFormsModule } from '@angular/forms';
import { ProgressSpinnerModule } from 'primeng/progressspinner';

import { DragDropModule } from 'primeng/dragdrop';
import { PickListModule } from 'primeng/picklist';
import { FormsModule } from '@angular/forms';
import { MultiSelectModule } from 'primeng/multiselect';

import { PasswordModule } from 'primeng/password';
import { ChartModule } from 'primeng/chart';

import { SplitterModule } from 'primeng/splitter';
import { CardModule } from 'primeng/card';
import { ChipModule } from 'primeng/chip';
import { MenuModule } from 'primeng/menu';
import { FullCalendarModule } from '@fullcalendar/angular';
import { CalendarModule } from 'primeng/calendar';
import { CheckboxModule } from 'primeng/checkbox';
import { DividerModule } from 'primeng/divider';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    TabViewModule,
    PanelModule,
    ButtonModule,
    TableModule,
    DialogModule,
    InputTextModule,
    InputNumberModule,
    DropdownModule,
    ReactiveFormsModule,
    ProgressSpinnerModule,
    DragDropModule,
    PickListModule,
    FormsModule,
    MultiSelectModule,
    PasswordModule,
    ChartModule,
    SplitterModule,
    CardModule,
    ChipModule,
    MenuModule,
    FullCalendarModule,
    CalendarModule,
    CheckboxModule,
    DividerModule
  ],
  exports:[
    TabViewModule,
    PanelModule,
    ButtonModule,
    TableModule,
    DialogModule,
    InputTextModule,
    InputNumberModule,
    DropdownModule,
    ReactiveFormsModule,
    ProgressSpinnerModule,
    DragDropModule,
    PickListModule,
    FormsModule,
    MultiSelectModule,
    PasswordModule,
    ChartModule,
    SplitterModule,
    CardModule,
    ChipModule,
    MenuModule,
    FullCalendarModule,
    CalendarModule,
    CheckboxModule,
    DividerModule
  ],
  providers: [MessageService]

})
export class SharedModule { }
