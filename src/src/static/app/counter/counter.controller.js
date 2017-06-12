(function () {
    'use-strict';

    angular
        .module('appMain')
        .controller('CounterController', CounterController);

    CounterController.$inject = ['$scope', '$timeout'];
    function CounterController($scope, $timeout) {
        $scope.message = ' OPREZ! Vremena preostalo za očitanje: ';
        $scope.counter = 20;

        var updateCounter = function () {
            $scope.counter++;
            if ($scope.counter >= 0 || $scope.tagData != '') {
                $timeout(updateCounter, 1000);
            }
            else {
                $scope.counter = 0;
            }
        };

        updateCounter();

        /*
         var stop;


         $scope.$watch('tagData', function (value) {
         if (value != undefined && value != '' && value != null) {
         $scope.stopCounting();
         }
         });

         $scope.timedCount = function () {
         if (angular.isDefined(stop)) return;

         stop = $interval(function () {
         if (parseInt($scope.counter.toString()) > 0) {
         $scope.counter = parseInt($scope.counter.toString()) - 1;
         }
         else {
         $scope.stopCounting();
         }
         }, 1000);
         };

         $scope.resetCount = function () {
         $scope.counter = 20;
         };

         $scope.stopCounting = function () {
         if (angular.isDefined(stop)) {
         $interval.cancel(stop);
         stop = undefined;
         }
         };

         $scope.$on('$destroy', function () {
         $scope.stopCounting();
         });*/
    }
})();