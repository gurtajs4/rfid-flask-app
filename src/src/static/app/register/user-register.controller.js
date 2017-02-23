(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    UserRegisterController.$inject = ['$scope', '$log', '$location', 'Upload', 'registerService'];
    function UserRegisterController($scope, $log, $location, Upload, registerService) {
        var service = registerService;

        $scope.title = "Stranica za registraciju korisnika";
        $scope.note = "Registrirajte korisnika pridruživanjem informacija o RFID kartici sa podacima o korisniku";

        $scope.tagData = "";
        $scope.message = "";

        $scope.register = register;
        $scope.cancel = cancel;
        $scope.isNotValid = isNotValid;


        function isNotValid() {
            return ($scope.tagData == '' || $scope.firstName == '' || $scope.lastName == '' || $scope.email == '' || $scope.role == '');
        }

        function register() {
            var user = {
                tag_id: $scope.tagData,
                first_name: $scope.firstName,
                last_name: $scope.lastName,
                email: $scope.email,
                role_id: $scope.role
            };
            $log.info('From client - raw user data is: ', user);
            var imgName = $scope.image.name;
            var imgType = $scope.image.type;
            $log.info('Image type is ', imgType);
            $log.info('Image name is ', imgName);
            Upload.upload({
                url: '/api/users/register',
                data: {file: $scope.image, 'user_json': JSON.stringify(user), 'user': user}
            }).then(function (response) {
                $log.info('Success ' + response.config.data.file.name + 'uploaded. Response: ' + response.data);
                $location.url('/users');
            }, function (error) {
                $log.error('Error status: ' + error.status);
            }, function (evt) {
                var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                $log.info('progress: ' + progressPercentage + '% ' + evt.config.data.file.name);
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();