---
entity_id: "protein.P0AE76"
entity_type: "protein"
name: "cobU"
source_database: "UniProt"
source_id: "P0AE76"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cobU b1993 JW1971"
---

# cobU

`protein.P0AE76`

## Static

- Type: `protein`
- Source: `UniProt:P0AE76`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes ATP-dependent phosphorylation of adenosylcobinamide and addition of GMP to adenosylcobinamide phosphate. {ECO:0000250|UniProtKB:Q05599}. E. coli K-12, as well as natural isolates, can synthesize cobalamin only when supplied with the intermediate cobinamide . cobU encodes a predicted bifunctional protein complex with cobinamide kinase and cobinamide-P guanylyltransferase activity . Expression of the cobUST operon is induced by cobinamide .

## Biological Role

Component of cobinamide-P guanylyltransferase / cobinamide kinase (complex.ecocyc.COBU-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes ATP-dependent phosphorylation of adenosylcobinamide and addition of GMP to adenosylcobinamide phosphate. {ECO:0000250|UniProtKB:Q05599}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.COBU-CPLX|complex.ecocyc.COBU-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1993|gene.b1993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE76`
- `KEGG:ecj:JW1971;eco:b1993;ecoc:C3026_11245;`
- `GeneID:946519;`
- `GO:GO:0005524; GO:0005525; GO:0006779; GO:0006974; GO:0008820; GO:0009236; GO:0043752`
- `EC:2.7.1.156; 2.7.7.62`

## Notes

Bifunctional adenosylcobalamin biosynthesis protein CobU (Adenosylcobinamide kinase) (EC 2.7.1.156) (Adenosylcobinamide-phosphate guanylyltransferase) (EC 2.7.7.62)
