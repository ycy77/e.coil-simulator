---
entity_id: "protein.P08178"
entity_type: "protein"
name: "purM"
source_database: "UniProt"
source_id: "P08178"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purM purG b2499 JW2484"
---

# purM

`protein.P08178`

## Static

- Type: `protein`
- Source: `UniProt:P08178`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Phosphoribosylformylglycinamidine cyclo-ligase (EC 6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthetase)

## Biological Role

Component of phosphoribosylformylglycinamide cyclo-ligase (complex.ecocyc.AIRS-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

Phosphoribosylformylglycinamidine cyclo-ligase (EC 6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthetase)

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.AIRS-CPLX|complex.ecocyc.AIRS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2499|gene.b2499]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08178`
- `KEGG:ecj:JW2484;eco:b2499;ecoc:C3026_13860;`
- `GeneID:946975;`
- `GO:GO:0004637; GO:0004641; GO:0005524; GO:0005829; GO:0006164; GO:0006189; GO:0046084`
- `EC:6.3.3.1`

## Notes

Phosphoribosylformylglycinamidine cyclo-ligase (EC 6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthetase)
