f =>
  btoa(
    [...btoa(f)]
      .map(s =>
        String.fromCharCode(
          s.charCodeAt(0) + 99
        )
      )
      .join("")
  );
