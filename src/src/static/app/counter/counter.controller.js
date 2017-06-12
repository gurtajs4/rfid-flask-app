(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('CounterController', CounterController);

    CounterController.$inject = ['$scope', '$interval'];
    function CounterController($scope, $interval) {
        $scope.message = ' OPREZ! Vremena preostalo za očitanje: ';
        $scope.counter = 20;

        var stop;

        $scope.$watch('tagData', function (value) {
            if (value != undefined && value != '' && value != null) {
                $scope.stopCounting();
            }
        });

        $scope.startCounting = function () {
            if (angular.isDefined(stop)) return;

            stop = $interval(function () {
                if (parseInt($scope.counter.toString()) > 0) {
                    $scope.counter = parseInt($scope.counter.toString()) - 1;
                }
                else {
                    $scope.stopCounting();
                }
            }, 20);
        };

        $scope.stopCounting = function () {
            if (angular.isDefined(stop)) {
                $interval.cancel(stop);
                stop = undefined;
            }
        };

        $scope.$on('$destroy', function () {
            $scope.stopCounting();
        });
    }
})();