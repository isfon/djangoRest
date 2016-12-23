function productsFactory ($http, $q){
	var factory = {};
	var paths = {
		getProducts: "/api/productos.json"
	};

	factory.getProducts = function(){
		var data = '';
        $http.get(paths.getProducts).success(function (response) {
            data = response;
            console.log(data);
        });
        return data;
	}

	return factory;
}

angular
	.module('app')
	.factory('productsFactory', productsFactory);