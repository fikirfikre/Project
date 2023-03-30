import 'dart:math';

Stream<int> randomNumbers() async* {
  final random = Random();

  for (var i = 0; i < 100; ++i) {
    await Future.delayed(Duration(seconds: 1));
    yield random.nextInt(50) + 1;
  }
}

void main() async {
  final stream = randomNumbers();
  await for (var value in stream) {
    print(value);
  }
}
