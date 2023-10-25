import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './core/main/main.component';

import { LoginComponent } from './pages/login/login.component';
import { JwtAuthGuard } from './guards/jwt-auth.guard';
import { EquipeComponent } from './pages/equipe/equipe.component';

const routes: Routes = [
  {path: 'login', component: LoginComponent},
  { 
    path: '',  canActivate: [JwtAuthGuard], component: MainComponent, children: [
      {path: '', component: EquipeComponent, },
    ] 
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
