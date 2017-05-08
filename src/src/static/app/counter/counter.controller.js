(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('CounterController', CounterController);

    CounterController.$inject = ['$scope', '$timeout'];
    function CounterController($scope, $timeout) {
        $scope.message = ' OPREZ! Vremena preostalo za očitanje: ';
        $scope.counter = 20;

        startCounting();

        function startCounting() {
            while (parseInt($scope.counter.toString()) > 0) {
                $timeout(function () {
                    $scope.$apply(function () {
                        $scope.counter -= 1;
                    });
                }, 1000);
                if ($scope.tagData != undefined && $scope.tagData != '' && $scope.tagData != null) {
                    $scope.counter = 0;
                }
            }
        }
    }
})();