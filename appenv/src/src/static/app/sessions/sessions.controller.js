(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('SessionsController', SessionsController);

    SessionsController.$inject = ['sessionService'];
    function SessionsController(sessionService) {
        var self = this;
        var service = sessionService;

        self.list = [];

        init();

        function init() {
            service.sessions().then(function (response) {
                var data = response.data;
                var viewModel = [];         //new Array();
                for (var i = 0; i < data.length; i++) {
                    viewModel.push(JSON.parse(data[i]));
                }
                self.list = viewModel;
            });
        }
    }
})();