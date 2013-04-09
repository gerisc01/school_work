//
//  FlickrPhotoViewController.m
//  Flickr_Places
//
//  Created by Scott Gerike on 4/18/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "FlickrPhotoViewController.h"
#import "FlickrFetcher.h"

@interface FlickrPhotoViewController() <UIScrollViewDelegate>
@property (weak, nonatomic) IBOutlet UIScrollView *scrollView;
@property (weak, nonatomic) IBOutlet FlickrPhotoView *imageView;
@property (weak, nonatomic) IBOutlet UINavigationItem *navBar;
@property (weak, nonatomic) NSDictionary *imageDict;
@property (nonatomic) BOOL isFromMap;
@property (weak, nonatomic) NSString *photoTitle;
@property (strong, nonatomic) UIImage *image;
@property (weak, nonatomic) IBOutlet UIToolbar *myToolbar;
@property (strong, nonatomic) IBOutlet UIActivityIndicatorView *activityIndicator;
@end

@implementation FlickrPhotoViewController
@synthesize activityIndicator = _activityIndicator;
@synthesize photoView;
@synthesize scrollView;
@synthesize imageView;
@synthesize navBar;
@synthesize photoDataDelegate = _photoDataDelegate;
@synthesize imageDict = _imageDict;
@synthesize photoTitle = _photoTitle;
@synthesize image = _image;
@synthesize myToolbar;
@synthesize isFromMap = _isFromMap;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void) awakeFromNib {
    [super awakeFromNib];
    self.splitViewController.delegate = self;
}

-(void)setPhotoDataDelegate:(FlickrPopularPhotosViewController *)photoDataDelegate{
    _photoDataDelegate = photoDataDelegate;
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc that aren't in use.
}

- (UIView *)viewForZoomingInScrollView:(UIScrollView *)scrollView
{
    return self.photoView;
}

- (void) setFlickrImage:(NSDictionary *)dict title:(NSString *)photoTitle
{
    _imageDict = dict;
    _photoTitle = photoTitle;
}

/*-(void) startActivityIndicator
{
    _activityIndicator = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle: UIActivityIndicatorViewStyleWhiteLarge];
    _activityIndicator.center = self.topImageView.center;
    NSLog(@"%@",self.activityIndicator);
    [_activityIndicator startAnimating];
    [self.topImageView addSubview:_activityIndicator];
}

-(void) stopActivityIndicator
{
    [_activityIndicator stopAnimating];
}*/

#pragma mark - View lifecycle

/*
// Implement loadView to create a view hierarchy programmatically, without using a nib.
- (void)loadView
{
}
*/


- (void)viewDidLoad
{
    [super viewDidLoad];
    if (_isFromMap == NO){
        [self drawPicture];
    }
    else {
        [self drawPictureFromMap];
    }
    
    //[_activityIndicator startAnimating];
    //NSLog(@"%@",self.activityIndicator);
}

-(void)setZoomScale
{
    UIDeviceOrientation orientation = [[UIDevice currentDevice] orientation];
    NSLog(@"%f, %f",self.scrollView.contentSize.width,self.scrollView.contentSize.height);
    if (orientation == UIDeviceOrientationLandscapeLeft || orientation == UIDeviceOrientationLandscapeRight){
        if (self.scrollView.contentSize.width <= self.scrollView.contentSize.height){
            scrollView.zoomScale = self.scrollView.bounds.size.height/self.scrollView.contentSize.width;
        }
        else {
            scrollView.zoomScale = self.scrollView.bounds.size.width/self.scrollView.contentSize.height;
        }

    }
    else {
        if (self.scrollView.contentSize.width <= self.scrollView.contentSize.height){
            scrollView.zoomScale = self.scrollView.bounds.size.height/self.scrollView.contentSize.width;
        }
        else {
            scrollView.zoomScale = self.scrollView.bounds.size.width/self.scrollView.contentSize.height;
        }
    }
}

