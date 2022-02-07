var count_skill = parseInt(document.getElementsByName("cv_count_skill")[0].value);
function add_skill() {
    count_skill++;
    var add = document.getElementById("add_skill");
    var del = document.getElementById("delete_skill");
    var skill = document.getElementById("cv_skill" + count_skill);
    skill.innerHTML = "Programming";

    var skill_expert = document.getElementById("cv_skill" + count_skill + "_expert");
    skill_expert.value = "80";

    document.getElementsByName('cv_skill' + count_skill)[0].value = 'Programming';
    document.getElementsByName('cv_skill' + count_skill + '_expert')[0].value = '80';

    document.getElementsByName("cv_count_skill")[0].value = count_skill;

    if (count_skill > 0) del.style.display = "inline-block";
    if (count_skill >= 10) {
        add.style.display = "none";
        del.style.display = "inline-block"; // display the delete button if you add.    
    }
    //document.getElementById("cv_education_list").innerHTML += "<li id='cv_degree_item" + count_education + "'><h5 contenteditable = 'True' id ='cv_graduation_time"+count_education+"'>2010 - 2013</h5><h4 contenteditable = 'True' id ='cv_degree"+count_education+"'>Master Degree in Computer Science</h4><h4 contenteditable = 'True' id ='cv_graduation_school"+count_education+"'>University Name</h4></li>";
    var item = document.getElementById("cv_skill_item" + count_skill);
    item.style.display = "block";
}

// Delete function
function delete_skill() {
    if (count_skill > 0) {
        // Remove
        var add = document.getElementById("add_skill");
        var del = document.getElementById("delete_skill");
        var item = document.getElementById('cv_skill_item' + count_skill); // Get the item 
        // Hide this item and return to the deafault values .  
        item.style.display = "none";
        // skilluage

        document.getElementsByName('cv_skill' + count_skill)[0].value = '';
        document.getElementsByName('cv_skill' + count_skill + '_expert')[0].value = '';

        count_skill--;
        document.getElementsByName("cv_count_skill")[0].value = count_skill;
        del.style.display = "inline-block";
        add.style.display = "inline-block";
    }

    if (count_skill == 0) {
        del.style.display = "none";// Display the add button, hide the delete button
        add.style.display = "inline-block";
    }

}