//ПЕРЕМЕННЫЕ
const edit = document.getElementById('mainedit');
const editBlock = document.getElementById('edit-disabled');

const name = document.getElementById('name');
const occupation = document.getElementById('occupation');
const workplace = document.getElementById('workplace');

const input_name = document.getElementById('input1');
const input_occupation = document.getElementById('input2');
const input_workplace = document.getElementById('input3');
const error = document.getElementById('error-input');


//functions
function changeName() {
    edit.setAttribute("id", "main-edit");
    editBlock.setAttribute("id", "edit");
}

function EXITchangeName() {
    edit.setAttribute("id", "mainedit");
    editBlock.setAttribute("id", "edit-disabled");
}

function stretchElement(n) {
    document.getElementById(n).id = 'str';
}

function EXITstretchElement(n) {
    document.getElementById('str').id = n;
}

function saveChanges() {
    if (input_name.value.length == 0 || input_occupation.value.length == 0 || input_workplace.value.length == 0) {
        error.setAttribute("id", "error");
        setTimeout(() => {document.getElementById('error').setAttribute("id", "error-input");}, 5000);
    } else {
        name.innerHTML = 'Имя: '+ input_name.value;
        occupation.innerHTML = 'Имя: '+ input_occupation.value;
        workplace.innerHTML = 'Имя: '+ input_workplace.value;
        EXITchangeName()
    }
}