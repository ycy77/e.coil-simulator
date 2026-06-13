---
entity_id: "protein.P0A996"
entity_type: "protein"
name: "glpC"
source_database: "UniProt"
source_id: "P0A996"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Note=Loosely bound to the cytoplasmic membrane often occurring in vesicles associated with fumarate reductase."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpC b2243 JW2237"
---

# glpC

`protein.P0A996`

## Static

- Type: `protein`
- Source: `UniProt:P0A996`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein. Note=Loosely bound to the cytoplasmic membrane often occurring in vesicles associated with fumarate reductase.

## Enriched Summary

FUNCTION: Electron transfer protein; may also function as the membrane anchor for the GlpAB dimer. GlpC is the membrane associated subunit of the heterotrimeric glycerol-3-phosphate dehydrogenase complex. In anaerobic conditions this respiratory enzyme converts glycerol-3-phosphate to dihydroxyacetone phosphate (DHAP) using fumarate a a terminal electron acceptor. Overexpressed GlpC associates with the inner membrane . GlpC contains two cysteine clusters typical of iron-sulfur binding domains . uses the name GlpB for the protein encoded by the third gene in the glp operon.

## Biological Role

Component of anaerobic glycerol-3-phosphate dehydrogenase (complex.ecocyc.ANGLYC3PDEHYDROG-CPLX).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Electron transfer protein; may also function as the membrane anchor for the GlpAB dimer.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ANGLYC3PDEHYDROG-CPLX|complex.ecocyc.ANGLYC3PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2243|gene.b2243]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A996`
- `KEGG:ecj:JW2237;eco:b2243;ecoc:C3026_12530;`
- `GeneID:75172373;946735;`
- `GO:GO:0004368; GO:0005886; GO:0009061; GO:0009331; GO:0019563; GO:0022900; GO:0046168; GO:0046872; GO:0051536; GO:0051539`

## Notes

Anaerobic glycerol-3-phosphate dehydrogenase subunit C (G-3-P dehydrogenase)
