function sessionFactory($http, $q, $state){
	var factory = {};

	factory.getToken = function(){
		var token = sessionStorage.getItem('token');
		return token;
	}

	factory.setToken = function(token){
		sessionStorage.setItem('token',token);
	}
	factory.getUser = function(){
		var user = {};
		user.usuario = sessionStorage.getItem('usuario');
		user.nombre = sessionStorage.getItem('nombre');
		user.tipo = sessionStorage.getItem('tipo');
		return user;
	}

	factory.deleteAll = function(){
		sessionStorage.clear();
		$state.go('home.login');
	}

	return factory;
}


angular
	.module('app')
	.factory('sessionFactory', sessionFactory);