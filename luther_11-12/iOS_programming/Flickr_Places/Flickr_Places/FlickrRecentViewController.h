//
//  FlickrRecentViewController.h
//  Flickr_Places
//
//  Created by Scott Gerike on 4/23/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "FlickrPhotoView.h"

@interface FlickrRecentViewController : UITableViewController <PhotoData>

- (void)changeRecentEntries:(NSInteger)index;

@end
