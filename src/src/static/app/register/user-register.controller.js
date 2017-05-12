(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$scope', '$log', '$location', 'registerService', 'authService'];
    function UserRegisterController($scope, $log, $location, registerService, authService) {
        var service = registerService;

        $scope.title = "Stranica za registraciju korisnika";
        $scope.note = "Registrirajte korisnika pridruživanjem informacija o RFID kartici sa podacima o korisniku";

        $scope.tagInfo = {
            tagId: "",
            message: ""
        };
        $scope.isPreloading = false;
        $scope.roleOptions = [
            {id: 1, name: 'Profesor'},
            {id: 2, name: 'Student'}
        ];
        $scope.errorRegistering = {
            firstname: '', lastname: '', email: '', password: '', password2: '', imageFile: ''
        };

        $scope.proceed = proceed;
        $scope.cancel = cancel;
        $scope.isValid = isValid;

        function isValid() {
            var _isValid = true;
            if (!$scope.firstname) {
                $scope.errorRegistering.firstname = 'Ovo polje je obavezno!';
                _isValid = false;
            }
            if (!$scope.lastname) {
                $scope.errorRegistering.lastname = 'Ovo polje je obavezno!';
                _isValid = false;
            }
            if (!$scope.email) {
                $scope.errorRegistering.email = 'Ovo polje je obavezno!';
                _isValid = false;
            }
            if (!$scope.password) {
                $scope.errorRegistering.password = 'Ovo polje je obavezno!';
                _isValid = false;
            }
            if (!$scope.password2) {
                $scope.errorRegistering.password2 = 'Ovo polje je obavezno!';

                _isValid = false;
            }
            if ($scope.password2 != $scope.password) {
                $scope.errorRegistering.password2 = 'Lozinke moraju biti jednake!';
                _isValid = false;
            }
            if ($scope.password.length < 9) {
                $scope.errorRegistering.password = 'Lozinka je sigurna kao ima više od 8 znakova!';
                _isValid = false;
            }
            return _isValid;
        }

        function proceed(callback) {
            if (isValid()) {
                var user = {
                    tag_id: $scope.tagInfo.tagId,
                    first_name: $scope.firstName,
                    last_name: $scope.lastName,
                    email: $scope.email,
                    password: $scope.password,
                    role_id: $scope.role
                };
                $log.info('User data is: ', user);
                var image = $scope.image;
                $log.info('Image is ', image);
                service.registerUser(user, image).then(function (response) {
                    var token = response.data.token;
                    $log.info(response.data.data);
                    $log.info(token);
                    authService.setCredentials(user.email, token, function () {
                        callback(response.data);
                        $location.url('/home');
                    });
                }).catch(function (error) {
                    $log.error('Error status: ', error);
                });
            }
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();