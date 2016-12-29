(function () {
    'use strict';

    angular
        .module('appMain')
        .provider('templateServiceProvider', templateServiceProvider);

    function templateServiceProvider() {
        this.$get = templateService;

        function templateService() {
            var service = {
                appBaseUrl: appBaseUrl
            };

            return service;

            function appBaseUrl() {
                return angular.element(document.querySelector('base')).attr('href') + 'static/app';
            }
        }
    }
})();