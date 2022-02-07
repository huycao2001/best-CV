var count_experience = parseInt(document.getElementsByName("cv_count_experience")[0].value); // Number of items

function add_experience() {
    count_experience = count_experience + 1;
    var add = document.getElementById("add_experience");
    var del = document.getElementById("delete_experience");

    //time
    var time = document.getElementById("cv_working_time" + count_experience);
    time.innerHTML = "03/2018 - NOW";
    // degree
    var company = document.getElementById("cv_company_name" + count_experience);
    company.innerHTML = "BestCV Company";

    //school
    var role = document.getElementById("cv_company_role" + count_experience);
    role.innerHTML = "Full-stack Developer";

    //description 
    var des = document.getElementById("cv_job_description" + count_experience);
    des.innerHTML = "Build and deploy projects, participate in the development of projects using artistic Javascript, Django API.";


    document.getElementsByName('cv_company_name' + count_experience)[0].value = 'BestCV Company';
    document.getElementsByName('cv_working_time' + count_experience)[0].value = '03/2018 - NOW';
    document.getElementsByName('cv_company_role' + count_experience)[0].value = 'Full-stack Developer';
    document.getElementsByName('cv_job_description' + count_experience)[0].value = 'Build and deploy projects, participate in the development of projects using artistic Javascript, Django API.';
    document.getElementsByName("cv_count_experience")[0].value = count_experience;


    if (count_experience > 0) del.style.display = "inline-block";
    if (count_experience >= 5) {
        add.style.display = "none";
        del.style.display = "inline-block"; // display the delete button if you add.    
    }
    //document.getElementById("cv_education_list").innerHTML += "<li id='cv_degree_item" + count_education + "'><h5 contenteditable = 'True' id ='cv_graduation_time"+count_education+"'>2010 - 2013</h5><h4 contenteditable = 'True' id ='cv_degree"+count_education+"'>Master Degree in Computer Science</h4><h4 contenteditable = 'True' id ='cv_graduation_school"+count_education+"'>University Name</h4></li>";
    var item = document.getElementById("cv_experience_item" + count_experience);
    item.style.display = "block";
}

function delete_experience() {
    if (count_experience > 0) {
        // Remove
        var add = document.getElementById("add_experience");
        var del = document.getElementById("delete_experience");
        var item = document.getElementById("cv_experience_item" + count_experience); // Get the item with id cv_degree_itemx
        // Hide this item and return to the deafault values .  
        item.style.display = "none";
        
        document.getElementsByName('cv_company_name' + count_experience)[0].value = '';
        document.getElementsByName('cv_working_time' + count_experience)[0].value = '';
        document.getElementsByName('cv_company_role' + count_experience)[0].value = '';
        document.getElementsByName('cv_job_description' + count_experience)[0].value = '';

        count_experience--;
        document.getElementsByName("cv_count_experience")[0].value = count_experience;


        del.style.display = "inline-block";
        add.style.display = "inline-block";
    }

    if (count_experience == 0) {
        del.style.display = "none";// Display the add button, hide the delete button
        add.style.display = "inline-block";
    }
}