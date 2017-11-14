var myApp = angular.module("myApp", []);

myApp.controller("myController", function($scope, $http){

    $scope.lojas = [];
    $scope.newLoja = {};
    $scope.info = "";

    $scope.loadLojas = function(){
            $http.get("/Stores/", {})
                 .then(function successCallback(response) {
                         for (i = 0; i < response.data.length; i++) { 
                              var p = response.data[i];
                              $scope.lojas.push({ id : p.id,  descricao: p.descricao, cep : p.cep });
                         };
                       }, 
                       function errorCallback(response) {
                                console.log('errorCallback') ;
                       });
                   };


    $scope.loadLojas();

    $scope.saveLoja = function(){
        $http.post("/Stores/", { 
                    'id': $scope.newLoja.id,
                    'descricao': $scope.newLoja.descricao,
                    'cep': $scope.newLoja.cep })
                .then(function successCallback(response) {
                               d = response.data;
                               $scope.newLoja.id = d.id;
                               $scope.lojas.push($scope.newLoja);
                               $scope.info = "Nova Loja Inserida !";
                               $scope.newLoja = {};
                      }, 
                      function errorCallback(response) {
                               console.log('errorCallback') ;
                      });


    };

    $scope.updateLoja = function(){
        $http.put("/Stores/", { 
                    'id': $scope.clickedLoja.id,
                    'descricao': $scope.clickedLoja.descricao,
                    'cep': $scope.clickedLoja.cep })
                .then(function successCallback(response) {
                               $scope.info = "Loja Atualizada !";
                               $scope.newLoja = {};
                      }, 
                      function errorCallback(response) {
                               console.log('errorCallback') ;
                      });
    };


    $scope.selectLoja = function(loja){
        $scope.clickedLoja = loja;
    };

    $scope.deleteLoja = function(){
        $http.delete("/Stores/Delete/" + $scope.clickedLoja.id + "/")
                .then(function successCallback(response) {
                               $scope.lojas.splice($scope.lojas.indexOf($scope.clickedLoja), 1);
                               $scope.info = "Loja excluída com sucesso !";
        
                      }, 
                      function errorCallback(response) {
                               console.log('errorCallback') ;
                      });

    };

    $scope.clearInfo = function(){
        $scope.info = "";
    };
});
