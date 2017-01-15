(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserSessionsController', UserSessionsController);

    UserSessionsController.$inject = ['$routeParams', 'userSessionsService'];
    function UserSessionsController($routeParams, userSessionsService) {
        var self = this;
        var service = userSessionsService;

        self.title = '';
        self.userId = $routeParams.id;

        activate();

        function activate() {
            service.getUserSessions(self.userId).then(function (response) {
                var data = response.data;
                var viewModel = [];
                for (var i = 0; i < data.length; i++) {
                    viewModel.push(JSON.parse(data[i]));
                }
                self.list = viewModel;
            });
        }
    }
})();