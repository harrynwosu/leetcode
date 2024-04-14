class ArrayWrapper {
    nums: number[];
    constructor(nums: number[]) {
        this.nums = nums;
    }
    
    valueOf(): number {
       return this.nums.reduce((acc, curr) => acc + curr, 0); 
    }
    
    toString(): string {
        return `[${this.nums.join(",")}]`;
    }
};