function mostrarHora() {
    const fecha = new Date(); 
    const hora = fecha.getHours();
    const minutos = fecha.getMinutes();
    const segundos = fecha.getSeconds();
    const horaFormateada = hora < 10 ? "0" + hora : hora;
    const minutosFormateados = minutos < 10 ? "0" + minutos : minutos;
    const segundosFormateados = segundos < 10 ? "0" + segundos : segundos;
    const reloj = document.getElementById("reloj");
    reloj.textContent = `${horaFormateada}:${minutosFormateados}:${segundosFormateados}`;
  }

  setInterval(mostrarHora, 1000);

  const miElemento = document.getElementById('mi-elemento');

