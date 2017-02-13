(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeySessionsController', KeySessionsController);

    KeySessionsController.$inject = ['$scope', '$timeout', 'searchSessionsService'];
    function KeySessionsController($scope, $timeout, searchSessionsService) {
        var service = searchSessionsService;

        init();

        function init() {
            service.getSessionsByKey($scope.keyId).then(function (response) {
                $timeout(function () {
                    $scope.$apply(function () {
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