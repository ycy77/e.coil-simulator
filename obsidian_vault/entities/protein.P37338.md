---
entity_id: "protein.P37338"
entity_type: "protein"
name: "glaR"
source_database: "UniProt"
source_id: "P37338"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glaR csiR gabC ygaE b2664 JW2639"
---

# glaR

`protein.P37338`

## Static

- Type: `protein`
- Source: `UniProt:P37338`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Negatively regulates the expression of the glaH-lhgD-gabDTP operon in a temporal manner during entry into stationary phase or during the first few hours of carbon starvation (PubMed:14731280, PubMed:30498244). Thereby is involved in the regulation of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). Binds to two primary and two secondary sites in the promoter region of the glaH operon with the consensus sequences TTGTN5TTTT and ATGTN5TTTT of the primary sites, each separated by six nucleotides (PubMed:30498244). {ECO:0000269|PubMed:14731280, ECO:0000269|PubMed:30498244}. The transcription factor CsiR, for "Carbon starvation induced Regulator," was initially identified as a repressor that controls the transcription of genes involved in the degradation and transport of 4-aminobutyrate (GABA) for utilization as a source of nitrogen . However, CsiR does not appear to respond directly to the presence of GABA , and later reports suggested that it does not affect expression of gabDTP . CsiR represses transcription from the csiD promoter during stationary phase . The CsiR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Biological Role

Component of GlaR-glutarate (complex.ecocyc.CPLX0-8293).

## Annotation

FUNCTION: Negatively regulates the expression of the glaH-lhgD-gabDTP operon in a temporal manner during entry into stationary phase or during the first few hours of carbon starvation (PubMed:14731280, PubMed:30498244). Thereby is involved in the regulation of a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). Binds to two primary and two secondary sites in the promoter region of the glaH operon with the consensus sequences TTGTN5TTTT and ATGTN5TTTT of the primary sites, each separated by six nucleotides (PubMed:30498244). {ECO:0000269|PubMed:14731280, ECO:0000269|PubMed:30498244}.

## Outgoing Edges (121)

