---
entity_id: "protein.P75682"
entity_type: "protein"
name: "yagE"
source_database: "UniProt"
source_id: "P75682"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yagE b0268 JW0261"
---

# yagE

`protein.P75682`

## Static

- Type: `protein`
- Source: `UniProt:P75682`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the formation of 2-keto-3-deoxy-gluconate (KDG) from pyruvate and glyceraldehyde (PubMed:21294156). May also function as a 2-dehydro-3-deoxy-D-pentonate aldolase (PubMed:23233208). Overexpression leads to increased growth (over 2 hours) in the presence of the antibiotics norfloxacin, ampicillin and streptomycin (PubMed:21294156). {ECO:0000269|PubMed:21294156, ECO:0000305|PubMed:23233208}.

## Biological Role

Component of CP4-6 prophage; 2-dehydro-3-deoxygluconate aldolase (complex.ecocyc.CPLX0-7940).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of 2-keto-3-deoxy-gluconate (KDG) from pyruvate and glyceraldehyde (PubMed:21294156). May also function as a 2-dehydro-3-deoxy-D-pentonate aldolase (PubMed:23233208). Overexpression leads to increased growth (over 2 hours) in the presence of the antibiotics norfloxacin, ampicillin and streptomycin (PubMed:21294156). {ECO:0000269|PubMed:21294156, ECO:0000305|PubMed:23233208}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7940|complex.ecocyc.CPLX0-7940]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0268|gene.b0268]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75682`
- `KEGG:ecj:JW0261;eco:b0268;ecoc:C3026_01300;`
- `GeneID:944925;`
- `GO:GO:0005829; GO:0042802; GO:0046176; GO:0047440; GO:0061677`
- `EC:4.1.2.28; 4.1.2.51`

## Notes

Putative 2-dehydro-3-deoxy-D-gluconate aldolase YagE (KDG aldolase YagE) (EC 4.1.2.51) (Putative 2-dehydro-3-deoxy-D-pentonate aldolase YagE) (EC 4.1.2.28)
