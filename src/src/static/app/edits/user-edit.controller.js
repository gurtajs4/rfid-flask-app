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
        $scope.isPreloading = true;

        $scope.proceed = proceed;
        $scope.cancel = cancel;
        $scope.isNotValid = isNotValid;

        init();

        function init() {
            service.getUser(userId).then(function (response) {
                // var user = JSON.parse(response.data);
                var user = response.data;
                $log.info('User info loaded: ' + user);
                $scope.tagData = user.tag_id;
                $scope.email = user.email;
                $scope.firstName = user.first_name;
                $scope.lastName = user.last_name;
                $scope.role = user.role_id;
                $scope.image = user.pic_url;
            }).catch(function (error) {
                $log.error('Failed to load user data... ' + error.data);
                $location.url('/home');
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
            service.updateUser(user, image).then(function (response) {
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