(function () {
    'use strict';

    angular.module('appMain').service('fileUploadService', fileUploadService);

    fileUploadService.$inject = ['$http', '$log'];
    function fileUploadService($http, $log) {
        var service = {
            uploadFileToUrl: uploadFileToUrl
        };
        return service;

        function uploadFileToUrl(file, uploadUrl) {
            var fd = new FormData();
            fd.append('file', file);

            $http.post(uploadUrl, fd, {
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
            }).then(function (response) {
                $log.info('From client - file upload service - response is ', response.data.message['message']);
            }).catch(function (error) {
                $log.error('From client - error: ', error);
            });
        }
    }
})();