-(void)fromMap:(BOOL)map
{
    self.isFromMap = map;
}

- (void)drawPicture
{
    [self.activityIndicator startAnimating];
    dispatch_queue_t downloadQueue = dispatch_queue_create("flickr downloader", NULL);
    dispatch_async(downloadQueue, ^{
        navBar.title = _photoTitle;
        self.photoView.photoDataDelegate = _photoDataDelegate;
        self.scrollView.delegate = self;
        NSURL *url = [FlickrFetcher urlForPhoto:_imageDict format:2];
        UIImage *image = [UIImage imageWithData:[NSData dataWithContentsOfURL:url]];
        self.scrollView.contentSize = image.size;
        self.photoView.frame = CGRectMake(0, 0, image.size.width, image.size.height);
        dispatch_async(dispatch_get_main_queue(), ^{
            [self setZoomScale];
            [self.imageView setImage:image];
            [_activityIndicator stopAnimating];});
    });
    dispatch_release(downloadQueue);
}

- (void)setPictureFromMap:(UIImage *)picture title:(NSString *)photoTitle
{
    self.image = picture;
    self.photoTitle = photoTitle;
}
         
-(void)drawPictureFromMap
{
    [self.activityIndicator startAnimating];
    dispatch_queue_t downloadQueue = dispatch_queue_create("flickr downloader", NULL);
    dispatch_async(downloadQueue, ^{
        navBar.title = self.photoTitle;
        self.photoView.photoDataDelegate = _photoDataDelegate;
        self.scrollView.delegate = self;
        UIImage *image = self.image;
        self.scrollView.contentSize = image.size;
        dispatch_async(dispatch_get_main_queue(), ^{
            self.photoView.frame = CGRectMake(0, 0, image.size.width, image.size.height);
            [self setZoomScale];
            [self.imageView setImage:image];
            [self.activityIndicator stopAnimating];});
    });
    dispatch_release(downloadQueue);
}


- (void)viewDidUnload
{
    [self setScrollView:nil];
    [self setPhotoView:nil];
    [self setImageView:nil];
    [self setNavBar:nil];
    [self setMyToolbar:nil];
    [self setActivityIndicator:nil];
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations
    //return (interfaceOrientation == UIInterfaceOrientationPortrait);
    return YES;
}

- (void) setSplitViewBarButtonItem:(UIBarButtonItem *)splitViewBarButtonItem
{
    NSMutableArray *toolbarItems = [self.myToolbar.items mutableCopy];
    if (splitViewBarButtonItem) [toolbarItems insertObject:splitViewBarButtonItem atIndex:0];
    self.myToolbar.items = toolbarItems;
}

- (void) removeSplitViewBarButtonItem:(UIBarButtonItem *)splitViewBarButtonItem
{
    NSMutableArray *toolbarItems = [self.myToolbar.items mutableCopy];
    
    [toolbarItems removeObject:splitViewBarButtonItem];
    self.myToolbar.items = toolbarItems;
}

-(BOOL) splitViewController:(UISplitViewController *)svc shouldHideViewController:(UIViewController *)vc inOrientation:(UIInterfaceOrientation)orientation {
    return UIInterfaceOrientationIsPortrait(orientation);
}

-(void)splitViewController:(UISplitViewController *)svc willHideViewController:(UIViewController *)aViewController withBarButtonItem:(UIBarButtonItem *)barButtonItem forPopoverController:(UIPopoverController *)pc
{    
    barButtonItem.title = @"Photos";
    //tell detail view controlle rto put this button up
    
    [self setSplitViewBarButtonItem:barButtonItem];
}

-(void)splitViewController:(UISplitViewController *)svc willShowViewController:(UIViewController *)aViewController invalidatingBarButtonItem:(UIBarButtonItem *)barButtonItem
{
    [self removeSplitViewBarButtonItem:barButtonItem];
}

@end
