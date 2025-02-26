const edit = document.getElementById('mainedit');
const editBlock = document.getElementById('edit-disabled');

function changeName() {
    edit.setAttribute("id", "main-edit");
    editBlock.setAttribute("id", "edit");
}

function EXITchangeName() {
    edit.setAttribute("id", "mainedit");
    editBlock.setAttribute("id", "edit-disabled");
}