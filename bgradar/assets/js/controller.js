angular.module('bgradarApp.controllers', [])
  .controller('WallController', ['$scope',
  	 function($scope) {
  	 	var init = function(){
			console.log("Hello world");
		}
		init();
  	}])
  .controller('RadarController', ['$scope',
  	 function($scope) {
  	 	var init = function(){
			$scope.map = {
			    center: {
			        latitude: 45,
			        longitude: -73
			    },
			    zoom: 8
			};
		}
		init();
  	}])