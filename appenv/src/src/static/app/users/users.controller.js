(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersController', UsersController);

    UsersController.$inject = ['$log', 'usersService', 'imagesService'];
    function UsersController($log, usersService, imagesService) {
        var self = this;
        var service = usersService;
        var images = imagesService;

        self.deleteSelected = deleteSelected;

        init();

        function init() {
            service.getItems().then(function (response) {
                var data = response.data;
                $log.info(data);
                var viewModel = [];
                angular.forEach(data, function (value, key) {
                    var singleViewModel = JSON.parse(value);
                    if ("" === singleViewModel.pic_url) {
                        singleViewModel.pic_url = images.getDefaultUserProfileImageUrl();
                    }
                    this.push(singleViewModel)
                }, viewModel);
                self.list = viewModel;
            });
        }

        function deleteById(id) {
            return service.userDelete(id).then(function (response) {
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