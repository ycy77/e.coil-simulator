---
entity_id: "protein.P69739"
entity_type: "protein"
name: "hyaA"
source_database: "UniProt"
source_id: "P69739"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type I membrane protein; Periplasmic side."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hyaA b0972 JW0954"
---

# hyaA

`protein.P69739`

## Static

- Type: `protein`
- Source: `UniProt:P69739`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type I membrane protein; Periplasmic side.

## Enriched Summary

FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD1 is believed to have a role in hydrogen cycling during fermentative growth. HyaA is the small subunit of hydrogenase 1. HyaA contains a distal [4Fe-4S]cluster, a medial [3Fe-4S] cluster and a unique proximal [4Fe-3S] cluster that is essential for oxygen tolerance (and see . The unique proximal [4Fe-3S] cluster is coordinated by six cysteine residues (at positions 17, 19, 20, 1115, 120 and 149 in the mature enzyme); the conserved cysteines at positions 19 and 120 correspond to glycine residues in standard oxygen-sensitive hydrogenases (hydrogenase 2 in E. coli K-12); a HyaA C19G mutation results in hydrogenase 1 enzyme that is devoid of H(2) oxidising activity in the presence of 1% oxygen . The reduction potential of the medial [3Fe-4S] cluster in oxygen tolerant hydrogenases is higher than in standard oxygen sensitive hydrogenases; a P242C mutation results in conversion of the [3Fe-4S] cluster to a [4Fe-4S] cluster and the modified enzyme is unable to sustain H(2) oxidation in the presence of 1% oxygen . Insertion of the C-terminal transmembrane domain of HyaA into the inner membrane is dependent on the Tat translocation system...

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

- `encodes` <-- [[gene.b0972|gene.b0972]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69739`
- `KEGG:ecj:JW0954;eco:b0972;ecoc:C3026_05935;`
- `GeneID:945579;`
- `GO:GO:0006113; GO:0008901; GO:0009055; GO:0009061; GO:0009267; GO:0009375; GO:0016020; GO:0019645; GO:0033748; GO:0044569; GO:0046872; GO:0051538; GO:0051539; GO:0098567; GO:1902421`
- `EC:1.12.99.6`

## Notes

Hydrogenase-1 small chain (HYD1) (EC 1.12.99.6) (Membrane-bound hydrogenase 1 small subunit) (NiFe hydrogenase)
