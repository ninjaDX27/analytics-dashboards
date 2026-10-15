import { columns } from './simulated.mjs';
export function parseDataset(csv) {
  const lines=csv.trim().split(/\r?\n/);
  if(lines.shift()!==columns.join(','))throw new Error('Unexpected columns');
  // This exported fixture has no quoted fields. Reject rather than silently misparse other CSVs.
  return lines.map(line=>{
    if(line.includes('"'))throw new Error('Quoted CSV requires a general CSV reader');
    const fields=line.split(',');if(fields.length!==10)throw new Error('Invalid row width');
    return Object.fromEntries(columns.map((key,i)=>[key,i<3?fields[i]:fields[i].trim()===''?NaN:Number(fields[i])]));
  });
}
export const divide = (numerator,denominator) => denominator===0?null:numerator/denominator;
export function summarize(rows) {
  const sums=Object.fromEntries(columns.slice(3).map(k=>[k,0]));
  for(const row of rows)for(const key of Object.keys(sums))sums[key]+=key.endsWith('_EUR')?Math.round(row[key]*100):row[key];
  sums.Cost_EUR/=100;sums.Revenue_EUR/=100;
  return {...sums,mediaCAC:divide(sums.Cost_EUR,sums.Conversions),CPQL:divide(sums.Cost_EUR,sums.Qualified_Leads),qualificationRate:divide(sums.Qualified_Leads,sums.Leads),blendedROAS:divide(sums.Revenue_EUR,sums.Cost_EUR)};
}
export function validateRows(rows) {
  const keys=new Set();
  for(const row of rows){
    const key=[row.Date,row.Channel,row.Campaign].join('|');if(keys.has(key))throw new Error('Duplicate grain');keys.add(key);
    if(!/^2026-(04|05|06|07|08|09)-\d{2}$/.test(row.Date)||new Date(row.Date).toISOString().slice(0,10)!==row.Date)throw new Error('Invalid date');
    for(const k of columns.slice(3))if(!Number.isFinite(row[k])||row[k]<0||(!k.endsWith('_EUR')&&!Number.isSafeInteger(row[k])))throw new Error('Invalid numeric measure');
    if(!(row.Impressions>=row.Clicks&&row.Clicks>=row.Leads&&row.Leads>=row.Qualified_Leads&&row.Qualified_Leads>=row.Conversions))throw new Error('Impossible funnel');
    if(row.Conversions===0&&row.Revenue_EUR!==0)throw new Error('Revenue without conversion');
  }
  return {rows:rows.length,uniqueDays:new Set(rows.map(r=>r.Date)).size,months:new Set(rows.map(r=>r.Date.slice(0,7))).size};
}
