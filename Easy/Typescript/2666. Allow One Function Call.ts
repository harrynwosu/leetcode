/*
Implement a closure that has access to an external boolean flag variable which indicates whether the function has been called or not
If not, return the input function.
*/
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
    let used: boolean = false;

    return function (...args) {
        if (!used) {
            used = true;
            return fn(...args);
        }
    };
}