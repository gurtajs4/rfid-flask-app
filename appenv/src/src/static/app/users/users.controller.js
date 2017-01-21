(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersController', UsersController);

    UsersController.$inject = ['$log', 'usersService'];
    function UsersController($log, usersService) {
        var self = this;
        var service = usersService;

        self.list = [];

        activate();

        function activate() {
            service.getItems(function (response) {
                var data = response.data;
                $log.info(data);
                var viewModel = [];
                for (var i = 0; i < data.length; i++) {
                    var singleViewModel = data[i];
                    $log.info(singleViewModel);
                    viewModel.push(JSON.parse(singleViewModel));
                }
                self.list = viewModel;
            });
        }
    }
})();