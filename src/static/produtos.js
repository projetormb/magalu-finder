var myApp = angular.module("myApp", []);

myApp.controller("myController", function($scope, $http){

    $scope.produtos = [];
    $scope.newProduto = {};
    $scope.info = "";

    $scope.loadProdutos = function(){
            $http.get("/Products/", {})
                 .then(function successCallback(response) {
                         for (i = 0; i < response.data.length; i++) { 
                              p = response.data[i];
                              $scope.produtos.push({ id : p.id,  descricao: p.descricao, venda : p.venda });
                         };
                       }, 
                       function errorCallback(response) {
                                console.log('errorCallback') ;
                       });
                   };


    $scope.loadProdutos();

    $scope.saveProduto = function(){
        $http.post("/Products/", { 
                    'id': $scope.newProduto.id,
                    'descricao': $scope.newProduto.descricao,
                    'venda': $scope.newProduto.venda })
                .then(function successCallback(response) {
                               $scope.produtos.push($scope.newProduto);
                               $scope.info = "Novo Produto Inserido !";
                               $scope.newProduto = {};
                      }, 
                      function errorCallback(response) {
                               console.log('errorCallback') ;
                      });


    };

    $scope.updateProduto = function(){
        $http.put("/Products/", { 
                    'id': $scope.clickedProduto.id,
                    'descricao': $scope.clickedProduto.descricao,
                    'venda': $scope.clickedProduto.venda })
                .then(function successCallback(response) {
                               $scope.info = "Produto Atualizado !";
                               $scope.newProduto = {};
                      }, 
                      function errorCallback(response) {
                               console.log('errorCallback') ;
                      });


    };


    $scope.selectProduto = function(produto){
        $scope.clickedProduto = produto;
    };

    $scope.deleteProduto = function(){
        $http.delete("/Products/Delete/" + $scope.clickedProduto.id + "/")
                .then(function successCallback(response) {
                               $scope.produtos.splice($scope.produtos.indexOf($scope.clickedProduto), 1);
                               $scope.info = "Produto excluído com sucesso !";
        
                      }, 
                      function errorCallback(response) {
                               console.log('errorCallback') ;
                      });

        /*
        $scope.produtos.splice($scope.produtos.indexOf($scope.clickedProduto), 1);
        $scope.info = "Produto excluído com sucesso !";
        */
    };

    $scope.clearInfo = function(){
        $scope.info = "";
    };
});
