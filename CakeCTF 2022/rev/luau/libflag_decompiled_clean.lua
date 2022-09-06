function checkFlag(flag, key)
  xored = {62, 85, 25, 84, 47, 56, 118, 71, 109, 0, 90, 71, 115, 9, 30, 58, 32, 101, 40, 20, 66, 111, 3, 92, 119, 22, 90, 11, 119, 35, 61, 102, 102, 115, 87, 89, 34, 34} -- 38個

  -- 入力値とxoredの長さ(=38)が同じかチェック
  L3_2 = #flag
  L4_2 = #xored
  if L3_2 ~= L4_2 then
    L3_2 = false
    return L3_2
  end

  flag_enc = {}
  key_enc = {}

  -- 1文字ずつアスキー値に変換する
  for idx = 1, #flag do
    L10_2 = flag.sub(flag, idx, idx + 1)
    L9_2 = string.byte(L10_2)
    flag_enc[idx] = L9_2
  end

  -- 1文字ずつアスキー値に変換する
  for idx = 1, #key do
    L10_2 = key.sub(key, idx, idx+1)
    L9_2 = string.byte(L10_2)
    key_enc[idx] = L9_2
  end

  -- flag_encをreverseする
  for i = 1, #flag_enc, 1 do
    for j = i + 1, #flag_enc, 1 do
      L13_2 = flag_enc[i]
      L14_2 = flag_enc[j]
      flag_enc[i] = L14_2
      flag_enc[j] = L13_2
    end
  end

  -- flag_encとkeyをxorした結果がxoredと等しいかチェック
  for idx = 1, #flag_enc, 1 do
    L10_2 = (idx - 1) % #key_enc
    L10_2 = 1 + L10_2
    flag_enc[idx] = flag_enc[idx] ~ key_enc[L10_2]
    if flag_enc[idx] ~= xored[idx] then
      L9_2 = false
      return L9_2
    end
  end
  L5_2 = true
  return L5_2
end

lib = {}
lib.checkFlag = checkFlag
return lib
