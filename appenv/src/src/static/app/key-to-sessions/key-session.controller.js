(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('KeySessionController', KeySessionController);

    KeySessionController.$inject = ['keysService'];
    function KeySessionController(keyService) {
        var self = this;
        var service = keyService;

        init();

        function init() {
            var waitSocket = setInterval(function () {
                if (self.result != {}) {
                    service.activeSession(self.result).then(function (response) {
                        self.result = response.data;
                    });
                    stopIntervalWaiter()
                }
            }, 1000);

            function stopIntervalWaiter() {
                clearInterval(waitSocket);
            }
        }

        /*
         function activate() {
         $socket().then(function (socket) {
         var sid = 0;
         socket.emit('sid request');
         var waitSocket = setTimeout(function () {
         socket.on('sid response', function (response) {
         sid = response.data;
         stopIntervalWaiter()
         });
         }, 500);
         socket.emit('find key session', self.result);
         waitSocket = setTimeout(function () {
         socket.on('key session result', function (response) {
         console.log(response.data);
         self.result = response.data;
         stopIntervalWaiter()
         });
         }, 1000);

         function stopIntervalWaiter() {
         clearInterval(waitSocket);
         }
         });
         }
         */
    }
})();