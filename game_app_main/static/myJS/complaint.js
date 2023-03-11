$( document ).ready(function() {

    // função mudança do campo turma na form
    $("#id_turma").change(function () {

        var url = $("#participacaoForm").attr("data-alunos-url");   // get the url of the `load_alunos_da_turma` view

        var turmaId = $(this).val();               // get the selected 'turma' ID from the HTML input

        $.ajax({                           // initialize an AJAX request
            url: url,                             // set the url of the request (= localhost:8000/ajax/load-alunos/)
            data: {
                'turma': turmaId                  // add the turmaId to the GET parameters
            },
            success: function (data) {            // `data` is the return of the `load_alunos_da_turma` view function

                // replace the contents of the aluno input with the data that came from the server
                $("#id_aluno").html(data);
            }
        });

    });

    // função mudança do número do aluno na form
    $("#id_aluno").change(function () {

        var url = $("#participacaoForm").attr("data-numero-aluno-url")   // get the url of the `load_numero_aluno` view

        var alunoId = $(this).val();            // get the selected 'aluno' ID from the HTML input

        $.ajax({                        // initialize an AJAX request
            url: url,                          // set the url of the request (= localhost:8000/ajax/load_numero_aluno/)
            data: {
                'aluno': alunoId,             // add the alunoID to the GET parameters
            },
             success: function (data) {        // `data` is the return of the `load_numero_aluno` view function

                // replace the contents of número with the data that came from the server
                $("#id_class_number").html(data).attr('value', data);
            }
        });
    });


});














