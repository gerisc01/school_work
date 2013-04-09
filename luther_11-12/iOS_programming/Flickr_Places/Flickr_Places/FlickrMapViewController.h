//
//  FlickrMapViewController.h
//  Flickr_Places
//
//  Created by Scott Gerike on 5/7/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <MapKit/MapKit.h>

@class FlickrMapViewController;

@protocol MapViewControllerDelegate <NSObject>

-(UIImage *)mapViewController:(FlickrMapViewController *)sender imageForAnnotation:(id <MKAnnotation>)annotation thumbnail:(BOOL)small;

@end


@interface FlickrMapViewController : UIViewController

@property (nonatomic, strong) NSArray *annotations; //of id <MKAnnotation>
@property (nonatomic, weak) id <MapViewControllerDelegate> delegate;
-(void)setMapRegion:(CLLocationCoordinate2D)locationCoordinate;

@end
