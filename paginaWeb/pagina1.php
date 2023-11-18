<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/x-icon" href="data:image/x-icon;,">
  <title>Cuantos titulos tiene cada pagina</title>
</head>
<body>
  <div class="container">
    <header>
      <h1>Información de la Tabla</h1>
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
      $sql = "SELECT * FROM resultados1a";
      $result = $conn->query($sql);

      echo "<h2>Información de la Tabla</h2>";

      if ($result->num_rows > 0) {
          echo "<table>";
          echo "<tr><th>ID</th><th>Título</th><th>Conteo</th></tr>";

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
