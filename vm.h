#include "instruction.h"
#ifndef VM_H_
#define VM_H_

// Number of cells in a Segment
#define MEMORY_SEGMENT_SIZE 256
// Number of segments
#define MEMORY_SEGMENT_COUNT 256
// 256*256 = 357604 Total memory cells

#define REGISTER_COUNT 16

typedef struct
{
    int regs[REGISTER_COUNT]; // General purpose registers
    // Memory is indexed by segment and then cell
    int memory[MEMORY_SEGMENT_COUNT][MEMORY_SEGMENT_SIZE];
    int* pc; // Program counter / instruction pointer
    int* code; // List of instructions
} VM;

VM* createVM(int* code);

void run(VM* vm);

Instruction* decode(int* instr);

void exec(VM* vm, Instruction* instr);

#endif
