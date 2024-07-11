<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verifique se o seu PC está ligado</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            text-align: center;
        }

        button {
            font-size: 1.2rem;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            margin-bottom: 20px;
        }

        .imageContainer {
            margin-top: 20px;
        }

        #pcImage {
            max-width: 100%;
            display: none; /* Esconde a imagem por padrão */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Verifique se o seu PC está ligado</h1>
        <button id="checkButton">Verificar</button>
        <div class="imageContainer">
            <img src="" alt="Imagem" id="pcImage">
        </div>
    </div>
    <script>
        document.getElementById('checkButton').addEventListener('click', function() {
            var pcImage = document.getElementById('pcImage');
            // Substitua a URL da imagem pela sua escolha
            pcImage.src = 'caminho/para/sua/imagem.jpg'; 
            pcImage.style.display = 'block'; // Mostra a imagem
        });
    </script>
</body>
</html>
