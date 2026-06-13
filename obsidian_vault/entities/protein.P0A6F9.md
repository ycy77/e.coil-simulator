---
entity_id: "protein.P0A6F9"
entity_type: "protein"
name: "groES"
source_database: "UniProt"
source_id: "P0A6F9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00580, ECO:0000269|PubMed:22380631}. Note=Exclusively localized in foci, usually near 1 cell pole in mid-to-late exponential phase; polar localization depends on the minCDE operon. Foci form near midcell."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "groES groS mopB b4142 JW4102"
---

# groES

`protein.P0A6F9`

## Static

- Type: `protein`
- Source: `UniProt:P0A6F9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00580, ECO:0000269|PubMed:22380631}. Note=Exclusively localized in foci, usually near 1 cell pole in mid-to-late exponential phase; polar localization depends on the minCDE operon. Foci form near midcell.

## Enriched Summary

FUNCTION: Together with the chaperonin GroEL, plays an essential role in assisting protein folding (PubMed:10532860, PubMed:16751100, PubMed:1676490, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391, PubMed:2573517, PubMed:2897629). The GroEL-GroES system forms a nano-cage that allows encapsulation of the non-native substrate proteins and provides a physical environment optimized to promote and accelerate protein folding, probably by preventing aggregation and by entropically destabilizing folding intermediates (PubMed:16751100, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391). GroES binds to the apical surface of the GroEL ring, thereby capping the opening of the GroEL channel (PubMed:9285585). Regulates the ATPase activity of GroEL (PubMed:1361169, PubMed:1676490). {ECO:0000269|PubMed:10532860, ECO:0000269|PubMed:1361169, ECO:0000269|PubMed:16751100, ECO:0000269|PubMed:1676490, ECO:0000269|PubMed:18418386, ECO:0000269|PubMed:18987317, ECO:0000269|PubMed:20603018, ECO:0000269|PubMed:24816391, ECO:0000269|PubMed:2573517, ECO:0000269|PubMed:2897629, ECO:0000269|PubMed:9285585}.; FUNCTION: (Microbial infection) Essential for the assembly of several bacteriophages. {ECO:0000269|PubMed:379350, ECO:0000269|PubMed:7015340}. groS belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Component of GroEL-GroES chaperonin complex (complex.ecocyc.CPLX0-3934).

## Annotation

FUNCTION: Together with the chaperonin GroEL, plays an essential role in assisting protein folding (PubMed:10532860, PubMed:16751100, PubMed:1676490, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391, PubMed:2573517, PubMed:2897629). The GroEL-GroES system forms a nano-cage that allows encapsulation of the non-native substrate proteins and provides a physical environment optimized to promote and accelerate protein folding, probably by preventing aggregation and by entropically destabilizing folding intermediates (PubMed:16751100, PubMed:18418386, PubMed:18987317, PubMed:20603018, PubMed:24816391). GroES binds to the apical surface of the GroEL ring, thereby capping the opening of the GroEL channel (PubMed:9285585). Regulates the ATPase activity of GroEL (PubMed:1361169, PubMed:1676490). {ECO:0000269|PubMed:10532860, ECO:0000269|PubMed:1361169, ECO:0000269|PubMed:16751100, ECO:0000269|PubMed:1676490, ECO:0000269|PubMed:18418386, ECO:0000269|PubMed:18987317, ECO:0000269|PubMed:20603018, ECO:0000269|PubMed:24816391, ECO:0000269|PubMed:2573517, ECO:0000269|PubMed:2897629, ECO:0000269|PubMed:9285585}.; FUNCTION: (Microbial infection) Essential for the assembly of several bacteriophages. {ECO:0000269|PubMed:379350, ECO:0000269|PubMed:7015340}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3934|complex.ecocyc.CPLX0-3934]] `EcoCyc` `database` - EcoCyc component coefficient=14 | EcoCyc protcplxs.col coefficient=14

## Incoming Edges (1)

- `encodes` <-- [[gene.b4142|gene.b4142]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6F9`
- `KEGG:ecj:JW4102;eco:b4142;ecoc:C3026_22385;`
- `GeneID:86861465;948655;`
- `GO:GO:0005524; GO:0005829; GO:0006457; GO:0009408; GO:0019068; GO:0042802; GO:0044183; GO:0046872; GO:0051082; GO:0051087; GO:1990220`

## Notes

Co-chaperonin GroES (10 kDa chaperonin) (Chaperonin-10) (Cpn10)
