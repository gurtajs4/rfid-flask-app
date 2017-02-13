(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserSessionsController', UserSessionsController);

    UserSessionsController.$inject = ['$scope', '$timeout', 'searchSessionsService'];
    function UserSessionsController($scope, $timeout, searchSessionsService) {
        var service = searchSessionsService;

        init();

        function init() {
            service.getSessionsByUser($scope.userId).then(function (response) {
                $timeout(function () {
                    $scope.apply(function () {
                        var data = response.data;
                        var viewModel = [];
                        for (var i = 0; i < data.length; i++) {
                            viewModel.push(JSON.parse(data[i]));
                        }
                        $scope.result = viewModel;
                    });
                }, 0);
            });
        }
    }
})();