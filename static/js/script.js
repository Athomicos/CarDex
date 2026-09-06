document.getElementById("marca").addEventListener("change", function() {

    const brand = this.value;

    const respuesta = await fetch('/models/${brand}');
    const modelos = await respuesta.json();

    const selectModelo = document.getElementById("modelo");
    selectModelo.innerHTML = "";
    for (const m of modelos) {
        const option = document.createElement("option");
        option.value = m.model;
        option.textContent = m.model;
        selectModelo.appendChild(option);
    }
    selectModelo.disabled = false;
});