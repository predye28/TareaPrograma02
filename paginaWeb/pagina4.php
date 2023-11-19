<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/x-icon" href="data:image/x-icon;,">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans">
  <title>Cuántas veces se usa cada referencia en el texto</title>
</head>
<body>
  <div class="container">
    <header>
      <h1>¿Cuántas veces se usa cada referencia en el texto?</h1>
    </header>

    <nav>
      <ul>
        <li><a href="index.html">Volver al Menú Principal</a></li>
      </ul>
    </nav>

    <?php
      // Incluir el archivo de conexión
      include 'conexion.php';

      // Consulta a la base de datos
      $sql = "SELECT title, referencias, SUM(count) AS total_count FROM resultados1d GROUP BY title, referencias";
      $result = $conn->query($sql);

      echo "<h2>Información de la Tabla</h2>";

      if ($result->num_rows > 0) {
          echo "<table>";
          echo "<tr><th>Página</th><th>Referencia</th><th>Cantidad Total</th></tr>";

          while($row = $result->fetch_assoc()) {
              echo "<tr><td>" . $row["title"] . "</td><td>" . $row["referencias"] . "</td><td>" . $row["total_count"] . "</td></tr>";
          }

          echo "</table>";
      } else {
          echo "0 resultados";
      }

      $conn->close();
    ?>
  </div>
</body>
</html>


