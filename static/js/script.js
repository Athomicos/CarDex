document.getElementById("marca").addEventListener("change", async function() {
    const brand = this.value;

    const selectVersion = document.getElementById("version");
    selectVersion.innerHTML = "";
    selectVersion.disabled = true;

    const respuesta = await fetch(`/models/${encodeURIComponent(brand)}`);
    const modelos = await respuesta.json();

    const selectModelo = document.getElementById("modelo");
    selectModelo.innerHTML = "";

    if (modelos.length === 0) {
        const option = document.createElement("option");
        option.disabled = true;
        option.selected = true;
        option.textContent = "Ya tienes todos los modelos de esta marca";
        selectModelo.appendChild(option);
        selectModelo.disabled = true;
        return;
    }

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

    const respuesta = await fetch(`/versions/${encodeURIComponent(brand)}/${encodeURIComponent(model)}`);
    const versions = await respuesta.json();

    const selectVersion = document.getElementById("version");
    selectVersion.innerHTML = "";

    if (versions.length === 0) {
        const option = document.createElement("option");
        option.disabled = true;
        option.selected = true;
        option.textContent = "Ya tienes todas las versiones de este modelo";
        selectVersion.appendChild(option);
        selectVersion.disabled = true;
        return;
    }

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