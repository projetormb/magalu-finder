var myApp = angular.module("myApp", []);

myApp.controller("myController", function($scope){
    console.log("in controller...");
    $scope.newProduto = {};
	$scope.info = "";

    $scope.produtos = [
        { id : 1,  descricao: "TV branco e preto", venda : 2299.99 } ,
        { id : 2,  descricao: "Celular motorola tijolo", venda : 99.90 } ,
        { id : 3,  descricao: "Fogão a lenha", venda : 199.99 } 
    ];

    $scope.saveProduto = function(){
        console.log("Saving...");
        $scope.produtos.push($scope.newProduto);
        $scope.info = "Novo Produto Inserido !";
        $scope.newProduto = {};
    };

    $scope.selectProduto = function(produto){
        $scope.clickedProduto = produto;
    };

    $scope.deleteProduto = function(){
        console.log($scope.produtos.indexOf($scope.clickedProduto));
        $scope.produtos.splice($scope.produtos.indexOf($scope.clickedProduto), 1);
        $scope.info = "Produto excluído com sucesso !";
    };

    $scope.clearInfo = function(){
        $scope.info = "";
    };
});
