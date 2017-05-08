(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$scope', 'authService'];
    function LoginController($scope, authService) {
        var service = authService;

        $scope.loginErrro = {};

        $scope.doLogin = doLogin;
        $scope.isValid = isValid;

        function isValid() {
            var _isValid = true;
            if (!$scope.email) {
                $scope.loginError.email = 'Ovo polje je obavezno!';
                _isValid = false;

            }
            if (!$scope.password) {
                $scope.loginError.password = 'Ovo polje je obavezno!';
                _isValid = false;

            }
            if ($scope.password.length < 9) {
                $scope.loginError.password = 'Lozinka je sigurna kao ima više od 8 znakova!';
                _isValid = false;

            }
            return _isValid;
        }

        function doLogin(callback) {
            if (isValid()) {
                service.login($scope.email, $scope.password)
                    .then(function (response) {
                        var token = response.data['token'];
                        service.setCredentials($scope.email, token, callback);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        }
    }
})();