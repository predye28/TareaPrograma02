<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/x-icon" href="data:image/x-icon;,">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans">
  <title>Cuántas palabras distintas tiene</title>
</head>
<body>
  <div class="container">
    <header>
      <h1>¿Cuántas palabras distintas tiene?</h1>
    </header>

    <nav>
      <ul>
        <li><a href="index.html">Volver al Menú Principal</a></li>
      </ul>
    </nav>

    <?php
      include 'conexion.php';
      
      $sql = "SELECT * FROM resultados1b";
      $result = $conn->query($sql);

      echo "<h2>Información de la Tabla</h2>";

      if ($result->num_rows > 0) {
          echo "<table>";
          echo "<tr><th>ID</th><th>Página</th><th>Cantidad</th></tr>";

          while($row = $result->fetch_assoc()) {
              echo "<tr><td>" . $row["id"] . "</td><td>" . $row["title"] . "</td><td>" . $row["count"] . "</td></tr>";
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
