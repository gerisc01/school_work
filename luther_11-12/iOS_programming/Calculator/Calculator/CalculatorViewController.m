//
//  CalculatorViewController.m
//  Calculator
//
//  Created by Scott Gerike on 2/7/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "CalculatorViewController.h"
#import "CalculatorBrain.h"
#import "GraphingViewController.h"

@interface CalculatorViewController()
@property (nonatomic) BOOL userIsInTheMiddleOfEnteringANumber;
@property (nonatomic) BOOL userHasPressedADecimal;
@property (nonatomic) BOOL variableOnScreen;
@property (nonatomic) BOOL negativeEnabled;
@property (nonatomic, strong) CalculatorBrain *brain;
@property (nonatomic, strong) NSMutableDictionary *variables;
@end

@implementation CalculatorViewController
@synthesize display;
@synthesize recentEntries;
@synthesize userIsInTheMiddleOfEnteringANumber;
@synthesize negativeEnabled;
@synthesize variableOnScreen;
@synthesize userHasPressedADecimal = _userHasPressedADecimal;
@synthesize brain = _brain;
@synthesize variables = _variables;

-(CalculatorBrain *)brain {
    if (!_brain) _brain = [[CalculatorBrain alloc] init];
    return _brain;
}

- (NSMutableDictionary *)variables {
    if (!_variables) {
        _variables = [[NSMutableDictionary alloc] init];
    }
    return _variables;
}
- (IBAction)doGraph:(id)sender {
    GraphingViewController *gvc = [self.splitViewController.viewControllers lastObject];
    [gvc setGraphDataDelegate:self];
    [gvc graphIt];
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqualToString:@"graphing"]) {
        [segue.destinationViewController setGraphDataDelegate:self];
        [segue.destinationViewController setProgramLabel:self.recentEntries.text];
    }
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation {
    return YES;
}

- (IBAction)digitPressed:(UIButton *)sender {
    NSString *digit = [sender currentTitle];
    if (self.userIsInTheMiddleOfEnteringANumber) {
        self.display.text = [self.display.text stringByAppendingString:digit];
    }
    else {
        self.display.text = digit;
        self.userIsInTheMiddleOfEnteringANumber = YES;
    }
}
- (IBAction)enterPressed {
    if (variableOnScreen) {
        [self.brain pushStringOperand:self.display.text];
    } else {
        [self.brain pushOperand:[self.display.text doubleValue]];
    }
    self.recentEntries.text = [self.brain updateDescription];
    self.userIsInTheMiddleOfEnteringANumber = NO;
    self.userHasPressedADecimal = NO;
    self.negativeEnabled = NO;
}

- (IBAction)decimalPressed {
    if (!self.userHasPressedADecimal) {
        self.display.text = [self.display.text stringByAppendingString:@"."];
        self.userIsInTheMiddleOfEnteringANumber = YES;
        self.userHasPressedADecimal = YES;
    }
}

- (IBAction)operationPressed:(UIButton *)sender {
    if (self.userIsInTheMiddleOfEnteringANumber) {
        [self enterPressed];
    }
    NSString *operation = [sender currentTitle];
    double result = [self.brain performOperation:operation];
    self.display.text = [NSString stringWithFormat:@"%g", result];
    self.recentEntries.text = [self.brain updateDescription];
}

- (IBAction)negativePressed {
    if (self.negativeEnabled == NO) {
        NSString *negative = @"-";
        negative = [negative stringByAppendingString:self.display.text];
        self.display.text = negative;
        self.negativeEnabled = YES;
    } else { 
        self.display.text = [self.display.text substringFromIndex:1];
        self.negativeEnabled = NO;
    }
}

- (IBAction)clearPressed {
    [self.brain clearOperands];
    self.display.text = @"0";
    self.recentEntries.text = @"";
    self.userIsInTheMiddleOfEnteringANumber = NO;
    self.userHasPressedADecimal = NO;
    self.negativeEnabled = NO;
    self.variableOnScreen = NO;
}
- (IBAction)undoPressed {
    NSString *newDisplay = [self.display.text substringToIndex:[self.display.text length]-1];
    if (self.userIsInTheMiddleOfEnteringANumber == NO || [self.display.text isEqualToString:@"0"]) {
        self.display.text = [self.brain popAndClearOperand];
        self.recentEntries.text = [self.brain updateDescription];
    } else if ([self.display.text length] == 1) {
        self.display.text = @"0";
        self.userIsInTheMiddleOfEnteringANumber = NO;
    } else if ([self.display.text length] == 2 && self.negativeEnabled == YES) {
        self.display.text = @"0";
        self.userIsInTheMiddleOfEnteringANumber = NO;
    } else {
        self.display.text = newDisplay;
    }
}
- (IBAction)variablePressed:(id)sender {
    NSString *variable = [sender currentTitle];
    if (!self.userIsInTheMiddleOfEnteringANumber) {
        self.display.text = variable;
        self.variableOnScreen = YES;
    }
}

- (void)viewDidUnload {
    [self setRecentEntries:nil];
    [super viewDidUnload];
}

- (double)getValueForXCoordinate:(float)x
{
    [self.variables setValue:[NSNumber numberWithDouble:x] forKey:@"x"];
    return [CalculatorBrain runProgram:self.brain.program usingVariableValues:self.variables];
}

@end
