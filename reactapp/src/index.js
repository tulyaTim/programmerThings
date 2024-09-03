import React from 'react';
import ReactDOM from 'react-dom/client';

const myArray = ['apple', 'banana', 'orange']

const myList = myArray.map((item) => <p>{item}</p>)

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(myList);
