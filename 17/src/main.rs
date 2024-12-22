use std::fs;

fn _parse() {
    // TODO
    let content = fs::read_to_string("input.txt").expect("not found");
    println!("{content}");
}

fn process_instructions(
    mut a: i128,
    mut b: i128,
    mut c: i128,
    instructions: Vec<i128>,
) -> (i128, i128, i128, Vec<i128>) {
    let mut i: usize = 0;
    let mut output: Vec<i128> = Vec::new();

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
        let mut goto: Option<i128> = None;

        match instruction {
            0 => a = a / 2_i128.pow(combo.try_into().unwrap()),
            1 => b ^= literal,
            2 => b = combo % 8,
            3 => {
                if a != 0 {
                    goto = Some(literal)
                }
            }
            4 => b ^= c,
            5 => output.push(combo % 8),
            6 => b = a / 2_i128.pow(combo.try_into().unwrap()),
            7 => c = a / 2_i128.pow(combo.try_into().unwrap()),
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
    let mut a = 1;
    let b = 0;
    let c = 0;
    let instructions = vec![]; // TODO parse

    let (_, _, _, mut output) = process_instructions(a, b, c, instructions.clone());

    while instructions != output {
        if instructions.len() > output.len() {
            a *= 8;
        } else {
            for index in (0..instructions.len()).rev() {
                if instructions[index] != output[index] {
                    a += 8_i128.pow(index.try_into().unwrap());
                    break;
                }
            }
        }

        (_, _, _, output) = process_instructions(a, b, c, instructions.clone());
    }
    println!("Part 2: {a}")
}
