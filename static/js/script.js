document.getElementById("marca").addEventListener("change", async function() {
    const brand = this.value;

    const selectVersion = document.getElementById("version");
    selectVersion.innerHTML = "";
    selectVersion.disabled = true;

    const respuesta = await fetch(`/models/${encodeURIComponent(brand)}`);
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

    if (modelos.length === 1) {
        selectModelo.dispatchEvent(new Event("change"));
    }
});

document.getElementById("modelo").addEventListener("change", async function() {
    
    const brand = document.getElementById("marca").value;
    const model = this.value;
    console.log("brand:", brand, "model:", model);

    const respuesta = await fetch(`/versions/${encodeURIComponent(brand)}/${encodeURIComponent(model)}`);
    const versions = await respuesta.json();
    console.log("versiones recibidas:", versions);

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

document.querySelector("form").addEventListener("submit", function (e) {
    const fotoInput = document.getElementById("fotos");
    if (fotoInput.files.length === 0) {
        const continuar = confirm("There's no photo selected. Do you want to continue without uploading a photo?");
        if (!continuar) {
            e.preventDefault();
        }
    }
});