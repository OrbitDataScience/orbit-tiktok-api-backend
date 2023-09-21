import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  constructor() { }

  senha  = ''
  email = ''
  select = 0

  ngOnInit(): void {
  }

  getValues(){
    console.log(this.senha)
    console.log(this.email)
    console.log(this.select)
  }
}
