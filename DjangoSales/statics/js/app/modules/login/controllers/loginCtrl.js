function loginCtrl(sessionFactory,authFactory,$state){
	var vm = this;
	vm.login = login;
	initialData();


	function initialData(){
		var token = sessionFactory.getToken();
		if(token != null){
			$state.go('home.dashboard');
		}
	}

	function login(){
		authFactory.getAuth(vm.user,vm.password).then(function(data){
			if(data == "Unable to log in with provided credentials."){

			}else{
				sessionFactory.setToken(data);
				$state.go('home.dashboard');
			}
		});
	}
}

angular
	.module('app')
	.controller('loginCtrl', loginCtrl);