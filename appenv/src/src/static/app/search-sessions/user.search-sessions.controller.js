(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UserSessionsController', UserSessionsController);

    UserSessionsController.$inject = ['$scope', '$timeout', 'userSessionsService'];
    function UserSessionsController($scope, $timeout, userSessionsService) {
        var service = userSessionsService;

        init();

        function init() {
            service.getSessionsByUser(self.userId).then(function (response) {
                $timeout(function () {
                    $scope.apply(function () {
                        var data = response.data;
                        var viewModel = [];
                        for (var i = 0; i < data.length; i++) {
                            viewModel.push(JSON.parse(data[i]));
                        }
                        $scope.result = viewModel;
                    });
                }, 0);
            });
        }
    }
})();