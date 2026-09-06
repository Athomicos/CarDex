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

document.getElementById("modelo").addEventListener("change", async function() {
    
    const brand = document.getElementById("marca").value;
    const model = this.value;

    const respuesta = await fetch('/versions/${brand}/${model}');
    const versions = await respuesta.json();

    const selectVersion = document.getElementById("version");
    selectVersion.innerHTML = "";
    for (const v of versions) {
        const option = document.createElement("option");
        option.value = v.id;
        option.textContent = v.version;
        selectVersion.appendChild(option);
    }
    selectVersion.disabled = false;
});