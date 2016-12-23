function authFactory($http, $q, sessionFactory){
	var factory = {};
	var paths = {
		getAutentication: "/api-token-auth/",
	}

	factory.getAuth = function (username, password) {
        var deferred = $q.defer();
        var Parametros = {
            "username":username,
            "password":password
        };
        var token;
        $http.post('http://localhost:8000' + paths.getAutentication, JSON.stringify(Parametros)).success(function (data) {
            token = data.token;        
            deferred.resolve(token);
        }).error(function (data) {
            token = data.non_field_errors[0];
            deferred.resolve(token);
        });

        return deferred.promise;
    };


	return factory;
}

angular
	.module('app')
	.factory('authFactory',authFactory);