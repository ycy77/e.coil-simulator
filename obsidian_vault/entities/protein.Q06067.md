---
entity_id: "protein.Q06067"
entity_type: "protein"
name: "atoS"
source_database: "UniProt"
source_id: "Q06067"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16153782}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "atoS b2219 JW2213"
---

# atoS

`protein.Q06067`

## Static

- Type: `protein`
- Source: `UniProt:Q06067`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16153782}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system AtoS/AtoC. In the presence of acetoacetate, AtoS/AtoC stimulates the expression of the atoDAEB operon, leading to short chain fatty acid catabolism and activation of the poly-(R)-3-hydroxybutyrate (cPHB) biosynthetic pathway. Also induces the operon in response to spermidine (PubMed:16153782, PubMed:16564134, PubMed:17475408). Involved in the regulation of motility and chemotaxis, via transcriptional induction of the flagellar regulon (PubMed:22083893). AtoS is a membrane-associated kinase that phosphorylates and activates AtoC in response to environmental signals (PubMed:16153782, PubMed:18534200). {ECO:0000269|PubMed:16153782, ECO:0000269|PubMed:16564134, ECO:0000269|PubMed:17475408, ECO:0000269|PubMed:18534200, ECO:0000269|PubMed:22083893}.

## Biological Role

Component of sensor histidine kinase AtoS (complex.ecocyc.CPLX0-7870), AtoS-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-ATOS).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system AtoS/AtoC. In the presence of acetoacetate, AtoS/AtoC stimulates the expression of the atoDAEB operon, leading to short chain fatty acid catabolism and activation of the poly-(R)-3-hydroxybutyrate (cPHB) biosynthetic pathway. Also induces the operon in response to spermidine (PubMed:16153782, PubMed:16564134, PubMed:17475408). Involved in the regulation of motility and chemotaxis, via transcriptional induction of the flagellar regulon (PubMed:22083893). AtoS is a membrane-associated kinase that phosphorylates and activates AtoC in response to environmental signals (PubMed:16153782, PubMed:18534200). {ECO:0000269|PubMed:16153782, ECO:0000269|PubMed:16564134, ECO:0000269|PubMed:17475408, ECO:0000269|PubMed:18534200, ECO:0000269|PubMed:22083893}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7870|complex.ecocyc.CPLX0-7870]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-ATOS|complex.ecocyc.PHOSPHO-ATOS]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2219|gene.b2219]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q06067`
- `KEGG:ecj:JW2213;eco:b2219;ecoc:C3026_12405;`
- `GeneID:949011;`
- `GO:GO:0000155; GO:0005524; GO:0005886; GO:0006355; GO:0007165; GO:0042803; GO:1904583`
- `EC:2.7.13.3`

## Notes

Signal transduction histidine-protein kinase AtoS (EC 2.7.13.3)
