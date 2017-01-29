(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeySessionsController', KeySessionsController);

    KeySessionsController.$inject = ['$scope', 'timeout', 'searchSessionsService'];
    function KeySessionsController($scope, $timeout, searchSessionsService) {
        var service = searchSessionsService;

        init();

        function init() {
            service.getSessionsByKey(self.result).then(function (response) {
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

            // var isRunningSearch = $interval(function () {
            //     if (self.result != {}) {
            //         service.getSessionsByKey(self.result).then(function (response) {
            //             self.result = response.data;
            //         });
            //         stopIntervalWaiter()
            //     }
            // }, 1000);
            //
            // function stopIntervalWaiter() {
            //     $interval.cancel(isRunningSearch);
            // }
        }
    }
})();