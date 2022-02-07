var count_interest = parseInt(document.getElementsByName("cv_count_interest")[0].value); // Number of items
function add_interest() {
    count_interest++;
    var add = document.getElementById("add_interest");
    var del = document.getElementById("delete_interest");
    var item = document.getElementById('cv_interest' + count_interest); // Get the item 
    item.innerHTML = "Swimming"

    document.getElementsByName('cv_interest' + count_interest)[0].value = 'Swimming';
    document.getElementsByName("cv_count_interest")[0].value = count_interest;

    

    if (count_interest > 0) del.style.display = "inline-block";
    if (count_interest >= 10) {
        add.style.display = "none";
        del.style.display = "inline-block"; // display the delete button if you add.    
    }
    //document.getElementById("cv_education_list").innerHTML += "<li id='cv_degree_item" + count_education + "'><h5 contenteditable = 'True' id ='cv_graduation_time"+count_education+"'>2010 - 2013</h5><h4 contenteditable = 'True' id ='cv_degree"+count_education+"'>Master Degree in Computer Science</h4><h4 contenteditable = 'True' id ='cv_graduation_school"+count_education+"'>University Name</h4></li>";
    var item = document.getElementById("cv_interest" + count_interest);
    item.style.display = "block";
}

function delete_interest() {
    if (count_interest > 0) {
        // Remove
        var add = document.getElementById("add_interest");
        var del = document.getElementById("delete_interest");
        var item = document.getElementById('cv_interest' + count_interest); // Get the item 
        // Hide this item and return to the deafault values .  
        item.style.display = "none";
        

        document.getElementsByName('cv_interest' + count_interest)[0].value = '';

        count_interest--;
        document.getElementsByName("cv_count_interest")[0].value = count_interest;

        del.style.display = "inline-block";
        add.style.display = "inline-block";
    }

    if (count_interest == 0) {
        del.style.display = "none";// Display the add button, hide the delete button
        add.style.display = "inline-block";
    }
}