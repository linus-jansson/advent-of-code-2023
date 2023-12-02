import fs from 'node:fs/promises';

async function main() {
    const data = await fs.readFile('input.txt', 'utf8');

    const lines = data.split('\n');

    console.log(lines)

    lines.map((line) =>  {
        for (let i = 0; i < line.length; i++) {
            const char = line[i];
            let tmp = ''
            if (parseInt(char) === Number.NaN)
            {
                continue;
            }
            else {
                if (tmp.length === 0 || tmp.length === i) {
                    
                }
            }

            console.log(line[i])
        }
    })

}


main();
