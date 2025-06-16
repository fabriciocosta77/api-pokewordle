function gerarCabecalhos(json) {
    const container = document.getElementById("container");
    const jaTemCabecalhos = container.querySelector(".cabecalho");

    if (jaTemCabecalhos) return;

    container.innerHTML = "";
    Object.keys(json).forEach(key => {
        const divCabecalho = document.createElement("div");
        divCabecalho.classList.add("cabecalho");
        divCabecalho.textContent = key;
        container.appendChild(divCabecalho);
    });
}

function gerarValores(json) {
    const container = document.getElementById("container");
    Object.values(json).forEach(value => {
        const divValor = document.createElement("div");
        divValor.classList.add("valor");
        divValor.classList.add("centralizaTexto");
        let status = value.at(-3)
        if (status == 'S') {
            divValor.classList.add("certo")
        } else {
            divValor.classList.add("errado")
        }

        const textoFinal = value.slice(2, -3);
        if (typeof textoFinal === "string" && (textoFinal.startsWith("http") || textoFinal.endsWith(".png") || textoFinal.endsWith(".jpg") || textoFinal.endsWith(".jpeg") || textoFinal.endsWith(".gif"))) {
            const img = document.createElement("img");
            img.src = textoFinal;
            img.style.maxWidth = "150px"; 
            img.style.display = "block";
            divValor.appendChild(img);
        } else {
            divValor.textContent += textoFinal;
        }

        container.appendChild(divValor);
    });
}

function limpaValores() {
    const container = document.getElementById("container");
    container.innerHTML = "";
}

async function sorteiaNovo() {
    const url = "http://localhost:8000/pkmn/sorteia";
    const carregandoDiv = document.getElementById("loadingSorteio");
    carregandoDiv.style.display = "block";

    try {
      const response = await fetch(url, {
        method: "POST"
      });
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const json = await response.json();
      console.log(json);
    } catch (error) {
      console.error(error.message);
    } finally {
        carregandoDiv.style.display = "none";
    }
  }
  

async function pegaChute() {
    let chute = document.getElementById("textoChute").value;

    if (chute == "missingno" || chute == "missing-no" || chute == "missing_no") {
        setTimeout(function() {
            window.close()
        }, 1)
    }
    const url = "http://localhost:8000/pkmn/chute/" + chute;

    const carregandoDiv = document.getElementById("loadingChute");
    carregandoDiv.style.display = "block";

    try {
        const response = await fetch(url, {
            method: "POST"
        });
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
  
        const json = await response.json();

        console.log(json);

        gerarCabecalhos(json);
        gerarValores(json);
    
    } catch (error) {
        console.error(error.message);
    } finally {
        carregandoDiv.style.display = "none";
    }
  }
  