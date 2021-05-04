const frameworks = [
    {
      name: "angular"
    },
    {
      name: "ember"
    },
    {
      name: "react"
    },
    {
      name: "vue"
    },
    {
      name: "abc"
    }
  ];
  frameworks.forEach( framework => {
    const card = `<div class="cardcontainer">
    <div class="images">
      <img src="mobile.jpeg" />
    </div>
    <div class="product">
      <h1>Nike Epic React Flyknit</h1>
      <p class="desc">The Nike Epic React Flyknit foam cushioning is responsive yet light-weight, durable yet soft. This creates a sensation that not only enhances the feeling of moving forward, but makes running feel fun, too.</p>
     </div>
     
    <div class="buttons">
    <button class="add cardbutton">Details</button>
        </div>
  </div>`
    const ele = document.createElement('div');
    ele.innerHTML = card;
    document.getElementById("card").appendChild(ele.firstChild);
  })