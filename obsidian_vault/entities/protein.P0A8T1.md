---
entity_id: "protein.P0A8T1"
entity_type: "protein"
name: "prmA"
source_database: "UniProt"
source_id: "P0A8T1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00735, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prmA yhdI b3259 JW3227"
---

# prmA

`protein.P0A8T1`

## Static

- Type: `protein`
- Source: `UniProt:P0A8T1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00735, ECO:0000305}.

## Enriched Summary

FUNCTION: Methylates ribosomal protein L11. {ECO:0000255|HAMAP-Rule:MF_00735, ECO:0000269|PubMed:372746, ECO:0000269|PubMed:7715456}. PrmA is the methyltransferase responsible for the multiple methylation of EG10872-MONOMER. Free L11 is a better substrate than assembled 50S ribosomal subunits . prmA mutants are deficient in the methylation of ribosomal protein L11 . A strain containing a prmA null mutation is viable and shows no growth defect, indicating that lack of methylation of L11 does not affect its function in the ribosome . PrmA: "protein methylation A"

## Biological Role

Catalyzes RXN0-5419 (reaction.ecocyc.RXN0-5419).

## Annotation

FUNCTION: Methylates ribosomal protein L11. {ECO:0000255|HAMAP-Rule:MF_00735, ECO:0000269|PubMed:372746, ECO:0000269|PubMed:7715456}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5419|reaction.ecocyc.RXN0-5419]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3259|gene.b3259]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8T1`
- `KEGG:ecj:JW3227;eco:b3259;ecoc:C3026_17730;`
- `GeneID:75173428;75206107;947708;`
- `GO:GO:0005829; GO:0016279; GO:0032259; GO:0071885`
- `EC:2.1.1.-`

## Notes

Ribosomal protein L11 methyltransferase (L11 Mtase) (EC 2.1.1.-)
