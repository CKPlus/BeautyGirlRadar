angular.module('bgradarApp.controllers', [])
  .controller('WallController', ['$scope', '$modal', 'BGlbs50',
  	 function($scope, $modal, BGlbs50) {
  	 	var init = function(){
  	 		$scope.selectedRecord = {}
  	 		var records = BGlbs50.list(function(data){
  	 			$scope.records = data.results;
  	 		});
		}
		init();

		$scope.showModal = function(selectedRecord){
			$('#myModal').modal();

			$scope.website = selectedRecord.fans_url;
			$scope.comment = selectedRecord.comment;

			$scope.selectedRecord = selectedRecord;
		}

		$scope.save = function(){
			

			var patchData = {
				"_id": $scope.selectedRecord.uid,
				"comment": $scope.comment || '',
  				"fans_url": $scope.website || ''
			}

			BGlbs50.updateData(patchData, function(){
				alert('感謝眾鄉民的工人智慧！');
				$('#myModal').modal('toggle');
				$scope.website = '';
				$scope.comment = '';
				init();
			});
		}



		
  	}])
  .controller('RadarController', ['$scope', 'BGlbs', '$timeout',
  	 function($scope, BGlbs, $timeout) {
  	 	google.maps.visualRefresh = true;
  	 	var markerToClose = null;
  	 	// var origCenter = {latitude: $scope.map.center.latitude, longitude: $scope.map.center.longitude};
  	 	var init = function(){
  	 		$scope.selectedRecord = {}
  	 		
  	 		BGlbs.list(function(data){
  	 			var markers = [];
  	 			
				_.each(data.results, function (marker) {
				  var obj = {
				  	id : marker.uid,
					latitude :marker.lat,
					longitude :marker.lng,
					title :'Test Record',
					showWindow :false,
					comment: marker.comment,
					fans_url: marker.fans_url,
					picurl: marker.picurl
				  }
				  
			      obj.closeClick = function () {
			        marker.showWindow = false;
			        $scope.$apply();
			      };
			      obj.onClicked = function () {
			        $scope.onMarkerClicked(obj);
			      };
			      markers.push(obj);
			      
			      
			    });
				$scope.map.dynamicMarkers = markers;
  	 		});

	    	$scope.map = {
			    center: {
			      latitude: 25.041762,
			      longitude: 121.549071
			    },
			    zoom: 15
			};

			// var dynamicMarkers = [
   //    {   id: 1,
   //      latitude: 46,
   //      longitude: -79
   //    },
   //    {
   //      id: 2,
   //      latitude: 33,
   //      longitude: -79
   //    },
   //    {
   //      id: 3,
   //      latitude: 35,
   //      longitude: -127
   //    }
   //  ];
   //  _.each(dynamicMarkers, function (marker) {
   //    marker.closeClick = function () {
   //      marker.showWindow = false;
   //      $scope.$apply();
   //    };
   //    marker.onClicked = function () {
   //      $scope.onMarkerClicked(marker);
   //    };
   //  });
    // $scope.map.dynamicMarkers = dynamicMarkers;

		}


		$scope.refreshMap = function () {
		    //optional param if you want to refresh you can pass null undefined or false or empty arg
		    $scope.map.control.refresh({latitude: 25.041762, longitude: 121.549071});
		    // $scope.map.control.getGMap().setZoom(11);
		};

		$scope.onMarkerClicked = function (marker) {
			//    if (markerToClose) {
			//      markerToClose.showWindow = false;
			//    }
			
			$scope.selectedRecord = marker;
			$('#myModal').modal();

			$scope.website = marker.fans_url;
			$scope.comment = marker.comment;

			// $scope.selectedRecord = selectedRecord;
			// markerToClose = marker; // for next go around
			// marker.showWindow = true;
			$scope.$apply();
		}

		$scope.save = function(){
			

			var patchData = {
				"_id": $scope.selectedRecord.id,
				"comment": $scope.comment || '',
  				"fans_url": $scope.website || ''
			}

			BGlbs.updateData(patchData, function(){
				alert('感謝眾鄉民的工人智慧！');
				$('#myModal').modal('toggle');
				$scope.website = '';
				$scope.comment = '';
				init();
			});
		}

		init();

		// var origCenter = {latitude: $scope.map.center.latitude, longitude: $scope.map.center.longitude};
  	}])