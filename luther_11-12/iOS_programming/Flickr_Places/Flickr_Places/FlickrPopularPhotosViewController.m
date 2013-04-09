//
//  FlickrPopularPhotosViewController.m
//  Flickr_Places
//
//  Created by Scott Gerike on 4/17/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "FlickrPhotoViewController.h"
#import "FlickrFetcher.h"
#import "FlickrMapView.h"
#import "FlickrMapViewController.h"
#import "FlickrPopularPhotosViewController.h"


@interface FlickrPopularPhotosViewController() <MapViewControllerDelegate>
@property (nonatomic, strong) NSDictionary *place;
@property (nonatomic) NSInteger rows;
@property (nonatomic) NSInteger currentRow;
@property (nonatomic, strong) NSArray *photosInPlace;
@property (nonatomic, strong) UIActivityIndicatorView *activityIndicator;
@property (nonatomic, strong) NSArray *mapAnnotations;
@end

@implementation FlickrPopularPhotosViewController

@synthesize place = _place;
@synthesize rows = _rows;
@synthesize currentRow = _currentRow;
@synthesize photosInPlace;
@synthesize activityIndicator = _activityIndicator;
@synthesize mapAnnotations = _mapAnnotations;

- (id)initWithStyle:(UITableViewStyle)style
{
    self = [super initWithStyle:style];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    NSInteger index = [self.tableView indexPathForCell:sender].row;
    UITableViewCell *cell = [self.tableView cellForRowAtIndexPath:[self.tableView indexPathForCell:sender]];
    NSString *photoTitle = cell.textLabel.text;
    if ([segue.identifier isEqualToString:@"goToPhoto"]) {
        [self changeRecentEntries:index];
        NSLog(@"Beginning of Segue");
        [segue.destinationViewController fromMap:NO];
        [segue.destinationViewController setPhotoDataDelegate:self];
        [segue.destinationViewController setFlickrImage:[self.photosInPlace objectAtIndex:index] title:photoTitle];
        NSLog(@"End of Segue");}
    
    if ([segue.identifier isEqualToString:@"photosToMap"]) {
        NSDictionary *aPlace = [self.photosInPlace objectAtIndex:0];
        CLLocationCoordinate2D coordinate;
        coordinate.latitude = [[aPlace objectForKey:@"latitude"] doubleValue];
        coordinate.longitude = [[aPlace objectForKey:@"longitude"] doubleValue];
        [segue.destinationViewController setDelegate:self];
        [segue.destinationViewController setMapRegion:coordinate];
        [segue.destinationViewController setAnnotations:self.mapAnnotations];
    }
}

- (NSArray *)mapAnnotations
{
    NSMutableArray *annotations = [NSMutableArray arrayWithCapacity:[self.photosInPlace count]];
    for (NSDictionary *photo in self.photosInPlace) {
        [annotations addObject:[FlickrMapView annotationForPhoto:photo]];
    }
    return annotations;
}

- (UIImage *)mapViewController:(FlickrMapViewController *)sender imageForAnnotation:(id<MKAnnotation>)annotation thumbnail:(BOOL)small
{
    FlickrMapView *fmv = (FlickrMapView *)annotation;
    if (small == YES){ 
        NSURL *url = [FlickrFetcher urlForPhoto:fmv.photo format:FlickrPhotoFormatSquare];
        NSData *data = [NSData dataWithContentsOfURL:url];
        return [UIImage imageWithData:data];}
    else {
        NSURL *url = [FlickrFetcher urlForPhoto:fmv.photo format:FlickrPhotoFormatLarge];
        NSData *data = [NSData dataWithContentsOfURL:url];
        return [UIImage imageWithData:data];}
}

- (void) setLocation:(NSDictionary *)location 
{
    _place = location;
    _rows = [[location objectForKey:@"photo_count"] intValue];
}

-(void) setPhotos:(NSArray *)photos
{
    self.photosInPlace = photos;
    if (self.tableView.window) [self.tableView reloadData];
}

-(void) startActivityIndicator
{
    _activityIndicator = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle: UIActivityIndicatorViewStyleGray];
    _activityIndicator.center = self.tableView.center;
    [_activityIndicator startAnimating];
    [self.tableView addSubview:_activityIndicator];
}

-(void) stopActivityIndicator
{
    [_activityIndicator stopAnimating];
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark - View lifecycle

- (void)viewDidLoad
{
    [super viewDidLoad];
    self.mapAnnotations = [self mapAnnotations];
    // Uncomment the following line to preserve selection between presentations.
    // self.clearsSelectionOnViewWillAppear = NO;
 
    // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
    // self.navigationItem.rightBarButtonItem = self.editButtonItem;
}

- (void)viewDidUnload
{
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (void)viewWillAppear:(BOOL)animated
{
    [super viewWillAppear:animated];
}

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];
}

