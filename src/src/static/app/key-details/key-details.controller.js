(function () {
    'use strict';

    angular.module('appMain').controller('KeyDetailsController', KeyDetailsController);

    KeyDetailsController.$inject = ['$scope', '$routeParams', '$location', '$log', 'keysService'];
    function KeyDetailsController($scope, $routeParams, $location, $log, keysService) {
        var service = keysService;

        $scope.keyId = $routeParams.id;
        $scope.deleteItem = deleteItem;

        init();

        function init() {
            service.getItem($scope.keyId).then(function (response) {
                var data = response.data;
                $log.info('Raw data from response is: ' + data);
                // $scope.keyData = JSON.parse(data);
                $scope.keyData = data;
            });
        }

        function deleteItem() {
            if ($scope.userData.isSelected) {
                service.keyDelete($scope.keyId).then(function (response) {
                    $location.url('/keys');
                }).catch(function (error) {
                    window.alert(' error: ' + error);
                });
            }
        }
    }
})();