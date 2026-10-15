export const columns = ['Date','Channel','Campaign','Impressions','Clicks','Cost_EUR','Leads','Qualified_Leads','Conversions','Revenue_EUR'];
export const metadata = { synthetic: true, seed: 7312026, start: '2026-04-01', end: '2026-09-30', currency: 'EUR', grain: 'acquisition date × channel × campaign', attribution: 'resolved synthetic acquisition cohort; no conversion lag', costScope: 'paid media only; excludes payroll, agency, software and organic production costs' };
export function generateMatrix() {
  let state = metadata.seed;
  const random = () => ((state = (1664525 * state + 1013904223) >>> 0) / 4294967296);
  const binomial = (n,p) => { let total=0; for(let i=0;i<n;i++) if(random()<p) total++; return total; };
  const channels = [
    ['Google Search',7000,.055,1.45,.085,.61,.20],
    ['Meta Ads',18000,.018,.72,.07,.42,.15],
    ['LinkedIn Ads',5000,.012,3.65,.095,.73,.25],
    ['Organic Search',3500,.07,0,.09,.57,.20],
  ];
  const rows = [columns];
  for(let time=Date.parse(metadata.start);time<=Date.parse(metadata.end);time+=86400000) {
    const date=new Date(time); const month=date.getUTCMonth()-3;
    const weekend=[0,6].includes(date.getUTCDay())?.72:1;
    const season=[1,1.04,1.08,.93,.9,1.1][month];
    for(const [channel,base,ctr,cpc,cvr,quality,close] of channels) for(const intent of ['Prospecting','HighIntent']) {
      const high=intent==='HighIntent';
      const impressions=Math.round(base*(high?.34:1)*weekend*season*(.8+random()*.4));
      const clicks=Math.round(impressions*ctr*(high?1.25:1)*(.8+random()*.4));
      const leads=binomial(clicks,Math.min(.5,cvr*(high?1.3:1)*(1+month*.025)));
      const qualityAdjustment=channel==='Meta Ads'&&month===2?.72:1;
      const qualified=binomial(leads,Math.min(.95,quality*(high?1.15:1)*qualityAdjustment));
      const conversions=binomial(qualified,close);
      const cost=Math.round(clicks*cpc*(.9+random()*.2)*100)/100;
      const revenue=Math.round(conversions*(1200+random()*700)*100)/100;
      rows.push([date.toISOString().slice(0,10),channel,intent,impressions,clicks,cost,leads,qualified,conversions,revenue]);
    }
  }
  return rows;
}
export const encodeCSV = matrix => matrix.map(row=>row.map(v=>{
  const text=String(v);return /[",\r\n]/.test(text)?'"'+text.replaceAll('"','""')+'"':text;
}).join(',')).join('\n')+'\n';
