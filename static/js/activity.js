var count_activity = parseInt(document.getElementsByName("cv_count_activity")[0].value); // Number of items

function add_activity() {
    count_activity = count_activity + 1;
    var add = document.getElementById("add_activity");
    var del = document.getElementById("delete_activity");

    //time
    var time = document.getElementById("cv_activity_working_time" + count_activity);
    time.innerHTML = "Jan 2021 - Feb 2021";
    // degree
    var company = document.getElementById("cv_activity_company_name" + count_activity);
    company.innerHTML = "BestCV - EDUCATION TALK 2021";

    //school
    var role = document.getElementById("cv_activity_company_role" + count_activity);
    role.innerHTML = "Member of BestCV Ambassador";

    //description 
    var des = document.getElementById("cv_activity_job_description" + count_activity);
    des.innerHTML = "Organize monthly events, network with HCMUT students and share how to hunt scholarships and support to find appropriate job or careers.";


    document.getElementsByName('cv_activity_company_name' + count_activity)[0].value = 'BestCV - EDUCATION TALK 2021';
    document.getElementsByName('cv_activity_working_time' + count_activity)[0].value = 'Jan 2021 - Feb 2021';
    document.getElementsByName('cv_activity_company_role' + count_activity)[0].value = 'Member of BestCV Ambassador';
    document.getElementsByName('cv_activity_job_description' + count_activity)[0].value = 'Organize monthly events, network with HCMUT students and share how to hunt scholarships and support to find appropriate job or careers.';
    document.getElementsByName("cv_count_activity")[0].value = count_activity;


    if (count_activity > 0) del.style.display = "inline-block";
    if (count_activity >= 5) {
        add.style.display = "none";
        del.style.display = "inline-block"; // display the delete button if you add.    
    }
    //document.getElementById("cv_education_list").innerHTML += "<li id='cv_degree_item" + count_education + "'><h5 contenteditable = 'True' id ='cv_graduation_time"+count_education+"'>2010 - 2013</h5><h4 contenteditable = 'True' id ='cv_degree"+count_education+"'>Master Degree in Computer Science</h4><h4 contenteditable = 'True' id ='cv_graduation_school"+count_education+"'>University Name</h4></li>";
    var item = document.getElementById("cv_activity_item" + count_activity);
    item.style.display = "block";
}

function delete_activity() {
    if (count_activity > 0) {
        // Remove
        var add = document.getElementById("add_activity");
        var del = document.getElementById("delete_activity");
        var item = document.getElementById("cv_activity_item" + count_activity); // Get the item with id cv_degree_itemx
        // Hide this item and return to the deafault values .  
        item.style.display = "none";

        document.getElementsByName('cv_activity_company_name' + count_activity)[0].value = '';
        document.getElementsByName('cv_activity_working_time' + count_activity)[0].value = '';
        document.getElementsByName('cv_activity_company_role' + count_activity)[0].value = '';
        document.getElementsByName('cv_activity_job_description' + count_activity)[0].value = '';

        count_activity--;
        document.getElementsByName("cv_count_activity")[0].value = count_activity;


        del.style.display = "inline-block";
        add.style.display = "inline-block";
    }

    if (count_activity == 0) {
        del.style.display = "none";// Display the add button, hide the delete button
        add.style.display = "inline-block";
    }
}