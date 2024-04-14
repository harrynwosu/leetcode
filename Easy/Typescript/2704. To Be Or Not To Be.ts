type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
        toBe: (newVal: any) => {
            if (val === newVal) {
                return true;
            }
            throw new Error("Not Equal");
        },

        notToBe: (newVal: any) => {
            if (val !== newVal) {
                return true;
            }
            throw new Error("Equal");
        }
    }
    
};