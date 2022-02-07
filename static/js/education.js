var count_education = parseInt(document.getElementsByName("cv_count_education")[0].value);

function add_education() {
    count_education = count_education + 1;
    var add = document.getElementById("add_education");
    var del = document.getElementById("delete_education");
    //time
    var time = document.getElementById("cv_graduation_time" + count_education);
    time.innerHTML = "2018 - 2022";
    // degree
    var degree = document.getElementById("cv_degree" + count_education);
    degree.innerHTML = "Master Degree in Computer Science";
    //school
    var school = document.getElementById("cv_graduation_school" + count_education);
    school.innerHTML = "HCM University of Technology";

    document.getElementsByName('cv_degree' + count_education)[0].value = 'Master Degree in Computer Science';
    document.getElementsByName('cv_graduation_time' + count_education)[0].value = "2018 - 2022";
    document.getElementsByName('cv_graduation_school' + count_education)[0].value = "HCM University of Technology";
    document.getElementsByName("cv_count_education")[0].value = count_education;
    if (count_education > 0) del.style.display = "inline-block";
    if (count_education >= 3) {
        add.style.display = "none";
        del.style.display = "inline-block"; // display the delete button if you add.    
    }
    //document.getElementById("cv_education_list").innerHTML += "<li id='cv_degree_item" + count_education + "'><h5 contenteditable = 'True' id ='cv_graduation_time"+count_education+"'>2010 - 2013</h5><h4 contenteditable = 'True' id ='cv_degree"+count_education+"'>Master Degree in Computer Science</h4><h4 contenteditable = 'True' id ='cv_graduation_school"+count_education+"'>University Name</h4></li>";
    var item = document.getElementById("cv_degree_item" + count_education);
    item.style.display = "block";
}

function delete_education() {
    if (count_education > 0) {
        // Remove
        var add = document.getElementById("add_education");
        var del = document.getElementById("delete_education");
        var item = document.getElementById('cv_degree_item' + count_education); // Get the item with id cv_degree_itemx
        // Hide this item and return to the deafault values .  
        item.style.display = "none";


        document.getElementsByName('cv_degree' + count_education)[0].value = '';
        document.getElementsByName('cv_graduation_time' + count_education)[0].value = '';
        document.getElementsByName('cv_graduation_school' + count_education)[0].value = '';
        
        count_education--;
        document.getElementsByName("cv_count_education")[0].value = count_education;
        del.style.display = "inline-block";
        add.style.display = "inline-block";
    }

    if (count_education == 0) {
        del.style.display = "none";// Display the add button, hide the delete button
        add.style.display = "inline-block";
    }


    
    
}