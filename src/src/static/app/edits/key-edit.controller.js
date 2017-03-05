(function () {
    'use strict';
    angular.module('appMain').controller('KeyEditController', KeyEditController);

    KeyEditController.$inject = ['$scope', '$log', '$routeParams', '$location', 'updateService'];
    function KeyEditController($scope, $log, $routeParams, $location, updateService) {
        var keyId = $routeParams.id;
        var service = updateService;

        $scope.title = "Stranica za uređivanje podataka o ključu";

        $scope.note = "Uredite podatke o ključu i prostoriji pridjeljujući broj prostorije s ostalim podacima poput odjela.";
        $scope.tagData = "";
        $scope.message = "";

        $scope.proceed = proceed;
        $scope.cancel = cancel;

        init();

        function init() {
            service.getKey(keyId)
                .then(function (response) {
                    if (response.status == 200) {
                        $location.url('/home');
                    }
                    else {
                        $log.debug('Response status is not 200 on editing key data: ' + response.data);
                    }
                }).catch(function (error) {
                    $log.error('Failed to load key data... ' + error.data);
                });
        }

        function proceed() {
            var key = {
                id: keyId,
                tag_id: $scope.tagData,
                room_id: $scope.roomId,
                block_name: $scope.blockName,
                sector_name: $scope.sectorName,
                floor: $scope.floor
            };
            $log.info('Key: ', key);
            service.registerKey(key)
                .then(function (response) {
                    if (response.status == 200) {
                        $location.url('/home');
                    }
                    else {
                        $log.debug('Response status is not 200 on registering key: ' + response.data);
                    }
                })
                .catch(function (error) {
                    $log.error('Failed to create key... ' + error.data);
                });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();