(function () {
    'use strict';

    angular.module('appMain').controller('KeysSeedController', KeysSeedController);

    KeysSeedController.$inject = ['$http', '$location', '$window', '$log', 'Upload'];
    function KeysSeedController($http, $location, $window, $log, Upload) {

        var self = this;

        self.getTemplate = getTemplate;
        self.send = send;
        self.cancel = cancel;

        function getTemplate() {
            $http.get('/api/data/template').then(function (response) {
                var data = response['file'];
                // var splitPath = data.split('/');
                // var filename = splitPath.split(splitPath.length - 1);
                var blob = new Blob([data], {
                    type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                });
                $window.saveAs(blob, 'seed_data.xlsx');
            });
        }

        function send() {
            Upload.upload({
                url: '/api/data/import',
                data: {file: $scope.file}
            }).then(function (response) {
                $log.info('Success ', response);
                $location.url('/keys');
            }, function (error) {
                $log.error('Error status: ', error);
            }, function (evt) {
                self.progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                $log.info('progress: ' + progressPercentage + '% ' + evt.config.data.file.name);
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();