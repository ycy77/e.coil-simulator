---
entity_id: "protein.P11349"
entity_type: "protein"
name: "narH"
source_database: "UniProt"
source_id: "P11349"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narH b1225 JW1216"
---

# narH

`protein.P11349`

## Static

- Type: `protein`
- Source: `UniProt:P11349`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The beta chain is an electron transfer unit containing four cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit. The β subunit (NarH) of nitrate reductase A contains 4 iron-sulfur clusters - one [3Fe-4S] cluster (FS4) and three [4Fe-4S] clusters (FS1, FS2 and FS3) . FS1, FS2 and FS3 are coordinated by 4 cysteine residues and FS4 is coordinated by 3 cysteine residues (reviewed by . NarH and NarG are significantly upregulated in a ΔCPLX0-245 Ahp strain compared to wild type and redox proteomics indicates that cysteine sites in peptides (NarHCys-217/NarGCys-292) are significantly reduced . nar: nitrate reductase; chl: chlorate resistant

## Biological Role

Component of nitrate reductase A (complex.ecocyc.NITRATREDUCTA-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The beta chain is an electron transfer unit containing four cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NITRATREDUCTA-CPLX|complex.ecocyc.NITRATREDUCTA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1225|gene.b1225]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11349`
- `KEGG:ecj:JW1216;eco:b1225;ecoc:C3026_07205;`
- `GeneID:75057227;945780;`
- `GO:GO:0008940; GO:0009055; GO:0009061; GO:0016020; GO:0019645; GO:0042126; GO:0042128; GO:0044799; GO:0046872; GO:0051538; GO:0051539; GO:0160182`
- `EC:1.7.5.1`

## Notes

Respiratory nitrate reductase 1 beta chain (EC 1.7.5.1) (Nitrate reductase A subunit beta) (Quinol-nitrate oxidoreductase subunit beta)
