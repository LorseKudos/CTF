document.addEventListener("DOMContentLoaded", (e) => {
  (() => {
    var d, b, h;
    const enc_image =
      "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";
    const expected_h = [
      0x2b47n,
      0x2ec76n,
      0x31e0f8n,
      0x34ffd37n,
      0x384feac4n,
      0x3bd4ea3c3n,
      0x3f9238ecb2n,
      0x438b5c7e540n,
      0x47c412466529n,
      0x4c40536acd1d6n,
      0x510458a17a1b46n,
      0x56149e2b91bfcc8n,
      0x5b75e80e4adbe365n,
      0x12d468f2f89a4375n,
      0x401af822823e94e2n,
      0x41ca7a4aa6280cc2n,
      0x5e721ef508a904f2n,
      0x45940e4593396e2fn,
      0x9ed4f29ec6d07adfn,
      0x8c241c8b33d8358en,
    ];
    function checkLocalStorage() {
      !localStorage.getItem("b") || !localStorage.getItem("h")
        ? (init(), setLocalStrage())
        : ((d = localStorage.getItem("d")),
          (b = BigInt(localStorage.getItem("b"))),
          (h = JSON.parse(localStorage.getItem("h")).map((arg) =>
            BigInt(arg)
          )));
    }
    function setLocalStrage() {
      localStorage.setItem("d", d),
        localStorage.setItem("b", b.toString()),
        localStorage.setItem(
          "h",
          JSON.stringify(h.map((arg) => arg.toString()))
        );
    }
    function init() {
      (d = ""), (b = 0x17n), (h = []);
    }
    function existsCategoryNameClass() {
      return (
        document.getElementsByClassName("category-name").length != 0x0
      );
    }
    function calcFromCategoryName() {
      let categoryName =
          document.getElementsByClassName("category-name")[0x0][
            "textContent"
          ],
        b =
          categoryName.charCodeAt(0x1) * categoryName.charCodeAt(0x6) -
          categoryName.charCodeAt(0x3),
        d = categoryName[0x1] + categoryName[0x6] + categoryName[0x3];
      return [b, d];
    }
    async function decrypto(enc_image, d) {
      const _d = new TextEncoder().encode(d),
        keyData = await crypto.subtle.digest("SHA-256", _d),
        string_iv = atob(enc_image).slice(0x0, 0xc),
        iv = new Uint8Array(
          Array.from(string_iv).map((arg) => arg.charCodeAt(0x0))
        ),
        algorithm = {
          name: "AES-GCM",
          iv: iv,
        },
        key = await crypto.subtle.importKey(
          "raw",
          keyData,
          algorithm,
          false,
          ["decrypt"]
        ),
        string_data = atob(enc_image).slice(0xc),
        data = new Uint8Array(
          Array.from(string_data).map((arg) => arg.charCodeAt(0x0))
        );
      try {
        const input = await crypto.subtle.decrypt(algorithm, key, data),
          image = new TextDecoder().decode(input);
        return image;
      } catch (e) {
        throw new Error("Decrypt failed");
      }
    }
    async function changeBackgroundImage() {
      const image = await decrypto(enc_image, d);
      document["body"]["style"]["backgroundImage"] = image;
    }
    function checkLengthOfH() {
      if (h["length"] == expected_h["length"])
        return changeBackgroundImage(), true;
      return false;
    }
    function main() {
      checkLocalStorage();
      if (checkLengthOfH()) return;
      if (!existsCategoryNameClass()) {
        init(), setLocalStrage();
        return;
      }
      let [_b, _d] = calcFromCategoryName();
      b *= 0x11n;
      b += BigInt(_b);
      b &= 0xffffffffffffffffn;
      d += _d;
      h.push(b);
      if (h["length"] == expected_h["length"])
        for (let idx = 0x0; idx < h["length"]; idx++) {
          if (h[idx] != expected_h[idx]) {
            init(), setLocalStrage();
            return;
          }
        }
      setLocalStrage(), checkLengthOfH();
    }
    main();
  })();
});
