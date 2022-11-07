var exec = require("child_process").exec;

const runMatrixes = async (threadCount, path = "./hw_parallel") => {
  const array = [
    16, // 16x16
    32, // 32x32
    64, // 16x64
    128, // 128x128
    512, // 512x512
  ];
  const timeArray = [];
  let startTime = new Date();

  await array.map(async (matrix) => {
    const start = new Date();
    await exec(`${path} ${threadCount} ${matrix}`);
    const end = new Date();

    timeArray.push({ start, end });
  });

  console.log("FINISHED---------");

  timeArray.map((time, index) => {
    console.log(`Execution time for ${array[index]}x${array[index]} is ${time} seconds`);
  });
  console.log("-------------");
};

runMatrixes(2);
runMatrixes(4);
runMatrixes(16);
runMatrixes(32);
runMatrixes(64);
runMatrixes(128);
