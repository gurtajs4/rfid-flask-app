(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserRegisterController', UserRegisterController);

    // UserRegisterController.$inject = ['$scope', '$log', '$location', 'Upload', 'registerService'];
    // function UserRegisterController($scope, $log, $location, Upload, registerService) {

    UserRegisterController.$inject = ['$scope', '$log', '$location', 'registerService'];
    function UserRegisterController($scope, $log, $location, registerService) {
        var service = registerService;

        $scope.title = "Stranica za registraciju korisnika";
        $scope.note = "Registrirajte korisnika pridruživanjem informacija o RFID kartici sa podacima o korisniku";

        $scope.tagData = "";
        $scope.message = "";
        $scope.isPreloading = false;

        $scope.proceed = proceed;
        $scope.cancel = cancel;
        $scope.isNotValid = isNotValid;


        function isNotValid() {
            return ($scope.tagData == '' || $scope.firstName == '' || $scope.lastName == '' || $scope.email == '' || $scope.role == '');
        }

        function proceed() {
            var user = {
                tag_id: $scope.tagData,
                first_name: $scope.firstName,
                last_name: $scope.lastName,
                email: $scope.email,
                role_id: $scope.role
            };
            $log.info('User data is: ', user);
            var image = $scope.image;
            $log.info('Image is ', image);
            // Upload.upload({
            //     url: '/api/users/register',
            //     data: {file: $scope.image, 'user_json': JSON.stringify(user), 'user': user}
            // }).then(function (response) {
            service.registerUser(user, image).then(function (response) {
                $log.info('Success ' + response.data['pic_url'] + 'uploaded. Response: ' + response.data);
                $location.url('/users');
            }).catch(function (error) {
                $log.error('Error status: ' + error.status);
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();