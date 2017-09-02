(function () {
    'use-strict';

    angular
        .module('administration')
        .directive('navigationSidebar', navigationSidebar);

    navigationSidebar.$inject = ['templateProvider'];
    function navigationSidebar(templateProvider) {
        var appBaseUrl = templateProvider.appBaseUrl();
        return {
            retstrict: 'E',
            scope: false,
            controller: 'SidebarController',
            templateUrl: appBaseUrl + '/navigation-sidebar/navigation-sidebar.html'
        }
    }
})();