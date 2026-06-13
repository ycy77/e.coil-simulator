---
entity_id: "protein.P0DMC7"
entity_type: "protein"
name: "rcsB"
source_database: "UniProt"
source_id: "P0DMC7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rcsB b2217 JW2205"
---

# rcsB

`protein.P0DMC7`

## Static

- Type: `protein`
- Source: `UniProt:P0DMC7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. RcsB is the response regulator that binds to regulatory DNA regions. Can function both in an RcsA-dependent or RcsA-independent manner. The system regulates expression of numerous genes, including genes involved in colanic acid capsule synthesis, biofilm formation, cell division and outer membrane proteins synthesis. Also involved, with GadE, in control of glutamate-dependent acid resistance, and, with BglJ, in derepression of the cryptic bgl operon. The RcsB-BglJ activity is probably independent of RcsB phosphorylation. {ECO:0000255|HAMAP-Rule:MF_00981, ECO:0000269|PubMed:10702265, ECO:0000269|PubMed:11309126, ECO:0000269|PubMed:11566985, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:1597415, ECO:0000269|PubMed:20189963, ECO:0000269|PubMed:20952573}. RcsB protein for "Regulator capsule synthesis B," is a response regulator that belongs to the multicomponent RcsF/RcsC/RcsD/RcsA-RcsB phosphorelay system and is involved in the regulation of the synthesis of colanic acid capsule, cell division, periplasmic proteins, motility, biofilm formation, and a small RNA . It has been observed that Rcs phosphorelay was beneficial for biofilm fitness in Salmonella Typhimurium as in E. coli...

## Biological Role

Component of GadE-RcsB DNA-binding transcriptional activator (complex.ecocyc.CPLX0-7852), RcsB-BglJ DNA-binding transcriptional activator (complex.ecocyc.CPLX0-7916), RcsAB DNA-binding transcriptional dual regulator (complex.ecocyc.PC00084).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. RcsB is the response regulator that binds to regulatory DNA regions. Can function both in an RcsA-dependent or RcsA-independent manner. The system regulates expression of numerous genes, including genes involved in colanic acid capsule synthesis, biofilm formation, cell division and outer membrane proteins synthesis. Also involved, with GadE, in control of glutamate-dependent acid resistance, and, with BglJ, in derepression of the cryptic bgl operon. The RcsB-BglJ activity is probably independent of RcsB phosphorylation. {ECO:0000255|HAMAP-Rule:MF_00981, ECO:0000269|PubMed:10702265, ECO:0000269|PubMed:11309126, ECO:0000269|PubMed:11566985, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:1597415, ECO:0000269|PubMed:20189963, ECO:0000269|PubMed:20952573}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (17)

- `activates` --> [[gene.b0094|gene.b0094]] `RegulonDB` `S` - regulator=RcsB; target=ftsA; function=+
- `activates` --> [[gene.b0095|gene.b0095]] `RegulonDB` `S` - regulator=RcsB; target=ftsZ; function=+
- `activates` --> [[gene.b1480|gene.b1480]] `RegulonDB` `S` - regulator=RcsB; target=sra; function=+
- `activates` --> [[gene.b1481|gene.b1481]] `RegulonDB` `S` - regulator=RcsB; target=bdm; function=+
- `activates` --> [[gene.b1482|gene.b1482]] `RegulonDB` `C` - regulator=RcsB; target=osmC; function=+
- `activates` --> [[gene.b1501|gene.b1501]] `RegulonDB` `S` - regulator=RcsB; target=ydeP; function=+
- `activates` --> [[gene.b2570|gene.b2570]] `RegulonDB` `C` - regulator=RcsB; target=rseC; function=+
- `activates` --> [[gene.b2571|gene.b2571]] `RegulonDB` `C` - regulator=RcsB; target=rseB; function=+
- `activates` --> [[gene.b2572|gene.b2572]] `RegulonDB` `C` - regulator=RcsB; target=rseA; function=+
- `activates` --> [[gene.b2573|gene.b2573]] `RegulonDB` `C` - regulator=RcsB; target=rpoE; function=+
- `activates` --> [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=RcsB; target=rprA; function=+
- `activates` --> [[gene.b4725|gene.b4725]] `RegulonDB` `C` - regulator=RcsB; target=rseD; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7852|complex.ecocyc.CPLX0-7852]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7916|complex.ecocyc.CPLX0-7916]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.PC00084|complex.ecocyc.PC00084]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `represses` --> [[gene.b3516|gene.b3516]] `RegulonDB` `C` - regulator=RcsB; target=gadX; function=-
- `represses` --> [[gene.b3517|gene.b3517]] `RegulonDB` `C` - regulator=RcsB; target=gadA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2217|gene.b2217]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DMC7`
- `KEGG:ecj:JW2205;eco:b2217;ecoc:C3026_12395;`
- `GeneID:45134793;93774960;947441;`
- `GO:GO:0000160; GO:0000976; GO:0001216; GO:0001217; GO:0003700; GO:0005667; GO:0005829; GO:0006351; GO:0006355; GO:0031346; GO:0042802; GO:0043470; GO:0044011; GO:0045892; GO:0045893; GO:0046677; GO:1901913; GO:1902021; GO:1990451`

## Notes

Transcriptional regulatory protein RcsB (Capsular synthesis regulator component B)
