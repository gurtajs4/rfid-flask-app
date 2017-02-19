(function () {
    'use strict';
    angular.module('appMain').controller('KeysController', KeysController);

    KeysController.$inject = ['$log', 'keysService'];
    function KeysController($log, keysService) {
        var self = this;
        var service = keysService;

        self.deleteSelected = deleteSelected;

        init();

        function init() {
            service.getItems().then(function (response) {
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

        function deleteById(id) {
            return service.keyDelete(id).then(function (response) {
                return true;
            }).catch(function (error) {
                $log.error(' error: ' + error);
                return false;
            });
        }

        function deleteSelected() {
            var selectedList = self.list.filter(function (session) {
                return session.isSelected;
            });
            for (var i = 0; i < selectedList.length; i++) {
                if (!deleteById(selectedList[i].id)) {
                    $log.error('Failed to delete session with id ' + id.toString());
                }
            }
            self.list = self.list.filter(function (session) {
                return selectedList.indexOf(session) < 0;
            });
        }
    }
})();