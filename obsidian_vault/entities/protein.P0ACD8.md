---
entity_id: "protein.P0ACD8"
entity_type: "protein"
name: "hyaB"
source_database: "UniProt"
source_id: "P0ACD8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyaB b0973 JW0955"
---

# hyaB

`protein.P0ACD8`

## Static

- Type: `protein`
- Source: `UniProt:P0ACD8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD1 is believed to have a role in hydrogen cycling during fermentative growth. HyaB is the large subunit of hydrogenase 1 and contains the Ni-Fe active site. The nickel and iron atoms are coordinated by 4 Cys thiolates plus 3 diatomic ligands (2 cyano and a carbonyl). Acquisition of the [NiFe] cofactor, C-terminal processing of HyaB and subsequent association with the small subunit (HyaA) are required prior to export by the Tat system (and reviewed in . A hyaB in-frame deletion mutant does not have a defect in anaerobic growth with hydrogen and fumarate as sole energy and carbon sources; a hyaB hybC double mutant does not grow under these conditions .

## Biological Role

Component of hydrogenase 1, oxygen tolerant hydrogenase (complex.ecocyc.CPLX0-8167), hydrogenase 1 (complex.ecocyc.FORMHYDROGI-CPLX).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD1 is believed to have a role in hydrogen cycling during fermentative growth.

## Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8167|complex.ecocyc.CPLX0-8167]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.FORMHYDROGI-CPLX|complex.ecocyc.FORMHYDROGI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0973|gene.b0973]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACD8`
- `KEGG:ecj:JW0955;eco:b0973;ecoc:C3026_05940;`
- `GeneID:945580;`
- `GO:GO:0006113; GO:0008901; GO:0009055; GO:0009061; GO:0009267; GO:0016020; GO:0016151; GO:0019645; GO:0030288; GO:0033748; GO:0044569; GO:0098567; GO:1902421`
- `EC:1.12.99.6`

## Notes

Hydrogenase-1 large chain (HYD1) (EC 1.12.99.6) (Membrane-bound hydrogenase 1 large subunit) (NiFe hydrogenase)
