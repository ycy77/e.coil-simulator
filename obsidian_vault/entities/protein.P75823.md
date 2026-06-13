---
entity_id: "protein.P75823"
entity_type: "protein"
name: "ltaE"
source_database: "UniProt"
source_id: "P75823"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ltaE ybjU b0870 JW0854"
---

# ltaE

`protein.P75823`

## Static

- Type: `protein`
- Source: `UniProt:P75823`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the cleavage of L-allo-threonine and L-threonine to glycine and acetaldehyde. L-threo-phenylserine and L-erythro-phenylserine are also good substrates. The low-specificity L-threonine aldolase (LtaE) can act on both L-threonine and L-allo-threonine as well as L-threo-phenylserine and L-erythro-phenylserine, but does not utilize the D isomers. The enzyme requires pyridoxal phosphate as a cofactor. L-threonine aldolase may serve in an alternative pathway for glycine biosynthesis when the major pathway is disrupted by a mutation in glyA . LtaE was found to be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 4-PHOSPHONOOXY-THREONINE, that lies downstream of PdxB. The pathway diverts 3-phosphohydroxypyruvate from serine biosynthesis. Here, LtaE catalyzes the aldol condensation of glycolaldehyde and glycine to form 4-hydroxy-L-threonine . An ltaE mutant has no growth defect when grown on glucose as the sole source of carbon . LtaE: "low-specificity L-threonine aldolase"

## Biological Role

Catalyzes L-threonine acetaldehyde-lyase (glycine-forming) (reaction.R00751), L-allo-threonine acetaldehyde-lyase (glycine-forming) (reaction.R06171). Component of low-specificity L-threonine aldolase (complex.ecocyc.LTAA-CPLX).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the cleavage of L-allo-threonine and L-threonine to glycine and acetaldehyde. L-threo-phenylserine and L-erythro-phenylserine are also good substrates.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00751|reaction.R00751]] `KEGG` `database` - via EC:4.1.2.48
- `catalyzes` --> [[reaction.R06171|reaction.R06171]] `KEGG` `database` - via EC:4.1.2.48
- `is_component_of` --> [[complex.ecocyc.LTAA-CPLX|complex.ecocyc.LTAA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0870|gene.b0870]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75823`
- `KEGG:ecj:JW0854;eco:b0870;ecoc:C3026_05410;`
- `GeneID:944955;`
- `GO:GO:0005829; GO:0006545; GO:0006567; GO:0008732; GO:0030170; GO:0042802; GO:0050179`
- `EC:4.1.2.48`

## Notes

Low specificity L-threonine aldolase (Low specificity L-TA) (EC 4.1.2.48)
