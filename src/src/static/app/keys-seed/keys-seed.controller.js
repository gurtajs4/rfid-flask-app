(function () {
    'use strict';

    angular.module('appMain').controller('KeysSeedController', KeysSeedController);

    KeysSeedController.$inject = ['$socket', '$location', '$window', '$log', 'Upload'];
    function KeysSeedController($socket, $location, $window, $log, Upload) {

        var self = this;

        self.getTemplate = getTemplate;
        self.send = send;
        self.cancel = cancel;

        function getTemplate() {

            $socket().then(function (socket) {

                $log.info('creating socket instance');

                socket.on('connect', function (message) {
                    socket.emit('client sid request', {});
                });

                socket.on('response sid', function (message) {
                    var uid = message;
                    socket.emit('download template', {
                        room: uid
                    });
                });

                socket.on('download begins', function (response) {
                    var data = response['file'];
                    // var splitPath = data.split('/');
                    // var filename = splitPath.split(splitPath.length - 1);
                    var blob = new Blob([data], {
                        type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    });
                    $window.saveAs(blob, 'seed_data.xlsx');
                });
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
                var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                $log.info('progress: ' + progressPercentage + '% ' + evt.config.data.file.name);
            });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();