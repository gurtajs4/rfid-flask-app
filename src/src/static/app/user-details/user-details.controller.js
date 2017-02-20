(function () {
    'use strict';

    angular.module('appMain').controller('UserDetailsController', UserDetailsController);

    UserDetailsController.$inject = ['$scope', '$routeParams', '$location', 'usersService'];
    function UserDetailsController($scope, $routeParams, $location, usersService) {
        var service = usersService;

        $scope.userId = $routeParams.id;
        $scope.deleteItem = deleteItem;

        init();

        function init() {
            service.getItem($scope.userId).then(function (response) {
                var data = response.data;
                $scope.userData = JSON.parse(data);
            });
        }

        function deleteItem() {
            if ($scope.userData.isSelected) {
                service.userDelete($scope.userId).then(function (response) {
                    $location.url('/users');
                }).catch(function (error) {
                    window.alert(' error: ' + error);
                });
            }
        }
    }
})();