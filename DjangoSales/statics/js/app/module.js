function routeConf ($stateProvider, $urlRouterProvider){
	
	$urlRouterProvider.otherwise('/login');
  	var states = [
       {
        name: "home",
        template: '<ui-view></ui-view>',
        abstract: true,
        data: {
            pageTitle: 'Procesos'
        },
      },
      {
        name: 'home.login',
        data: {
            pageTitle: 'Login'
        },
        url: '/login',
        templateUrl: 'static/js/app/modules/login/views/login.html',
        controller: 'loginCtrl',
        controllerAs: '$ctrl'
      },
      {
        name: 'home.dashboard',
        data: {
            pageTitle: 'Bienvenido'
        },
        url: '/administrador',
        templateUrl: 'static/js/app/modules/home/views/dashboard.html',
        controller: 'dashboardCtrl',
        controllerAs: '$ctrl'
      },
    ];

	states.forEach(function(state) {
      $stateProvider.state(state);
    });
}


angular
	.module('app')
	.config(routeConf);