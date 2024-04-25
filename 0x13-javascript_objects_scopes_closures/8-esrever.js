#!/usr/bin/node
exports.esrever = function (list) {
  const midPoint = Math.floor(list.length / 2);

  for (let i = 0; i < midPoint; i++) {
    const temp = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = temp;
  }

  return list;
};
