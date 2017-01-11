(function () {
    'use strict';
    angular.module('appMain').controller('KeysController', KeysController);

    KeysController.$inject = ['$log', 'keysService'];
    function KeysController($log, keysService) {
        var self = this;
        var service = keysService;

        activate();

        function activate() {
            service.getAllItems().then(function (response) {
                self.list = response.data;
            }).catch(function (error) {
                $log.error("Failed loading all stored items ", error);
            })
        }
    }
})();