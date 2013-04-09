//
//  FlickrPhotoViewController.h
//  Flickr_Places
//
//  Created by Scott Gerike on 4/18/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "FlickrPhotoView.h"
#import "FlickrPopularPhotosViewController.h"

@interface FlickrPhotoViewController : UIViewController <UISplitViewControllerDelegate>

- (void) setFlickrImage:(NSDictionary *)image title:(NSString *)photoTitle;
- (void)setPictureFromMap:(UIImage *)picture title:(NSString *)photoTitle;
- (void)fromMap:(BOOL)map;
- (void)drawPicture;
- (void)drawPictureFromMap;
@property (weak, nonatomic) IBOutlet FlickrPhotoView *photoView;
@property (weak, nonatomic) IBOutlet FlickrPopularPhotosViewController *photoDataDelegate;
@end
