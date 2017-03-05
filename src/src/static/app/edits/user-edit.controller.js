(function () {
    'use strict';
    angular.module('appMain').controller('UserEditController', UserEditController);

    UserEditController.$inject = ['$scope', '$log', '$routeParams', '$location', 'updateService'];
    function UserEditController($scope, $log, $routeParams, $location, updateService) {
        var userId = $routeParams.id;
        var service = updateService;

        $scope.title = "Stranica za uređivanje podataka korisnika";
        $scope.note = "Uredite podatke korisnika pridruživanjem informacija o RFID kartici sa podacima o korisniku";

        $scope.tagData = "";
        $scope.message = "";

        $scope.proceed = proceed;
        $scope.cancel = cancel;
        $scope.isNotValid = isNotValid;

        init();

        function init() {
            service.getUser(userId)
                .then(function (response) {
                    if (response.status == 200) {
                        $location.url('/home');
                    }
                    else {
                        $log.debug('Response status is not 200 on editing user data: ' + response.data);
                    }
                }).catch(function (error) {
                    $log.error('Failed to load user data... ' + error.data);
                });
        }

        function isNotValid() {
            return ($scope.tagData == '' || $scope.firstName == '' || $scope.lastName == '' || $scope.email == '' || $scope.role == '');
        }

        function proceed() {
            var user = {
                id: userId,
                tag_id: $scope.tagData,
                first_name: $scope.firstName,
                last_name: $scope.lastName,
                email: $scope.email,
                role_id: $scope.role
            };
            $log.info('User data is ', user);
            var image = $scope.image;
            $log.info('Image name is ', image);
            service.updateUser(user, image)
                .then(function (response) {
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