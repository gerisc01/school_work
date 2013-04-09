//
//  FlickrPopularPhotosViewController.h
//  Flickr_Places
//
//  Created by Scott Gerike on 4/17/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "FlickrPhotoView.h"

@interface FlickrPopularPhotosViewController : UITableViewController <PhotoData>

- (void) setLocation:(NSDictionary *)location;
- (void) setPhotos:(NSArray *)photos;
- (void)changeRecentEntries:(NSInteger)index;
- (void) startActivityIndicator;
- (void) stopActivityIndicator;

@end
