var count_cer = parseInt(document.getElementsByName("cv_count_cer")[0].value);

function add_cer() {
    count_cer = count_cer + 1;
    var add = document.getElementById("add_cer");
    var del = document.getElementById("delete_cer");
    //time
    var time = document.getElementById("cv_cer_year" + count_cer);
    time.innerHTML = "2020 - 2021";
    
    var name = document.getElementById("cv_cer_name" + count_cer);
    name.innerHTML = "BestCV Scholarship in 2nd semester 2012-2013 and 1st semester 2013-2014.";

    document.getElementsByName('cv_cer_year' + count_cer)[0].value = "2020 - 2021";
    document.getElementsByName('cv_cer_name' + count_cer)[0].value = "BestCV Scholarship in 2nd semester 2016-2017 and 1st semester 2017-2018.";
    document.getElementsByName("cv_count_cer")[0].value = count_cer;
    if (count_cer > 0) del.style.display = "inline-block";
    if (count_cer >= 5) {
        add.style.display = "none";
        del.style.display = "inline-block"; // display the delete button if you add.    
    }
    //document.getElementById("cv_cer_list").innerHTML += "<li id='cv_degree_item" + count_cer + "'><h5 contenteditable = 'True' id ='cv_graduation_time"+count_cer+"'>2010 - 2013</h5><h4 contenteditable = 'True' id ='cv_degree"+count_cer+"'>Master Degree in Computer Science</h4><h4 contenteditable = 'True' id ='cv_graduation_school"+count_cer+"'>University Name</h4></li>";
    var item = document.getElementById("cv_cer_item" + count_cer);
    item.style.display = "block";
}

function delete_cer() {
    if (count_cer > 0) {
        // Remove
        var add = document.getElementById("add_cer");
        var del = document.getElementById("delete_cer");
        var item = document.getElementById('cv_cer_item' + count_cer); // Get the item with id cv_degree_itemx
        // Hide this item and return to the deafault values .  
        item.style.display = "none";


        document.getElementsByName('cv_cer_year' + count_cer)[0].value = '';
        document.getElementsByName('cv_cer_name' + count_cer)[0].value = '';
        
        count_cer--;
        document.getElementsByName("cv_count_cer")[0].value = count_cer;
        del.style.display = "inline-block";
        add.style.display = "inline-block";
    }

    if (count_cer == 0) {
        del.style.display = "none";// Display the add button, hide the delete button
        add.style.display = "inline-block";
    }




}