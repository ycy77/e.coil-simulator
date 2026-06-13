---
entity_id: "protein.P37672"
entity_type: "protein"
name: "dlgD"
source_database: "UniProt"
source_id: "P37672"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dlgD yiaK b3575 JW3547"
---

# dlgD

`protein.P37672`

## Static

- Type: `protein`
- Source: `UniProt:P37672`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of 2,3-diketo-L-gulonate in the presence of NADH, to form 3-keto-L-gulonate. {ECO:0000269|PubMed:11741871}. The yiaK gene encodes a 2,3-diketo-L-gulonate reductase . The enzyme is homodimeric in the crystal structure . A YiaK crystal structure is presented at 2.0 Å resolution, and a structure with NAD and tartrate is presented at 2.2 Å resolution. The His44 residue is predicted to be catalytic. YiaK shows an atypical interaction with NAD . A mutation causing consitutive yiaKLMNO-lyxK-sgbHUE operon expression results in induction of L-lyxose metabolic capability . Regulation has been described .

## Biological Role

Component of 2,3-diketo-L-gulonate reductase (complex.ecocyc.CPLX0-2061).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of 2,3-diketo-L-gulonate in the presence of NADH, to form 3-keto-L-gulonate. {ECO:0000269|PubMed:11741871}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2061|complex.ecocyc.CPLX0-2061]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3575|gene.b3575]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37672`
- `KEGG:ecj:JW3547;eco:b3575;ecoc:C3026_19385;`
- `GeneID:948096;`
- `GO:GO:0005737; GO:0016616; GO:0047559; GO:0070403`
- `EC:1.1.1.130`

## Notes

2,3-diketo-L-gulonate reductase (2,3-DKG reductase) (EC 1.1.1.130) (3-dehydro-L-gulonate 2-dehydrogenase)
