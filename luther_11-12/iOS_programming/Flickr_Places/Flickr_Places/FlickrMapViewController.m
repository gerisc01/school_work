//
//  FlickrMapViewController.m
//  Flickr_Places
//
//  Created by Scott Gerike on 5/7/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "FlickrMapViewController.h"
#import "FlickrPhotoViewController.h"
#import <MapKit/MapKit.h>

@interface FlickrMapViewController() <MKMapViewDelegate>
@property (weak, nonatomic) IBOutlet MKMapView *mapView;
@property (nonatomic) CLLocationCoordinate2D coordinateRegion;
@property (nonatomic, weak) NSString *nextPhotoTitle;
@property (nonatomic, weak) UIImage *nextImage;
@end

@implementation FlickrMapViewController

@synthesize mapView = _mapView;
@synthesize annotations = _annotations;
@synthesize coordinateRegion = _coordinateRegion;
@synthesize delegate = _delegate;
@synthesize nextPhotoTitle = _nextPhotoTitle;
@synthesize nextImage = _nextImage;

-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"mapToPhoto"]){
        [segue.destinationViewController fromMap:YES];
        [segue.destinationViewController setPictureFromMap:_nextImage title:_nextPhotoTitle];
    }
}

-(void)updateMapView
{
    if (self.mapView.annotations) [self.mapView removeAnnotations:self.mapView.annotations];
    if (self.annotations) [self.mapView addAnnotations:self.annotations];
    if (self.mapView) {
        MKCoordinateRegion coord = MKCoordinateRegionMake(_coordinateRegion, MKCoordinateSpanMake(.3, .3));
        [self.mapView setRegion:coord];
    }
}

-(void)setMapView:(MKMapView *)mapView
{
    _mapView = mapView;
    [self updateMapView];
}

-(void)setMapRegion:(CLLocationCoordinate2D)locationCoordinate
{
    _coordinateRegion = locationCoordinate;
}

-(void)viewDidLoad
{
    [super viewDidLoad];
    self.mapView.delegate = self;
}

-(void)setDelegate:(id<MapViewControllerDelegate>)delegate
{
    _delegate = delegate;
}

- (MKAnnotationView *)mapView:(MKMapView *)mapView viewForAnnotation:(id<MKAnnotation>)annotation
{
    MKAnnotationView *aView = [mapView dequeueReusableAnnotationViewWithIdentifier:@"MapVC"];
    if (!aView) {
        aView = [[MKPinAnnotationView alloc] initWithAnnotation:annotation reuseIdentifier:@"MapVC"];
        aView.canShowCallout = YES;
        aView.leftCalloutAccessoryView = [[UIImageView alloc] initWithFrame:CGRectMake(0, 0, 30, 30)];
        aView.rightCalloutAccessoryView = [UIButton buttonWithType:UIButtonTypeDetailDisclosure];
    }
    aView.annotation = annotation;
    [(UIImageView *)aView.leftCalloutAccessoryView setImage:nil];
    return aView;
}

-(void)mapView:(MKMapView *)mapView didSelectAnnotationView:(MKAnnotationView *)view
{
    UIImage *image = [self.delegate mapViewController:self imageForAnnotation:view.annotation thumbnail:YES];
    [(UIImageView *)view.leftCalloutAccessoryView setImage:image];
}

-(void)mapView:(MKMapView *)mapView annotationView:(MKAnnotationView *)view calloutAccessoryControlTapped:(UIControl *)control
{
    _nextPhotoTitle = view.annotation.title;
    _nextImage = [self.delegate mapViewController:self imageForAnnotation:view.annotation thumbnail:NO];
    [self performSegueWithIdentifier:@"mapToPhoto" sender:self];
}

-(void)setAnnotations:(NSArray *)annotations
{
    _annotations = annotations;
    [self updateMapView];
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark - View lifecycle

/*
// Implement loadView to create a view hierarchy programmatically, without using a nib.
- (void)loadView
{
}
*/

/*
// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad
{
    [super viewDidLoad];
}
*/

- (void)viewDidUnload
{
    [self setMapView:nil];
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations
    return YES;
}

@end
