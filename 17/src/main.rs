use regex::Regex;
use std::fs;

fn parse() -> (i64, i64, i64, Vec<i64>) {
    let content = fs::read_to_string("input.txt").expect("not found");

    let re = Regex::new(
        r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n+Program: (\d(?:,\d+)*)",
    )
    .unwrap();
    let Some(caps) = re.captures(&content) else {
        return (0, 0, 0, vec![]);
    };
    let a = caps[1].parse().unwrap();
    let b = caps[2].parse().unwrap();
    let c = caps[3].parse().unwrap();

    let instructions = caps[4]
        .split(",")
        .map(|s| s.parse::<i64>().unwrap())
        .collect();

    return (a, b, c, instructions);
}

fn process_instructions(
    mut a: i64,
    mut b: i64,
    mut c: i64,
    instructions: Vec<i64>,
) -> (i64, i64, i64, Vec<i64>) {
    let mut i: usize = 0;
    let mut output: Vec<i64> = Vec::new();

    while i < instructions.len() {
        let instruction = instructions[i];
        let literal = instructions[i + 1];
        let combo;
        match literal {
            4 => combo = a,
            5 => combo = b,
            6 => combo = c,
            _ => combo = literal,
        }
        let mut goto: Option<i64> = None;

        match instruction {
            0 => a = a / 2_i64.pow(combo.try_into().unwrap()),
            1 => b ^= literal,
            2 => b = combo % 8,
            3 => {
                if a != 0 {
                    goto = Some(literal)
                }
            }
            4 => b ^= c,
            5 => output.push(combo % 8),
            6 => b = a / 2_i64.pow(combo.try_into().unwrap()),
            7 => c = a / 2_i64.pow(combo.try_into().unwrap()),
            _ => println!(""),
        }
        if let Some(value) = goto {
            i = value.try_into().unwrap();
        } else {
            i += 2
        }
    }

    return (a, b, c, output);
}

fn main() {
    let (mut a, b, c, instructions) = parse();


    // Part 1
    let (_, _, _, output) = process_instructions(a, b, c, instructions.clone());

    let string_vector: Vec<String> = output.iter().map(|v| v.to_string()).collect();
    let part_1_answer = string_vector.join(",");

    println!("Part 1: {part_1_answer}");

    // Part 2
    a = 1;

    let (_, _, _, mut output) = process_instructions(a, b, c, instructions.clone());

    while instructions != output {
        if instructions.len() > output.len() {
            a *= 8;
        } else {
            for index in (0..instructions.len()).rev() {
                if instructions[index] != output[index] {
                    a += 8_i64.pow(index.try_into().unwrap());
                    break;
                }
            }
        }

        (_, _, _, output) = process_instructions(a, b, c, instructions.clone());
    }
    println!("Part 2: {a}")
}
