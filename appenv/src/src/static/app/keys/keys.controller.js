(function () {
    'use strict';
    angular.module('appMain').controller('KeysController', KeysController);

    KeysController.$inject = ['$log', 'keysService'];
    function KeysController($log, keysService) {
        var self = this;
        var service = keysService;

        activate();

        function activate() {
            service.getItems().then(function (response) {
                var data = response.data;
                var viewModel = [];
                for (var i = 0; i < data.length; i++) {
                    viewModel.push(JSON.parse(data[i]));
                }
                self.list = viewModel;
            }).catch(function (error) {
                $log.error("Failed loading all stored items ", error);
            })
        }
    }
})();