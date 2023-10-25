import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoreModule } from './core/core.module';
import { SharedModule } from './shared/shared.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TableModule } from 'primeng/table';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './pages/login/login.component';
import { ChartModule } from 'primeng/chart';
import { BlockLoadingComponent } from './shared/block-loading/block-loading.component';
import { ToastModule } from 'primeng/toast';
import { EquipeComponent } from './pages/equipe/equipe.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    EquipeComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    CoreModule,
    SharedModule,
    BrowserAnimationsModule,
    TableModule,
    HttpClientModule,
    BlockLoadingComponent,
    ToastModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
