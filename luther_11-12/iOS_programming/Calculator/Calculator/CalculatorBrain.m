//
//  CalculatorBrain.m
//  Calculator
//
//  Created by Scott Gerike on 2/9/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "CalculatorBrain.h"

@interface CalculatorBrain()
@property (nonatomic, strong) NSMutableArray *programStack;
@property (nonatomic, strong) NSMutableDictionary *variableValues;
@end

@implementation CalculatorBrain

@synthesize programStack = _programStack;
@synthesize variableValues = _variableValues;

- (NSMutableArray *)programStack {
    if (!_programStack) {
        _programStack = [[NSMutableArray alloc] init];
    }
    return _programStack;
}

- (NSMutableDictionary *)variableValues {
    if (!_variableValues) {
        _variableValues = [[NSMutableDictionary alloc] init];
        [_variableValues setObject:[NSNumber numberWithFloat:0.0] forKey:@"a"];
        [_variableValues setObject:[NSNumber numberWithFloat:0.0] forKey:@"b"];
        [_variableValues setObject:[NSNumber numberWithFloat:0.0] forKey:@"c"];
    }
    return _variableValues;
}

- (void)pushOperand:(double)operand {
    [self.programStack addObject:[NSNumber numberWithDouble:operand]];
}

- (void)pushStringOperand:(NSString *)operand {
    [self.programStack addObject:operand];
}

- (NSString *)popAndClearOperand {
    NSNumber *one = [NSNumber numberWithInt:1];
    NSNumber *two = [NSNumber numberWithInt:2];
    NSDictionary *operands;
    operands = [NSDictionary dictionaryWithObjectsAndKeys: one, @"cos", one, @"sin", one, @"√", two, @"+", two, @"-", two, @"*", two, @"/", nil];
    NSArray *operandsList = [operands allKeys];
    BOOL found = NO;
    NSString *topOfStack;
    while (found == NO) {
        id stackTop = [_programStack lastObject];
        if ([operandsList containsObject:stackTop]) {
            topOfStack = [_programStack lastObject];
        } else if ([_programStack count] == 0) {
            topOfStack = @"0";
            found = YES;
        } else {
            NSNumber *doubleVal = [_programStack lastObject];
            topOfStack = [doubleVal stringValue];
            found = YES;
        }
        if (topOfStack) [_programStack removeLastObject]; }
    return topOfStack;
}

- (void)clearOperands {
    [self.programStack removeAllObjects];
}

- (double)performOperation:(NSString *)operation {
    [self.programStack addObject:operation];
    return [CalculatorBrain runProgram:self.program usingVariableValues:self.variableValues];
}

- (void)pushVariableValues:(NSNumber *)a variable2:(NSNumber *)b variable3:(NSNumber *)c; {
    [_variableValues setObject:a forKey:@"a"];
    [_variableValues setObject:b forKey:@"b"];
    [_variableValues setObject:c forKey:@"c"];
}

- (id)program {
    return [self.programStack copy];
}

+ (NSString *)descriptionOfProgram:(id)program dict:(NSDictionary *)operatorDict {    
    if ([program count] == 0) {
        return nil;
    }
    id topOfStack = [program lastObject];
    if ([topOfStack isKindOfClass:[NSNumber class]]) {
        if (topOfStack) [program removeLastObject];
        return [topOfStack stringValue];
    }
    if ([topOfStack isEqualToString:(@"x")]) {
        NSString *variable = topOfStack;
        if (topOfStack) [program removeLastObject];
        return variable;
    }
    if ([[operatorDict objectForKey:topOfStack] intValue] == 2) { 
        if (topOfStack) [program removeLastObject];
        NSString *right = [self descriptionOfProgram:program dict:operatorDict];
        NSString *left = [self descriptionOfProgram:program dict:operatorDict];
        return [NSString stringWithFormat:@"(%@ %@ %@)",left, topOfStack, right]; }
        else if ([[operatorDict objectForKey:topOfStack] intValue] == 1) {
            if (topOfStack) [program removeLastObject];
            NSString *operand = [self descriptionOfProgram:program dict:operatorDict];
            return [NSString stringWithFormat:@"%@(%@)",topOfStack,operand];
        }
    return nil;
    }

- (NSString *)updateDescription {
    NSNumber *one = [NSNumber numberWithInt:1];
    NSNumber *two = [NSNumber numberWithInt:2];
    NSDictionary *operators;
    operators = [NSDictionary dictionaryWithObjectsAndKeys: one, @"cos", one, @"sin", one, @"√", two, @"+", two, @"-", two, @"*", two, @"/", nil];
    
    NSMutableArray *stack = [_programStack mutableCopy];
    NSString *complete = [[self class] descriptionOfProgram:stack dict:operators];
    while ([stack count] != 0) {
        NSString *second = [[self class] descriptionOfProgram:stack dict:operators];
        complete = [NSString stringWithFormat:@"%@, %@",complete, second];}
    return complete;
}

+ (double)popOperandOffStack:(NSMutableArray *)stack {
    double result = 0;
    
    id topOfStack = [stack lastObject];
    if (topOfStack) [stack removeLastObject];
    
    if ([topOfStack isKindOfClass:[NSNumber class]]) {
        result = [topOfStack doubleValue];
    }
    else if ([topOfStack isKindOfClass:[NSString class]]) {
        NSString *operation = topOfStack;
        if ([operation isEqualToString:@"+"]) {
            result = [self popOperandOffStack:stack] + [self popOperandOffStack:stack];
        } else if ([@"*" isEqualToString:operation]) {
            result = [self popOperandOffStack:stack] * [self popOperandOffStack:stack];
        } else if ([operation isEqualToString:@"-"]) {
            double subtrahend = [self popOperandOffStack:stack];
            result = [self popOperandOffStack:stack] - subtrahend;
        } else if ([operation isEqualToString:@"/"]) {
            double divisor = [self popOperandOffStack:stack];
            if (divisor) result = [self popOperandOffStack:stack] / divisor;
        } else if ([operation isEqualToString:@"√"]) {
            result = sqrt([self popOperandOffStack:stack]);
        } else if ([operation isEqualToString:@"sin"]) {
            result = sin([self popOperandOffStack:stack]);
        } else if ([operation isEqualToString:@"cos"]) {
            result = cos([self popOperandOffStack:stack]);
        } else if ([operation isEqualToString:@"π"]) {
            result = M_PI;
        }
    }
    return result;
}


+ (double)runProgram:(id)program usingVariableValues:(NSMutableDictionary *)variableValues; { //Not only push operands and operations, but you need to change runProgram to work with variables... Use a dictionary where the keys are variable names and the values are NSNumbers
    NSMutableArray *stack;
    NSArray *variableList = [variableValues allKeys];
    if ([program isKindOfClass:[NSArray class]]) {
        stack = [program mutableCopy];
        for (int i = 0; i<[stack count]; i++) {
            if ([variableList containsObject:[stack objectAtIndex:i]]) {
                [stack replaceObjectAtIndex:i withObject:[variableValues objectForKey:[stack objectAtIndex:i]]];
            }
            
        }
    }
    return [self popOperandOffStack:stack];
}


@end
