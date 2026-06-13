---
entity_id: "protein.P0AAM1"
entity_type: "protein"
name: "hyaC"
source_database: "UniProt"
source_id: "P0AAM1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyaC b0974 JW0956"
---

# hyaC

`protein.P0AAM1`

## Static

- Type: `protein`
- Source: `UniProt:P0AAM1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Probable b-type cytochrome. The hyaC gene product is very hydrophobic, rich in aromatic residues, and has four putative hydrophobic membrane-spanning regions . An in-frame deletion in the hyaC gene results in wild-type levels of hydrogenase 1 activity and the appearance of multiple forms of the enzyme during purification . Sequence analysis suggests that the HyaC subunit contains two heme groups but only one heme could be identified in the crystal structure of the hydrogenase 1 complex; HyaC's main function may be anchoring the hydrogenase to the membrane . Overexpression of hyaC from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid .

## Biological Role

Component of hydrogenase 1, oxygen tolerant hydrogenase (complex.ecocyc.CPLX0-8167), hydrogenase 1 (complex.ecocyc.FORMHYDROGI-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Probable b-type cytochrome.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8167|complex.ecocyc.CPLX0-8167]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.FORMHYDROGI-CPLX|complex.ecocyc.FORMHYDROGI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0974|gene.b0974]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAM1`
- `KEGG:ecj:JW0956;eco:b0974;ecoc:C3026_05945;`
- `GeneID:75171048;945581;`
- `GO:GO:0005506; GO:0005886; GO:0006113; GO:0009055; GO:0009061; GO:0009267; GO:0019645; GO:0020037; GO:0033748; GO:0044569; GO:0098567; GO:1902421`

## Notes

Probable Ni/Fe-hydrogenase 1 B-type cytochrome subunit
