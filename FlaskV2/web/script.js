function getSuperheroName() {
    var power = document.getElementById("power").value;
    var animal = document.getElementById("animal").value;
    var color = document.getElementById("color").value;

    fetch("/generate_superhero_name", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ power: power, animal: animal, color: color }),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerHTML = data.superhero_name;
        })
        .catch(error => {
            console.error('Error fetching superhero name:', error);
        });
}
