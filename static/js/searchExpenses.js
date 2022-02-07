const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector(".table-output");

var str = "";

searchField.addEventListener("keyup", (e) => {
  const searchValue = e.target.value;
  
  
  fetch("/search-expenses", {
    body: JSON.stringify({ searchText: searchValue }),
    method: "POST",
  })
    .then((res) => res.json())
    .then((data) => {
      str = "";
      str += "<ul class='cards'>";
      data.forEach((item) => {
        str += "<li><div class='card'><img src='" + item.cv_avatar +
          "' class='card__image' alt='' /><div class='card__overlay'><div class='card__header'><img class='card__thumb' src='/static/images/boy.jpg' /><div class='card__header-text'><h3 class='card__title' ><a href='/cv/ "+item.id+"' class='card_icon'>" +
          item.title + "</a>";
        if (item.is_published) {
          str += "<i class='check icon green'></i>";
        }

        str += `
                      </h3>
                      <span class="card__status">${item.cv_current_job}</span>
                    </div>
                  </div>
                  <p class="card__description">${item.description}
                  </p>
                </div>
              </div>
            </li>`;

      });
      str += "</ul>";

      tableOutput.innerHTML = str;
    });
});
