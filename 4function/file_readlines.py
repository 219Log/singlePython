with open("info.txt", "r", encoding="utf-8-sig") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(", ")
        if len(parts) != 3:
            continue

        name, weight_str, height_str = parts

        try:
            weight = int(weight_str)
            height = int(height_str)
        except ValueError:
            continue

        bmi = weight / (height / 100) ** 2
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print("\n".join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}",
        ]).format(name, weight, height, bmi, result))
        print()