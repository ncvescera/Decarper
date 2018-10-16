PFont f;

void setup() {
  background(0);
  size(900, 300);
  f = createFont("Arial", 16, true);
}

void draw() {
  int[] values = get_data();

  int rect_x = 0;
  int rect_width = 15;

  for (int i = 0; i < values.length; i++) {
    int elem = values[i];

    if (elem == ' ') {
      elem = -100;
      fill(0, 204, 0);
    } else if (elem == '!') {
      elem = -height;
      fill(255, 0, 0);
    } else {
      fill(255);
      stroke(15);
      elem = -elem-100;
    }

    rect(rect_x, height, rect_width, elem);

    textFont(f, 10);
    text(char(values[i]), rect_x+5, height+elem-10);

    rect_x += rect_width;

    if (rect_x >= width) {
      rect_x = 0;
      background(0);
    }
  }
}

int[] get_data() {
  String[] lines = loadStrings("lettere.txt");
  int[] values = new int[lines.length];

  for (int i = 0; i < lines.length; i++)
    values[i] = int(lines[i].charAt(0));
  return values;
}
