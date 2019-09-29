function(p, a, c, k, e, r) {
    e = function(c) {
        return c.toString(a)
    };
    if (!''.replace(/^/, String)) {
        while (c--) r[e(c)] = k[c] || e(c);
        k = [function(e) {
            return r[e]
        }];
        e = function() {
            return '\\w+'
        };
        c = 1
    };
    while (c--) if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
    return p
} ('0 1="2";0 3="4";0 5="6";0 7="8";0 9="a";', 11, 11, 'var|dynamicurl|/WZWSREL2dvdXRvbmdqaWFvbGl1LzExMzQ1Ni8xMTM0NjkvMTEwNDAvaW5kZXgxLmh0bWw=|wzwsquestion|lO;D=#My]gEXCm_np2dT|wzwsfactor|3674|wzwsmethod|WZWS_METHOD|wzwsparams|WZWS_PARAMS'.split('|'), 0, {}));