    // Открыть модальное окно
    function openModal() {
        var modal = document.getElementById("myModal");
        modal.style.display = "block";
    }

    // Закрыть модальное окно
    function closeModal() {
        var modal = document.getElementById("myModal");
        modal.style.display = "none";
    }



    function addEmployee() {
      var surname = document.getElementById("surnameInput").value;
      var name = document.getElementById("nameInput").value;
      var telephone = document.getElementById("telephoneInput").value;
      var mail = document.getElementById("mailInput").value;

      // Отправляем данные на серверную часть Flask
      $.ajax({
        url: "/add_employee",
        type: "POST",
        data: {
          surname: surname,
          name: name,
          telephone: telephone,
          mail: mail
        },
        success: function(response) {
           location.reload();
        },
      });
    }



     $(document).ready(function() {
            // При нажатии на кнопку "Загрузить"
            $("#uploadBtn").click(function() {
                var type = $("#typeInput").val(); // Получаем значение типа документа
                var documentPath = $("#documentInput").val(); // Получаем путь к документу

                // Отправляем данные на серверную часть Flask
                $.ajax({
                    url: "/upload",
                    type: "POST",
                    data: {
                        type: type,
                        documentPath: documentPath
                    },
                    success: function(response) {
                        alert("Документ успешно загружен!");
                    },
                    error: function(xhr) {
                        alert("Произошла ошибка при загрузке документа.");
                    }
                });
            });
     });


    function confirmDelete() {
      var deleteModal = document.getElementById("deleteModal");
      deleteModal.style.display = "block";
      return false; // Отменяем отправку формы по умолчанию
    }

    function closeDeleteModal() {
      var deleteModal = document.getElementById("deleteModal");
      deleteModal.style.display = "none";
    }

    function deleteEmployee() {
      // Выполните дополнительные действия перед удалением сотрудника (если необходимо)

      // Отправка запроса на сервер для удаления сотрудника
      var form = document.querySelector('.delete-form_user');
      form.submit();
    }


