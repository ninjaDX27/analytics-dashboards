import { mkdir,writeFile } from 'node:fs/promises';
import { generateMatrix, encodeCSV, metadata } from '../src/simulated.mjs';
const root=new URL('../datasets/',import.meta.url);await mkdir(root,{recursive:true});
await writeFile(new URL('acquisition-funnel-simulated.csv',root),encodeCSV(generateMatrix()));
await writeFile(new URL('metadata.json',root),JSON.stringify(metadata,null,2)+'\n');
console.log('Generated synthetic acquisition cohorts, April–September 2026.');
