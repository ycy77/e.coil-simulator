---
entity_id: "protein.P31663"
entity_type: "protein"
name: "panC"
source_database: "UniProt"
source_id: "P31663"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "panC b0133 JW0129"
---

# panC

`protein.P31663`

## Static

- Type: `protein`
- Source: `UniProt:P31663`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the condensation of pantoate with beta-alanine in an ATP-dependent reaction via a pantoyl-adenylate intermediate. {ECO:0000269|PubMed:357689}. Pantothenate synthetase (PanC) catalyzes the ATP hydrolysis-dependent synthesis of pantothenate from β-alanine and pantoate . The enzyme from strains W or B requires both monovalent and divalent cations . The pantothenate:β-alanine exchange reaction depends on the presence of AMP, which supports the two-step Bi Uni Uni Bi reaction mechanism with pantoyl adenylate as the reaction intermediate . Crystal structures of the full length enzyme and its N-terminal domain have been solved. Pantothenate synthetase is dimeric both in solution and the crystal structure. It is a member of the cytidylyltransferase superfamily, with an N-terminal Rossmann fold domain containing the active site and a C-terminal domain that forms a hinged lid . The substrate pantoate is able to bind within the ATP-binding pocket of the N-terminal domain . Molecular dynamics simulations suggest that motions of the C-terminal domain dominate the functional dynamics of the E. coli enzyme . panC mutants are auxotrophic for pantothenate . Various inhibitors of pantothenate synthetase have been tested . PanC: "pantothenate"

## Biological Role

Component of pantothenate synthetase (complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX).

## Enriched Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of pantoate with beta-alanine in an ATP-dependent reaction via a pantoyl-adenylate intermediate. {ECO:0000269|PubMed:357689}.

## Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX|complex.ecocyc.PANTOATE-BETA-ALANINE-LIG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0133|gene.b0133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31663`
- `KEGG:ecj:JW0129;eco:b0133;ecoc:C3026_00570;`
- `GeneID:75202052;944958;`
- `GO:GO:0004592; GO:0005524; GO:0005829; GO:0015940; GO:0042802; GO:0042803`
- `EC:6.3.2.1`

## Notes

Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme)
