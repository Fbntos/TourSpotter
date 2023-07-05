$(document).ready(function() {
    // Realiza una solicitud a la API de conversión de moneda
    $.ajax({
      url: 'https://v6.exchangerate-api.com/v6/6943837dc5700b655ce71c3a/latest/USD',
      dataType: 'json',
      success: function(data) {
        // Obtiene el valor de la tasa de cambio de dólar a peso chileno
        var usdToClpRate = data.conversion_rates.CLP;

        // Calcula el valor de 1 dólar en pesos chilenos
        var usdAmount = 1;
        var clpAmount = usdAmount * usdToClpRate;

        // Inserta el valor de 1 dólar en pesos chilenos en tu página
        $('#clp-amount').text(clpAmount.toFixed(2));
      },
      error: function() {
        console.log('Error al obtener la tasa de cambio.');
      }
    });
  });

  $(document).ready(function() {
    // Realiza una solicitud a la API de conversión de moneda
    $.ajax({
      url: 'https://v6.exchangerate-api.com/v6/6943837dc5700b655ce71c3a/latest/EUR',
      dataType: 'json',
      success: function(data) {
        // Obtiene el valor de la tasa de cambio del euro a peso chileno
        var eurToClpRate = data.conversion_rates.CLP;
  
        // Calcula el valor de 1 euro en pesos chilenos
        var eurAmount = 1;
        var clpAmount = eurAmount * eurToClpRate;
  
        // Inserta el valor de 1 euro en pesos chilenos en tu página
        $('#clp-amount-eur').text(clpAmount.toFixed(2));
      },
      error: function() {
        console.log('Error al obtener la tasa de cambio.');
      }
    });
  });