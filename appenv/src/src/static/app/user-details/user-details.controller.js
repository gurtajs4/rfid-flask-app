(function () {
    'use strict';

    angular.module('appMain').controller('UserDetailsController', UserDetailsController);

    UserDetailsController.$inject = ['$scope', '$routeParams', 'usersService'];
    function UserDetailsController($scope, $routeParams, usersService) {
        var service = usersService;

        $scope.userId = $routeParams.id;

        init();

        function init() {
            service.getItem($scope.userId).then(function (response) {
                var data = response.data;
                $scope.userData = JSON.parse(data);
            });
        }
    }
})();