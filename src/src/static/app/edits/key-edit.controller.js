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
        $scope.isRoom = 1;
        $scope.isPreloading = false;

        $scope.proceed = proceed;
        $scope.cancel = cancel;

        init();

        function init() {
            service.getKey(keyId).then(function (response) {
                var key = response.data;
                $log.info('Key info loaded: ' + key);
                $scope.isRoom = (key.block_name.includes('F') && key.sector_name.includes('A')) ? 2 : 1;
                $scope.tagData = key.tag_id;
                $scope.roomId = key.room_id;
                $scope.blockName = key.block_name;
                $scope.sectorName = key.sector_name;
                $scope.floor = key.floor;
                $scope.roomRepr = key.room_repr;
                $scope.isPreloading = false;
            }).catch(function (error) {
                $log.error('Failed to load key data... ' + error.data);
                $location.url('/home');
            });
        }

        function proceed() {
            var key = {
                id: keyId,
                tag_id: $scope.tagData,
                room_id: $scope.roomId,
                block_name: $scope.blockName,
                sector_name: $scope.sectorName,
                floor: $scope.floor,
                room_repr: $scope.roomRepr
            };
            $log.info('Key: ', key);
            service.updateKey(key).then(function (response) {
                $log.info('Updated key: ' + response.data);
                $location.url('/keys');
            }).catch(function (error) {
                $log.error('Failed to create key... ' + error.data);
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();