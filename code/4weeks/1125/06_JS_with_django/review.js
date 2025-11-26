console.log('작업 1 시작');

const asyncTask = function (callBack) {
  let count = 0; // 경과 시간을 저장할 변수

  // 1초(1000ms) 간격으로 내부 로직을 반복 실행하는 setInterval 함수입니다.
  const timerId = setInterval(() => {
    count++; // 1초 증가
    console.log(count + '초...'); // 경과 시간 출력 (1초, 2초, 3초...)

    // 3초가 되면 타이머를 종료하고 원본 콜백을 실행합니다.
    if (count === 3) {
      clearInterval(timerId); // setInterval의 반복을 중단합니다.
      callBack('작업 완료');  // 최종 콜백 함수 호출
    }
  }, 1000);
};

asyncTask((result) => {
  // 3초 카운트가 끝난 뒤 실행됩니다.
  console.log(result);
});

console.log('작업 2 시작');