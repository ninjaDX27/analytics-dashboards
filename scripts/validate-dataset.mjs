import {readFile} from 'node:fs/promises';import {parseDataset,summarize,validateRows} from '../src/metrics.mjs';
const rows=parseDataset(await readFile(new URL('../datasets/acquisition-funnel-simulated.csv',import.meta.url),'utf8'));
console.log(JSON.stringify({synthetic:true,...validateRows(rows),totals:summarize(rows)},null,2));
