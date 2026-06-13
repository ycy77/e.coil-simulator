---
entity_id: "protein.P00816"
entity_type: "protein"
name: "cynS"
source_database: "UniProt"
source_id: "P00816"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cynS cnt b0340 JW0331"
---

# cynS

`protein.P00816`

## Static

- Type: `protein`
- Source: `UniProt:P00816`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reaction of cyanate with bicarbonate to produce ammonia and carbon dioxide. Cyanase is an inducible enzyme in E. coli and was first reported and subsequently studied in E. coli B . The cyanase operon may have evolved to function in detoxification/decomposition of cyanate arising from intra- and extracellular activities . It was shown that bicarbonate (HCO3-) is a substrate of the enzyme, and that water does not participate as a substrate . The initial product carbamate is unstable and spontaneously decomposes to ammonia and carbon dioxide . The enzyme shows competitive substrate inhibition by both substrates . The native enzyme from E. coli B has a molecular weight of ca. 150 kDa and thus appears to be a homodecamer in solution . A crystal structure of cyanase was solved at 1.65 Å resolution; it showed a homodecamer composed of five dimers. The structure allowed identification of the active site, which is located between dimers and is comprised of residues from four adjacent subunits . The free sulfhydryl group of the single cysteine residue is not required for catalytic activity, but plays a role in stabilizing the decameric structure . The single histidine residue is also required for the stability of the decamer and contributes to its catalytic properties...

## Biological Role

Component of cyanase (complex.ecocyc.CYANLY-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reaction of cyanate with bicarbonate to produce ammonia and carbon dioxide.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CYANLY-CPLX|complex.ecocyc.CYANLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b0340|gene.b0340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00816`
- `KEGG:ecj:JW0331;eco:b0340;ecoc:C3026_01665;ecoc:C3026_24835;`
- `GeneID:948998;`
- `GO:GO:0003677; GO:0008824; GO:0009440`
- `EC:4.2.1.104`

## Notes

Cyanate hydratase (Cyanase) (EC 4.2.1.104) (Cyanate hydrolase) (Cyanate lyase)
