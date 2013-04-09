//
//  FlickrRecentViewController.m
//  Flickr_Places
//
//  Created by Scott Gerike on 4/23/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "FlickrRecentViewController.h"
#import "FlickrFetcher.h"
#import "FlickrPhotoViewController.h"

@interface FlickrRecentViewController()
@property (nonatomic) NSInteger row;
@end


@implementation FlickrRecentViewController

@synthesize row = _row;

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
    NSArray *recentEntries = [[NSUserDefaults standardUserDefaults] arrayForKey:@"RecentEntries"];
    //NSDictionary *image = [recentEntries objectAtIndex:index];
    if ([segue.identifier isEqualToString:@"toRecentPhoto"]) {
        /*NSMutableArray *recentPhotos = [NSMutableArray arrayWithArray:recentEntries];
        if ([recentPhotos count]==20){
            [recentPhotos removeObjectAtIndex:19];
        }
        NSString *staticID = [[recentEntries objectAtIndex:index] objectForKey:@"id"];
        for (int x=0; x<[recentPhotos count]; x++) {
            NSString *photoID = [[recentPhotos objectAtIndex:x] objectForKey:@"id"];
            if ([photoID isEqualToString:staticID]) [recentPhotos removeObjectAtIndex:x];
        }
        [recentPhotos insertObject:[recentEntries objectAtIndex:index] atIndex:0];
        NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
        [[NSUserDefaults standardUserDefaults] setObject:recentPhotos forKey:@"RecentEntries"];
        [defaults synchronize];*/

        [self changeRecentEntries:index];
        [segue.destinationViewController setPhotoDataDelegate:self];
        [segue.destinationViewController setFlickrImage:[recentEntries objectAtIndex:index] title:photoTitle];
    }
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
    [self.tableView reloadData];
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

-(void)changeRecentEntries:(NSInteger)index
{
    NSArray *recentEntries = [[NSUserDefaults standardUserDefaults] arrayForKey:@"RecentEntries"];
    NSMutableArray *recentPhotos = [NSMutableArray arrayWithArray:recentEntries];
    if ([recentPhotos count]==20){
        [recentPhotos removeObjectAtIndex:19];
    }
    NSString *staticID = [[recentEntries objectAtIndex:index] objectForKey:@"id"];
    for (int x=0; x<[recentPhotos count]; x++) {
        NSString *photoID = [[recentPhotos objectAtIndex:x] objectForKey:@"id"];
        if ([photoID isEqualToString:staticID]) [recentPhotos removeObjectAtIndex:x];
    }
    [recentPhotos insertObject:[recentEntries objectAtIndex:index] atIndex:0];
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    [[NSUserDefaults standardUserDefaults] setObject:recentPhotos forKey:@"RecentEntries"];
    [defaults synchronize];
}

#pragma mark - Table view data source

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    // Return the number of sections.
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    NSArray *recentEntries = [[NSUserDefaults standardUserDefaults] arrayForKey:@"RecentEntries"];
    // Return the number of rows in the section.
    return [recentEntries count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *CellIdentifier = @"RecentPhotos";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
    }
    
    // Configure the cell...
    NSArray *recentEntries = [[NSUserDefaults standardUserDefaults] arrayForKey:@"RecentEntries"];
    NSDictionary *cellDict = [recentEntries objectAtIndex:indexPath.row];
    
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
    _row = indexPath.row;

    if (self.splitViewController) {
        UITableViewCell *cell = [self.tableView cellForRowAtIndexPath:indexPath];
        NSString *photoTitle = cell.textLabel.text;
        NSArray *recentEntries = [[NSUserDefaults standardUserDefaults] arrayForKey:@"RecentEntries"];
        FlickrPhotoViewController *pvc = [self.splitViewController.viewControllers lastObject];
        [pvc setPhotoDataDelegate:self];
        
        [self changeRecentEntries:_row];
        [pvc setFlickrImage:[recentEntries objectAtIndex:_row] title:photoTitle];
        [pvc drawPicture];}
}

-(NSURL *)getPhotoData
{
    NSArray *recentEntries = [[NSUserDefaults standardUserDefaults] arrayForKey:@"RecentEntries"];
    NSDictionary *photo = [recentEntries objectAtIndex:self.row];
    return [FlickrFetcher urlForPhoto:photo format:FlickrPhotoFormatLarge];
}

@end
