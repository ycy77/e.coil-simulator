---
entity_id: "protein.P37180"
entity_type: "protein"
name: "hybB"
source_database: "UniProt"
source_id: "P37180"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hybB b2995 JW5494"
---

# hybB

`protein.P37180`

## Static

- Type: `protein`
- Source: `UniProt:P37180`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Probable b-type cytochrome. The HybB protein is predicted to be an integral membrane component of hydrogenase 2 . hybB contains a HXXH conserved motif associated with cytochrome b type proteins . HybB contains no conserved histidines that would serve as heme iron ligands . HybB may act as a proton pump during H(2):quinone oxidoreductase activity (and see ). A hybB in-frame deletion mutant cannot grow on glycerol and fumarate as the sole energy sources. However, the HybOHybC complex is correctly targeted to the membrane and active with the artificial electron acceptor benzyl viologen (BV) .

## Biological Role

Component of hydrogenase 2 (complex.ecocyc.CPLX0-8762), hydrogenase 2 (complex.ecocyc.FORMHYDROG2-CPLX).

## Annotation

FUNCTION: Probable b-type cytochrome.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8762|complex.ecocyc.CPLX0-8762]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.FORMHYDROG2-CPLX|complex.ecocyc.FORMHYDROG2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2995|gene.b2995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37180`
- `KEGG:ecj:JW5494;eco:b2995;ecoc:C3026_16380;`
- `GeneID:948615;`
- `GO:GO:0005886; GO:0009061; GO:0019645; GO:0044569; GO:0046872`

## Notes

Probable Ni/Fe-hydrogenase 2 b-type cytochrome subunit