- `activates` --> [[gene.b0088|gene.b0088]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=murD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0113|gene.b0113]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=pdhR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0139|gene.b0139]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=htrE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0141|gene.b0141]] `RegulonDB` `S` - regulator=GlaR; target=yadN; function=+
- `activates` --> [[gene.b0467|gene.b0467]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=priC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0525|gene.b0525]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ppiB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1060|gene.b1060]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=bssS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1103|gene.b1103]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=hinT; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1178|gene.b1178]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=pliG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1196|gene.b1196]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycgY; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1213|gene.b1213]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ychQ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1215|gene.b1215]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=kdsA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1499|gene.b1499]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ydeO; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1500|gene.b1500]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=safA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1518|gene.b1518]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=lsrG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1544|gene.b1544]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ydfK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1974|gene.b1974]] `RegulonDB` `S` - regulator=GlaR; target=yodB; function=+
- `activates` --> [[gene.b2041|gene.b2041]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rfbB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2111|gene.b2111]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yehD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2124|gene.b2124]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yehS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2273|gene.b2273]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfbN; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2274|gene.b2274]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfbO; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2294|gene.b2294]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfbU; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2339|gene.b2339]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfcV; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2372|gene.b2372]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfdV; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2382|gene.b2382]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ypdC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2670|gene.b2670]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=alaE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2751|gene.b2751]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=cysN; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3024|gene.b3024]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ygiW; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3078|gene.b3078]] `RegulonDB` `S` - regulator=GlaR; target=ygjI; function=+
- `activates` --> [[gene.b3214|gene.b3214]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gltF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3284|gene.b3284]] `RegulonDB` `S` - regulator=GlaR; target=smg; function=+
- `activates` --> [[gene.b3507|gene.b3507]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=dctR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3516|gene.b3516]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gadX; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3698|gene.b3698]] `RegulonDB` `S` - regulator=GlaR; target=yidB; function=+
- `activates` --> [[gene.b3818|gene.b3818]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yigG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3858|gene.b3858]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yihD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4090|gene.b4090]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rpiB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4133|gene.b4133]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=cadC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4162|gene.b4162]] `RegulonDB` `S` - regulator=GlaR; target=orn; function=+
- `activates` --> [[gene.b4200|gene.b4200]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rpsF; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4249|gene.b4249]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=bdcA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4267|gene.b4267]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=idnD; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4364|gene.b4364]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yjjP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `is_component_of` --> [[complex.ecocyc.CPLX0-8293|complex.ecocyc.CPLX0-8293]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0052|gene.b0052]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=pdxA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0112|gene.b0112]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=aroP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0186|gene.b0186]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ldcC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0468|gene.b0468]] `RegulonDB` `S` - regulator=GlaR; target=ybaN; function=-
- `represses` --> [[gene.b0469|gene.b0469]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=apt; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0497|gene.b0497]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rhsD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0526|gene.b0526]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=cysS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0635|gene.b0635]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=mrdA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0940|gene.b0940]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=elfC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0942|gene.b0942]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycbU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0943|gene.b0943]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycbV; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0964|gene.b0964]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=csgI; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0965|gene.b0965]] `RegulonDB` `S` - regulator=GlaR; target=yccU; function=-
- `represses` --> [[gene.b1020|gene.b1020]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=phoH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1102|gene.b1102]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=fhuE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1168|gene.b1168]] `RegulonDB` `S` - regulator=GlaR; target=pdeG; function=-
- `represses` --> [[gene.b1177|gene.b1177]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycgJ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1202|gene.b1202]] `RegulonDB` `S` - regulator=GlaR; target=ycgV; function=-
- `represses` --> [[gene.b1212|gene.b1212]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=prmC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1216|gene.b1216]] `RegulonDB` `S` - regulator=GlaR; target=chaA; function=-
- `represses` --> [[gene.b1217|gene.b1217]] `RegulonDB` `S` - regulator=GlaR; target=chaB; function=-
- `represses` --> [[gene.b1218|gene.b1218]] `RegulonDB` `S` - regulator=GlaR; target=chaC; function=-
- `represses` --> [[gene.b1235|gene.b1235]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=rssB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1248|gene.b1248]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yciU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1312|gene.b1312]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ycjP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1375|gene.b1375]] `RegulonDB` `S` - regulator=GlaR; target=ynaE; function=-
- `represses` --> [[gene.b1428|gene.b1428]] `RegulonDB` `S` - regulator=GlaR; target=ydcK; function=-
- `represses` --> [[gene.b1429|gene.b1429]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=tehA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1519|gene.b1519]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=tam; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1542|gene.b1542]] `RegulonDB` `S` - regulator=GlaR; target=ydfI; function=-
- `represses` --> [[gene.b1668|gene.b1668]] `RegulonDB` `S` - regulator=GlaR; target=ydhS; function=-
- `represses` --> [[gene.b1760|gene.b1760]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ynjH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1761|gene.b1761]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gdhA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1781|gene.b1781]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yeaE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1820|gene.b1820]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yobD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1886|gene.b1886]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=tar; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2078|gene.b2078]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=baeS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2112|gene.b2112]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2149|gene.b2149]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=mglA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2237|gene.b2237]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=inaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2293|gene.b2293]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=hxpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2332|gene.b2332]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfcO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2347|gene.b2347]] `RegulonDB` `S` - regulator=GlaR; target=yfdC; function=-
- `represses` --> [[gene.b2373|gene.b2373]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=oxc; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2502|gene.b2502]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ppx; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2602|gene.b2602]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfiL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2603|gene.b2603]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yfiR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2604|gene.b2604]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=dgcN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2647|gene.b2647]] `RegulonDB` `S` - regulator=GlaR; target=ypjA; function=-
- `represses` --> [[gene.b2659|gene.b2659]] `RegulonDB` `C` - regulator=GlaR; target=glaH; function=-
- `represses` --> [[gene.b2660|gene.b2660]] `RegulonDB` `C` - regulator=GlaR; target=lhgD; function=-
- `represses` --> [[gene.b2661|gene.b2661]] `RegulonDB` `C` - regulator=GlaR; target=gabD; function=-
- `represses` --> [[gene.b2662|gene.b2662]] `RegulonDB` `S` - regulator=GlaR; target=gabT; function=-
- `represses` --> [[gene.b2663|gene.b2663]] `RegulonDB` `S` - regulator=GlaR; target=gabP; function=-
- `represses` --> [[gene.b2760|gene.b2760]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=casA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2808|gene.b2808]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gcvA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3010|gene.b3010]] `RegulonDB` `S` - regulator=GlaR; target=yqhC; function=-
- `represses` --> [[gene.b3023|gene.b3023]] `RegulonDB` `S` - regulator=GlaR; target=ygiV; function=-
- `represses` --> [[gene.b3060|gene.b3060]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ttdR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3061|gene.b3061]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ttdA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3216|gene.b3216]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yhcD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3389|gene.b3389]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=aroB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3515|gene.b3515]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gadW; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3661|gene.b3661]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=nlpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3873|gene.b3873]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yihM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3909|gene.b3909]] `RegulonDB` `S` - regulator=GlaR; target=kdgT; function=-
- `represses` --> [[gene.b4004|gene.b4004]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=zraR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4161|gene.b4161]] `RegulonDB` `S` - regulator=GlaR; target=rsgA; function=-
- `represses` --> [[gene.b4199|gene.b4199]] `RegulonDB` `S` - regulator=GlaR; target=yjfY; function=-
- `represses` --> [[gene.b4251|gene.b4251]] `RegulonDB` `S` - regulator=GlaR; target=bdcR; function=-
- `represses` --> [[gene.b4268|gene.b4268]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=idnK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4304|gene.b4304]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=sgcC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4365|gene.b4365]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yjjQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4461|gene.b4461]] `RegulonDB` `S` - regulator=GlaR; target=yfjD; function=-
- `represses` --> [[gene.b4487|gene.b4487]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yjdP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4613|gene.b4613]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=dinQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b2664|gene.b2664]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37338`
- `KEGG:ecj:JW2639;eco:b2664;ecoc:C3026_14685;`
- `GeneID:93779348;948055;`
- `GO:GO:0000987; GO:0003700; GO:0005737; GO:0006355; GO:2000143`

## Notes

HTH-type transcriptional repressor GlaR (Carbon starvation induced regulator) (GlaH operon repressor)
