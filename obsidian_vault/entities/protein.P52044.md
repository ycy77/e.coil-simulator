---
entity_id: "protein.P52044"
entity_type: "protein"
name: "ygfI"
source_database: "UniProt"
source_id: "P52044"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygfI b2921 JW5476"
---

# ygfI

`protein.P52044`

## Static

- Type: `protein`
- Source: `UniProt:P52044`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YgfI YgfI is a LysR-type transcription factor involved in regulation of formate, glycerol, dihydroxyacetone, and fucose utilization, hydrogen peroxide resistance, biofilm formation, antibiotic resistance, and stationary phase . The transcription of the srsR gene increases during transition to stationary phase for growth in LB medium, reaching levels in stationary phase 25 times higher than those of the exponential phase . YgfI was also found transcriptionally up-regulated in the presence of threonine (Thr) in M9 medium . Genome-wide YgfI binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium and in vitro by genomic systematic evolution of ligands using exponential enrichment (gSELEX-chip) . A total of 10 YgfI binding regions were identified by gSELEX-chip, some of them flanking operons, giving rise to an estimated of 30 putative regulated genes; the transcriptional regulation in vivo of various genes was confirmed by RT-qPCR . The 11-bp YfgI box TCAGATTTTGC was determined by in vitro gel shift assay and DNase-I footprinting assays in the yfdONMLK-yfdPQ spacer identified by gSELEX-chip, in which four boxes were found, after this consensus sequence was identified in the other binding regions...

## Annotation

Uncharacterized HTH-type transcriptional regulator YgfI

## Outgoing Edges (37)

- `activates` --> [[gene.b0225|gene.b0225]] `RegulonDB` `C` - regulator=SrsR; target=yafQ; function=+
- `activates` --> [[gene.b0226|gene.b0226]] `RegulonDB` `C` - regulator=SrsR; target=dinJ; function=+
- `activates` --> [[gene.b0227|gene.b0227]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=yafL; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b0903|gene.b0903]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1162|gene.b1162]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=bluR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1198|gene.b1198]] `RegulonDB` `S` - regulator=SrsR; target=dhaM; function=+
- `activates` --> [[gene.b1199|gene.b1199]] `RegulonDB` `S` - regulator=SrsR; target=dhaL; function=+
- `activates` --> [[gene.b1200|gene.b1200]] `RegulonDB` `S` - regulator=SrsR; target=dhaK; function=+
- `activates` --> [[gene.b1241|gene.b1241]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1387|gene.b1387]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=paaZ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1388|gene.b1388]] `RegulonDB` `C` - regulator=SrsR; target=paaA; function=+
- `activates` --> [[gene.b1389|gene.b1389]] `RegulonDB` `C` - regulator=SrsR; target=paaB; function=+
- `activates` --> [[gene.b1390|gene.b1390]] `RegulonDB` `C` - regulator=SrsR; target=paaC; function=+
- `activates` --> [[gene.b1391|gene.b1391]] `RegulonDB` `C` - regulator=SrsR; target=paaD; function=+
- `activates` --> [[gene.b1392|gene.b1392]] `RegulonDB` `C` - regulator=SrsR; target=paaE; function=+
- `activates` --> [[gene.b1393|gene.b1393]] `RegulonDB` `C` - regulator=SrsR; target=paaF; function=+
- `activates` --> [[gene.b1394|gene.b1394]] `RegulonDB` `C` - regulator=SrsR; target=paaG; function=+
- `activates` --> [[gene.b1395|gene.b1395]] `RegulonDB` `C` - regulator=SrsR; target=paaH; function=+
- `activates` --> [[gene.b1396|gene.b1396]] `RegulonDB` `C` - regulator=SrsR; target=paaI; function=+
- `activates` --> [[gene.b1397|gene.b1397]] `RegulonDB` `C` - regulator=SrsR; target=paaJ; function=+
- `activates` --> [[gene.b1398|gene.b1398]] `RegulonDB` `C` - regulator=SrsR; target=paaK; function=+
- `activates` --> [[gene.b1468|gene.b1468]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1785|gene.b1785]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=cdgI; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2354|gene.b2354]] `RegulonDB` `C` - regulator=SrsR; target=yfdK; function=+
- `activates` --> [[gene.b2356|gene.b2356]] `RegulonDB` `C` - regulator=SrsR; target=yfdM; function=+
- `activates` --> [[gene.b2357|gene.b2357]] `RegulonDB` `C` - regulator=SrsR; target=yfdN; function=+
- `activates` --> [[gene.b2358|gene.b2358]] `RegulonDB` `C` - regulator=SrsR; target=yfdO; function=+
- `activates` --> [[gene.b2359|gene.b2359]] `RegulonDB` `C` - regulator=SrsR; target=yfdP; function=+
- `activates` --> [[gene.b2360|gene.b2360]] `RegulonDB` `C` - regulator=SrsR; target=yfdQ; function=+
- `activates` --> [[gene.b2724|gene.b2724]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2799|gene.b2799]] `RegulonDB` `C` - regulator=SrsR; target=fucO; function=+
- `activates` --> [[gene.b2800|gene.b2800]] `RegulonDB` `C` - regulator=SrsR; target=fucA; function=+
- `activates` --> [[gene.b2801|gene.b2801]] `RegulonDB` `C` - regulator=SrsR; target=fucP; function=+
- `activates` --> [[gene.b2802|gene.b2802]] `RegulonDB` `C` - regulator=SrsR; target=fucI; function=+
- `activates` --> [[gene.b2803|gene.b2803]] `RegulonDB` `C` - regulator=SrsR; target=fucK; function=+
- `activates` --> [[gene.b2804|gene.b2804]] `RegulonDB` `C` - regulator=SrsR; target=fucU; function=+
- `activates` --> [[gene.b2805|gene.b2805]] `RegulonDB` `C` - regulator=SrsR; target=fucR; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b2921|gene.b2921]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52044`
- `KEGG:ecj:JW5476;eco:b2921;ecoc:C3026_16005;`
- `GeneID:75205241;947401;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0006974`

## Notes

Uncharacterized HTH-type transcriptional regulator YgfI
