var x, y
var dn = Date.now

var rc = function() {
    return Math.floor(107 + 19 * Math.random()) // 107〜125 乱数
}

var rn = new Math.seedrandom("0x42").int32() // -490046641

// rの数だけ文字生成
var rt = function() {
    let r = Math.floor(1 + 7 * Math.random()) // 1〜7 乱数
      , e = [];
    for (; r > 0; )
        e.push(rc()),
        r--;
    return String.fromCharCode(...e)
}

// r回右にシフト
var rr = function(r, e) {
    for (; r > 0; )
        e.unshift(e.pop()),
        --r;
    return e.join("")
}

// r回左にシフト
var lr = function(r, e) {
    for (; r > 0; )
        e.push(e.shift()),
        --r;
    return e.join("")
}


var cf = function(r) {
    try {
        let e = Array.from(atob(rr(243, Array.from(r)))), // lr(243, Array.from(btoa("flag")))
          n = 1;
        for (let r = 0; r < e.length; r++)
            r === n && (e.splice(r + 1, +e[r + 1] + 1),
            n += n);
        return +lr(168, e)
    } catch (r) {}
    return -1
}


var c = function() {
    let r = document.getElementById("message").value
      , e = document.getElementById("msg");
    x = rn % 2 == 0 ? lr : rr,
    y = rn % 2 != 0 ? lr : rr,
    cf(r) >= dn() - 6e4 ? fetch("/check", {
        method: "POST",
        mode: "same-origin",
        cache: "no-cache",
        headers: {
            "Content-Type": "application/json"
        },
        referrer: "no-refferer",
        body: JSON.stringify({
            key: r
        })
    }).then(r=>r.json()).then(r=>{
        r.hasOwnProperty("flag") ? e.innerHTML = "Congrats! <br/>" + r.flag : e.innerText = "Nope!!!"
    }
    ).catch(r=>{
        console.error(r)
    }
    ) : e.innerText = "Nope!!!"
};


lr(243, Array.from(btoa("11111111111111111110000")));
