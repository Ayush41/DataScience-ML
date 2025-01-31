const path = require('path');
const fs = require('fs');

const llamaModelFile = './llama3.2.1b.js';
const inputFilePath = './input.txt';

console.log(`Using ${path.basename(llamaModelFile)} as your Llama model`);
