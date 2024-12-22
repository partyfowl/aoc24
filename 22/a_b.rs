use std::collections::HashMap;
use std::collections::VecDeque;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn mix_and_prune(secret: i64, other_number: i64) -> i64 {
    return (secret ^ other_number) % 16777216;
}

fn evolve(mut secret: i64) -> i64 {
    secret = mix_and_prune(secret, secret * 64);
    secret = mix_and_prune(secret, secret / 32);
    secret = mix_and_prune(secret, secret * 2048);
    return secret;
}

fn main() {
    let file = File::open("input.txt").expect("not found");
    let reader = BufReader::new(file);

    let secrets: Vec<i64> = reader
        .lines()
        .map(|line| line.unwrap().parse::<i64>().unwrap())
        .collect();

    let iterations = 2000;
    let combo_length = 4;

    let mut part_1_total = 0;

    let mut combo_cache: HashMap<i64, HashMap<(i64, i64, i64, i64), i64>> = HashMap::new();

    for mut secret in secrets {
        let key = secret;

        let mut combos: HashMap<(i64, i64, i64, i64), i64> = HashMap::new();
        let mut price = secret % 10;

        let mut changes: VecDeque<i64> = VecDeque::with_capacity(combo_length);

        for i in 1..iterations + 1 {
            secret = evolve(secret);
            let new_price = secret % 10;
            let change = new_price - price;
            price = new_price;
            changes.push_front(change);
            if i >= combo_length {
                let a = changes[3];
                let b = changes[2];
                let c = changes[1];
                let d = changes[0];
                combos.entry((a, b, c, d)).or_insert(price);
            }
        }
        combo_cache.insert(key, combos);
        part_1_total = part_1_total + secret
    }

    let mut combo_scores: HashMap<(i64, i64, i64, i64), i64> = HashMap::new();

    for combos in combo_cache.values() {
        for (combo, price) in combos {
            combo_scores
                .entry(*combo)
                .and_modify(|k| *k += *price)
                .or_insert(*price);
        }
    }

    let mut part_2_total: i64 = 0;

    for total in combo_scores.values() {
        if *total > part_2_total {
            part_2_total = *total;
        }
    }

    println!("Part 1: {part_1_total}");
    println!("Part 2: {part_2_total}");
}
