const TextToSVG = require('text-to-svg');
const fs = require('fs');

const textToSVG = TextToSVG.loadSync('./SegoeUI.ttf');

const attributes = {fill: 'white', stroke: 'none', style: "color:#ffffff"};

const options = {
    x: 15, 
    y: 22, 
    textAnchor: "middle", 
    fontSize: 18, 
    fontFamily:"Segoe UI", 
    attributes: attributes
};

let arrayOfPaths = [];
const numbers = [...Array(41).keys()];
numbers.map(num =>{
    const svg = textToSVG.getSVG(num.toString(), options);
    const path = svg.match('(<path)([^<]*|[^>]*)')[0];
    arrayOfPaths.push(path)
})
console.log(arrayOfPaths);



