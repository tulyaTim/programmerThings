import React from 'react';
import ReactDOM from 'react-dom/client';

const myArray = ['apple', 'banana', 'orange']

const myList = myArray.map((item) => <p>{item}</p>)

// class Car {
//     constructor(name) {
//         this.brand = name;
//     }

//     present() {
//         return 'I have a ' + this.brand;
//     }
// }

// class Model extends Car {
//     constructor(name, model) {
//         super(name) // calls the parent constructor method
//         this.model = model;
//     }

//     show() {
//         return this.present() +', It is a '+ this.model 
//     }
// }

// const mycar = new Model("Ford", "Mustang")
// console.log(mycar.show());



class Uict {
    constructor(principle) {
        this.principle = principle;
    }

    grad() {
        return "12th graduation will see " + this.principle;
    }

}

class Mes extends Uict {
    constructor(name, pos) {
        super(name);
        this.pos = pos;
    }

    convoy() {
        return this.grad() + " as overseen by " + this.pos;
    }
}

const myUict = new Mes("Kitogo", "Amina");
console.log(myUict.convoy());

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(myList);
