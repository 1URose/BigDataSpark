1. Запустите контейнеры командой:

   ```
   docker-compose up -d
   ```
2. Перейдите в браузере по адресу:

   ```
   http://localhost:8888
   ```
3. Откройте терминал в контейнере Jupyter Notebook:

   ```
   docker exec -it jupyter-notebook bash
   ```

   Внутри контейнера выполните:

   ```
   jupyter server list
   ```

   Скопируйте сгенерированный токен и вставьте его в соответствующее поле на странице

   ```
   http://localhost:8888
   ```

   чтобы авторизоваться.
4. Запустите скрипт `to_notebook`.
5. Вернитесь в браузер на

   ```
   http://localhost:8888
   ```

   и откройте директорию `work`.
6. Последовательно выполняйте ячейки в файле `main.ipynb`.
