import { Component } from '@angular/core';
import {ApiService} from "./api.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'frontend';
  movies = [{name: 'login'}];
  selectedDnc;

  constructor(private api:ApiService) {
    this.getMovies();
    this.selectedDnc = {name: '', description: '', phonebook: ''}
  }
  getMovies = () => {
    this.api.getAllMovies().subscribe(
      data => {
        this.movies = data;
        // data => {
        //     this.name = data.name;
        //     this.description = data.description;
        // }
      },
      error => {
        console.log(error);
      }
    );
  }

  movieClicked = (movie) => {
    console.log(movie.id)
    this.api.getOneMovie(movie.id).subscribe(
      data => {
        console.log(data);
            this.selectedDnc = data;
      },
      error => {
        console.log(error);
      }
    );
  }

  updateDnc = () => {
    this.api.updateDnc(this.selectedDnc).subscribe(
      data => {
        console.log(data);
            this.selectedDnc = data;
      },
      error => {
        console.log(error);
      }
    );
  }

  createDnc = () => {
    this.api.createDnc(this.selectedDnc).subscribe(
      data => {
        console.log(data);
            this.movies.push(data);
      },
      error => {
        console.log(error);
      }
    );
  }


  deleteDnc = () => {
    this.api.deleteDnc(this.selectedDnc.id).subscribe(
      data => {
        console.log(data);
            this.getMovies();
      },
      error => {
        console.log(error);
      }
    );
  }

}
