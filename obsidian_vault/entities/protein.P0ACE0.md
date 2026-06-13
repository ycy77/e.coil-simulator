---
entity_id: "protein.P0ACE0"
entity_type: "protein"
name: "hybC"
source_database: "UniProt"
source_id: "P0ACE0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hybC b2994 JW2962"
---

# hybC

`protein.P0ACE0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACE0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD2 is involved in hydrogen uptake. HybC is the large, [NiFe]-containing subunit of hydrogenase 2. The nickel and iron atoms are coordinated by 4 Cys thiolates plus 3 diatomic ligands (2 cyano and a carbonyl). Acquisition of a [NiFe] cofactor, C-terminal processing of HybC and subsequent association with the small subunit (HybO) are required prior to export by the Tat system (and reviewed in . The maturation of the HybC protein was affected in a hypA mutant and a hypA slyD double mutant .

## Biological Role

Component of hydrogenase 2 (complex.ecocyc.CPLX0-8762), hydrogenase 2 (complex.ecocyc.FORMHYDROG2-CPLX).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD2 is involved in hydrogen uptake.

## Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8762|complex.ecocyc.CPLX0-8762]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.FORMHYDROG2-CPLX|complex.ecocyc.FORMHYDROG2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2994|gene.b2994]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACE0`
- `KEGG:ecj:JW2962;eco:b2994;ecoc:C3026_16375;`
- `GeneID:75173127;75203605;945182;`
- `GO:GO:0005886; GO:0008901; GO:0016151; GO:0033748`
- `EC:1.12.99.6`

## Notes

Hydrogenase-2 large chain (HYD2) (EC 1.12.99.6) (Membrane-bound hydrogenase 2 large subunit) (NiFe hydrogenase)
