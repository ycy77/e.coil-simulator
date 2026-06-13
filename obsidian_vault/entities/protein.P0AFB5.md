---
entity_id: "protein.P0AFB5"
entity_type: "protein"
name: "glnL"
source_database: "UniProt"
source_id: "P0AFB5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:15157101}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnL glnR ntrB b3869 JW3840"
---

# glnL

`protein.P0AFB5`

## Static

- Type: `protein`
- Source: `UniProt:P0AFB5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:15157101}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system NtrB/NtrC, which controls expression of the nitrogen-regulated (ntr) genes in response to nitrogen limitation. Under conditions of nitrogen limitation, NtrB autophosphorylates and transfers the phosphoryl group to NtrC. In the presence of nitrogen, acts as a phosphatase that dephosphorylates and inactivates NtrC. {ECO:0000269|PubMed:10074086, ECO:0000269|PubMed:2574599, ECO:0000269|PubMed:2874557, ECO:0000269|PubMed:3304660}.

## Biological Role

Component of protein histidine kinase NtrB (complex.ecocyc.GLNL-CPLX), NtrB-N-phospho-L-histidine (complex.ecocyc.PROTEIN-NRIIP).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system NtrB/NtrC, which controls expression of the nitrogen-regulated (ntr) genes in response to nitrogen limitation. Under conditions of nitrogen limitation, NtrB autophosphorylates and transfers the phosphoryl group to NtrC. In the presence of nitrogen, acts as a phosphatase that dephosphorylates and inactivates NtrC. {ECO:0000269|PubMed:10074086, ECO:0000269|PubMed:2574599, ECO:0000269|PubMed:2874557, ECO:0000269|PubMed:3304660}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.GLNL-CPLX|complex.ecocyc.GLNL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PROTEIN-NRIIP|complex.ecocyc.PROTEIN-NRIIP]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3869|gene.b3869]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFB5`
- `KEGG:ecj:JW3840;eco:b3869;ecoc:C3026_20915;`
- `GeneID:86861973;93778067;948360;`
- `GO:GO:0000155; GO:0004673; GO:0004721; GO:0005524; GO:0005737; GO:0006355; GO:0007165; GO:0016774; GO:0023019; GO:0042802; GO:0042803`
- `EC:2.7.13.3; 3.1.3.-`

## Notes

Sensory histidine kinase/phosphatase NtrB (EC 2.7.13.3) (EC 3.1.3.-) (Nitrogen regulation protein NR(II)) (Nitrogen regulator II) (NRII)
