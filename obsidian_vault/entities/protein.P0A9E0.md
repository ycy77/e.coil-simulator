---
entity_id: "protein.P0A9E0"
entity_type: "protein"
name: "araC"
source_database: "UniProt"
source_id: "P0A9E0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araC b0064 JW0063"
---

# araC

`protein.P0A9E0`

## Static

- Type: `protein`
- Source: `UniProt:P0A9E0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transcription factor that regulates the expression of several genes involved in the transport and metabolism of L-arabinose (PubMed:1447222, PubMed:2231717, PubMed:2962192, PubMed:328165, PubMed:4362626, PubMed:6251457, PubMed:6319708). Functions both as a positive and a negative regulator (PubMed:328165, PubMed:6251457). In the presence of arabinose, activates the expression of the araBAD, araE, araFGH and araJ promoters (PubMed:1447222, PubMed:2231717, PubMed:2962192, PubMed:328165, PubMed:4362626, PubMed:6251457, PubMed:6319708). In the absence of arabinose, negatively regulates the araBAD operon (PubMed:6251457). Represses its own transcription (PubMed:328165). Acts by binding directly to DNA (PubMed:1447222, PubMed:2531226, PubMed:2962192, PubMed:4943786, PubMed:6251457). {ECO:0000269|PubMed:1447222, ECO:0000269|PubMed:2231717, ECO:0000269|PubMed:2531226, ECO:0000269|PubMed:2962192, ECO:0000269|PubMed:328165, ECO:0000269|PubMed:4362626, ECO:0000269|PubMed:4943786, ECO:0000269|PubMed:6251457, ECO:0000269|PubMed:6319708}.

## Biological Role

Component of DNA-binding transcriptional dual regulator AraC (complex.ecocyc.PC00003).

## Annotation

FUNCTION: Transcription factor that regulates the expression of several genes involved in the transport and metabolism of L-arabinose (PubMed:1447222, PubMed:2231717, PubMed:2962192, PubMed:328165, PubMed:4362626, PubMed:6251457, PubMed:6319708). Functions both as a positive and a negative regulator (PubMed:328165, PubMed:6251457). In the presence of arabinose, activates the expression of the araBAD, araE, araFGH and araJ promoters (PubMed:1447222, PubMed:2231717, PubMed:2962192, PubMed:328165, PubMed:4362626, PubMed:6251457, PubMed:6319708). In the absence of arabinose, negatively regulates the araBAD operon (PubMed:6251457). Represses its own transcription (PubMed:328165). Acts by binding directly to DNA (PubMed:1447222, PubMed:2531226, PubMed:2962192, PubMed:4943786, PubMed:6251457). {ECO:0000269|PubMed:1447222, ECO:0000269|PubMed:2231717, ECO:0000269|PubMed:2531226, ECO:0000269|PubMed:2962192, ECO:0000269|PubMed:328165, ECO:0000269|PubMed:4362626, ECO:0000269|PubMed:4943786, ECO:0000269|PubMed:6251457, ECO:0000269|PubMed:6319708}.

## Outgoing Edges (22)

- `activates` --> [[gene.b0061|gene.b0061]] `RegulonDB` `C` - regulator=AraC; target=araD; function=-+
- `activates` --> [[gene.b0062|gene.b0062]] `RegulonDB` `C` - regulator=AraC; target=araA; function=-+
- `activates` --> [[gene.b0063|gene.b0063]] `RegulonDB` `C` - regulator=AraC; target=araB; function=-+
- `activates` --> [[gene.b0064|gene.b0064]] `RegulonDB` `C` - regulator=AraC; target=araC; function=-+
- `activates` --> [[gene.b0396|gene.b0396]] `RegulonDB` `S` - regulator=AraC; target=araJ; function=+
- `activates` --> [[gene.b1900|gene.b1900]] `RegulonDB` `C` - regulator=AraC; target=araG; function=+
- `activates` --> [[gene.b1901|gene.b1901]] `RegulonDB` `C` - regulator=AraC; target=araF; function=+
- `activates` --> [[gene.b2840|gene.b2840]] `RegulonDB` `S` - regulator=AraC; target=ygeA; function=+
- `activates` --> [[gene.b2841|gene.b2841]] `RegulonDB` `S` - regulator=AraC; target=araE; function=+
- `activates` --> [[gene.b4460|gene.b4460]] `RegulonDB` `S` - regulator=AraC; target=araH; function=+
- `is_component_of` --> [[complex.ecocyc.PC00003|complex.ecocyc.PC00003]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0061|gene.b0061]] `RegulonDB` `C` - regulator=AraC; target=araD; function=-+
- `represses` --> [[gene.b0062|gene.b0062]] `RegulonDB` `C` - regulator=AraC; target=araA; function=-+
- `represses` --> [[gene.b0063|gene.b0063]] `RegulonDB` `C` - regulator=AraC; target=araB; function=-+
- `represses` --> [[gene.b0064|gene.b0064]] `RegulonDB` `C` - regulator=AraC; target=araC; function=-+
- `represses` --> [[gene.b3564|gene.b3564]] `RegulonDB` `S` - regulator=AraC; target=xylB; function=-
- `represses` --> [[gene.b3565|gene.b3565]] `RegulonDB` `S` - regulator=AraC; target=xylA; function=-
- `represses` --> [[gene.b4227|gene.b4227]] `RegulonDB` `S` - regulator=AraC; target=ytfQ; function=-
- `represses` --> [[gene.b4230|gene.b4230]] `RegulonDB` `S` - regulator=AraC; target=ytfT; function=-
- `represses` --> [[gene.b4231|gene.b4231]] `RegulonDB` `S` - regulator=AraC; target=yjfF; function=-
- `represses` --> [[gene.b4485|gene.b4485]] `RegulonDB` `S` - regulator=AraC; target=ytfR; function=-
- `represses` --> [[gene.b4834|gene.b4834]] `RegulonDB` `S` - regulator=AraC; target=xylZ; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0064|gene.b0064]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9E0`
- `KEGG:ecj:JW0063;eco:b0064;`
- `GeneID:75169963;75202120;944780;`
- `GO:GO:0000976; GO:0001217; GO:0003700; GO:0005829; GO:0006355; GO:0019568; GO:0032993; GO:0042802`

## Notes

Arabinose operon regulatory protein (HTH-type transcriptional regulator AraC)
