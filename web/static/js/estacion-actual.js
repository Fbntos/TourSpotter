function getSeason() {
    // Obtiene la fecha actual
    var currentDate = new Date();

    // Obtiene el mes actual (0-11, donde 0 es enero y 11 es diciembre)
    var currentMonth = currentDate.getMonth();

    // Define los límites de los meses para cada estación
    var springStart = 9; // Octubre
    var summerStart = 0; // Enero
    var autumnStart = 3; // Abril
    var winterStart = 6; // Julio

    // Determina la estación actual
    if (currentMonth >= springStart && currentMonth < summerStart) {
      return 'PRIMAVERA';
    } else if (currentMonth >= summerStart && currentMonth < autumnStart) {
      return 'VERANO';
    } else if (currentMonth >= autumnStart && currentMonth < winterStart) {
      return 'OTOÑO';
    } else {
      return 'INVIERNO';
    }
  }

  // Obtiene el elemento HTML donde se mostrará la estación
  var seasonElement = document.getElementById('estacion');

  // Obtiene la estación actual
  var currentSeason = getSeason();

  // Inserta la estación en el elemento HTML
  seasonElement.textContent = currentSeason;