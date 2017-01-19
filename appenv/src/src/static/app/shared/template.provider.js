(function () {
    'use strict';

    angular
        .module('appMain')
        .provider('templateServiceProvider', templateServiceProvider);

    function templateServiceProvider() {
        this.$get = templateService;

        function templateService() {
            var service = {
                appBaseUrl: appBaseUrl,
                sharedBaseUrl: sharedBaseUrl
            };

            return service;

            function appBaseUrl() {
                return angular.element(document.querySelector('base')).attr('href') + 'static/app';
            }

            function sharedBaseUrl() {
                return angular.element(document.querySelector('base')).attr('href') + 'static/shared-components';
            }
        }
    }
})();