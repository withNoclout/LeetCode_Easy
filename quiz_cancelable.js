/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
function cancellable(fn, args, t) {
    const timeoutId = setTimeout(() => fn(...args), t);
    return function cancelFn() {
        clearTimeout(timeoutId);
    };
}