- (void)viewWillDisappear:(BOOL)animated
{
    [super viewWillDisappear:animated];
}

- (void)viewDidDisappear:(BOOL)animated
{
    [super viewDidDisappear:animated];
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations
    return YES;
}

#pragma mark - Table view data source

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [self.photosInPlace count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = @"LocationPhotos";
    
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
    }
    
    // Configure the cell...
    NSDictionary *cellDict = [self.photosInPlace objectAtIndex:indexPath.row];
    NSString *title = [cellDict objectForKey:@"title"];
    NSDictionary *desDict = [cellDict objectForKey:@"description"];
    NSString *description = [desDict objectForKey:@"_content"];
    if ([title isEqualToString:@""]){
        if ([description isEqualToString:@""]){
            title = @"Unknown";
        }
        else {
            title = description;
        }
    }
    cell.textLabel.text = title;
    cell.detailTextLabel.text = description;
    
    return cell;
}

-(void)changeRecentEntries:(NSInteger)index
{
    NSArray *recentEntries = [[NSUserDefaults standardUserDefaults] arrayForKey:@"RecentEntries"];
    if (recentEntries == nil) {
        NSMutableArray *photoArray = [[NSMutableArray alloc] init];
        [photoArray addObject:[self.photosInPlace objectAtIndex:index]];
        NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
        [[NSUserDefaults standardUserDefaults] setObject:photoArray forKey:@"RecentEntries"];
        [defaults synchronize];
    } else {
        NSMutableArray *recentPhotos = [NSMutableArray arrayWithArray:recentEntries];
        if ([recentPhotos count]==20){
            [recentPhotos removeObjectAtIndex:19];
        }
        NSString *staticID = [[self.photosInPlace objectAtIndex:index] objectForKey:@"id"];
        for (int x=0; x<[recentPhotos count]; x++) {
            NSString *photoID = [[recentPhotos objectAtIndex:x] objectForKey:@"id"];
            if ([photoID isEqualToString:staticID]) [recentPhotos removeObjectAtIndex:x];
        }
        [recentPhotos insertObject:[self.photosInPlace objectAtIndex:index] atIndex:0];
        NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
        [[NSUserDefaults standardUserDefaults] setObject:recentPhotos forKey:@"RecentEntries"];
        [defaults synchronize];
    }
}

/*
// Override to support conditional editing of the table view.
- (BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Return NO if you do not want the specified item to be editable.
    return YES;
}
*/

/*
// Override to support editing the table view.
- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath
{
    if (editingStyle == UITableViewCellEditingStyleDelete) {
        // Delete the row from the data source
        [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath] withRowAnimation:UITableViewRowAnimationFade];
    }   
    else if (editingStyle == UITableViewCellEditingStyleInsert) {
        // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
    }   
}
*/

/*
// Override to support rearranging the table view.
- (void)tableView:(UITableView *)tableView moveRowAtIndexPath:(NSIndexPath *)fromIndexPath toIndexPath:(NSIndexPath *)toIndexPath
{
}
*/

/*
// Override to support conditional rearranging of the table view.
- (BOOL)tableView:(UITableView *)tableView canMoveRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Return NO if you do not want the item to be re-orderable.
    return YES;
}
*/

#pragma mark - Table view delegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    _currentRow = indexPath.row;
    if (self.splitViewController) {
        UITableViewCell *cell = [self.tableView cellForRowAtIndexPath:indexPath];
        NSString *photoTitle = cell.textLabel.text;
        FlickrPhotoViewController *pvc = [self.splitViewController.viewControllers lastObject];
        
        [self changeRecentEntries:_currentRow];
        [pvc setPhotoDataDelegate:self];
        [pvc setFlickrImage:[self.photosInPlace objectAtIndex:_currentRow] title:photoTitle];
        [pvc drawPicture];
        
        /*dispatch_queue_t splitviewQueue = dispatch_queue_create("flickr downloader", NULL);
        dispatch_async(splitviewQueue, ^{
            [pvc setPhotoDataDelegate:self];
            dispatch_async(dispatch_get_main_queue(), ^{
                [pvc setPhotoDataDelegate:self];
                [pvc setFlickrImage:[self.photosInPlace objectAtIndex:_currentRow] title:photoTitle];
                [pvc drawPicture];});
             });
    dispatch_release(splitviewQueue);*/
    }
}


-(NSURL *)getPhotoData
{
    NSDictionary *photo = [self.photosInPlace objectAtIndex:self.currentRow];
    return [FlickrFetcher urlForPhoto:photo format:FlickrPhotoFormatLarge];
}

@end
