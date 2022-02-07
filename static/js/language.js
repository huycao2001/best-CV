var count_lang = parseInt(document.getElementsByName("cv_count_lang")[0].value);
function add_lang() {
    count_lang++;
    var add = document.getElementById("add_lang");
    var del = document.getElementById("delete_lang");
    var lang = document.getElementById("cv_lang" + count_lang);
    lang.innerHTML = "English";

    var lang_expert = document.getElementById("cv_lang" + count_lang + "_expert");
    lang_expert.value = "80";

    document.getElementsByName('cv_lang' + count_lang)[0].value = 'English';
    document.getElementsByName('cv_lang' + count_lang + '_expert')[0].value = '80';

    document.getElementsByName("cv_count_lang")[0].value = count_lang;

    if (count_lang > 0) del.style.display = "inline-block";
    if (count_lang >= 5) {
        add.style.display = "none";
        del.style.display = "inline-block"; // display the delete button if you add.    
    }
    //document.getElementById("cv_education_list").innerHTML += "<li id='cv_degree_item" + count_education + "'><h5 contenteditable = 'True' id ='cv_graduation_time"+count_education+"'>2010 - 2013</h5><h4 contenteditable = 'True' id ='cv_degree"+count_education+"'>Master Degree in Computer Science</h4><h4 contenteditable = 'True' id ='cv_graduation_school"+count_education+"'>University Name</h4></li>";
    var item = document.getElementById("cv_lang_item" + count_lang);
    item.style.display = "block";
}

// Delete function
function delete_lang() {
    if (count_lang > 0) {
        // Remove
        var add = document.getElementById("add_lang");
        var del = document.getElementById("delete_lang");
        var item = document.getElementById('cv_lang_item' + count_lang); // Get the item 
        // Hide this item and return to the deafault values .  
        item.style.display = "none";
        // language
        
        document.getElementsByName('cv_lang' + count_lang)[0].value = '';
        document.getElementsByName('cv_lang' + count_lang + '_expert')[0].value = '';

        count_lang--;
        document.getElementsByName("cv_count_lang")[0].value = count_lang;
        del.style.display = "inline-block";
        add.style.display = "inline-block";
    }

    if (count_lang == 0) {
        del.style.display = "none";// Display the add button, hide the delete button
        add.style.display = "inline-block";
    }

}