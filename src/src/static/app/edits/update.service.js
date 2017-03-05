(function () {
    'use strict';
    angular.module('appMain').service('updateService', updateService);

    updateService.$inject = ['$http', 'keysService', 'usersService', 'Upload'];
    function updateService($http, keysService, usersService, Upload) {
        var service = {
            getKey: keysService.getKey,
            getUser: usersService.getUser,
            keyUpdate: keyUpdate,
            userUpdate: userUpdate
        };

        return service;

        function keyUpdate(key) {
            return $http.put('/api/key/edit', JSON.stringify(key));
        }

        function userUpdate(user, image) {
            return Upload.upload({
                url: '/api/user/edit',
                data: {file: image, 'user_json': JSON.stringify(user), 'user': user}
            });
        }
    }
})();