function confApp ($interpolateProvider,$httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
 	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}

function mainController ($state){
	$state.go('home.login');
}


angular
	.module('app', ['ui.router', 'angularUtils.directives.dirPagination'])
	.controller('mainController', mainController)
	.config(confApp);
