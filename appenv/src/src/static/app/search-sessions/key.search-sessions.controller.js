(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeySessionsController', KeySessionsController);

    KeySessionsController.$inject = ['$scope', '$routeParams', 'timeout', 'searchSessionsService'];
    function KeySessionsController($scope, $routeParams, $timeout, searchSessionsService) {
        var service = searchSessionsService;
        $scope.keyId = $routeParams.id;

        init();

        function init() {
            service.getSessionsByKey($scope.keyId).then(function (response) {
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