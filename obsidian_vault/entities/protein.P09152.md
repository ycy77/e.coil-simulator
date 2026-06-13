---
entity_id: "protein.P09152"
entity_type: "protein"
name: "narG"
source_database: "UniProt"
source_id: "P09152"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narG bisD narC b1224 JW1215"
---

# narG

`protein.P09152`

## Static

- Type: `protein`
- Source: `UniProt:P09152`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The alpha chain is the actual site of nitrate reduction. The α subunit of nitrate reductase A is the site of nitrate reduction; it contains the molybdenum cofactor CPD-15873 (bis-MGD and an FS0 CPD-7 [4Fe-4S] cluster . The assembly of FS0 in nitrate reductase A is a prerequisite for bis-MGD insertion . The enzyme-specific chaperone NARJ-MONOMER "NarJ" facilitates bis-MGD insertion within the apoenzyme complex; NarJ interacts specifically with NarG . NarG contains a vestigal twin-arginine leader sequence . NarG and NarH are significantly upregulated in a ΔCPLX0-245 Ahp strain compared to wild type and redox proteomics indicates that cysteine sites in peptides (NarGCys-292/NarHCys-217) are significantly reduced . nar: nitrate reductase; chl: chlorate resistant

## Biological Role

Component of nitrate reductase A (complex.ecocyc.NITRATREDUCTA-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The alpha chain is the actual site of nitrate reduction.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NITRATREDUCTA-CPLX|complex.ecocyc.NITRATREDUCTA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1224|gene.b1224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09152`
- `KEGG:ecj:JW1215;eco:b1224;ecoc:C3026_07200;`
- `GeneID:945782;`
- `GO:GO:0008940; GO:0009055; GO:0009061; GO:0016020; GO:0019645; GO:0042126; GO:0042128; GO:0043546; GO:0044799; GO:0046872; GO:0051539; GO:0160182`
- `EC:1.7.5.1`

## Notes

Respiratory nitrate reductase 1 alpha chain (EC 1.7.5.1) (Nitrate reductase A subunit alpha) (Quinol-nitrate oxidoreductase subunit alpha)
