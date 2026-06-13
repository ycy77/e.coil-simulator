---
entity_id: "protein.P32176"
entity_type: "protein"
name: "fdoG"
source_database: "UniProt"
source_id: "P32176"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdoG b3894 JW3865"
---

# fdoG

`protein.P32176`

## Static

- Type: `protein`
- Source: `UniProt:P32176`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Allows to use formate as major electron donor during aerobic respiration. Subunit alpha possibly forms the active site. fdoG encodes the α subunit of formate dehydrogenase O. It has 75% amino acid identity with FDNG-MONOMER FdnG - the catalytic, molybdopterin cofactor containing α subunit of formate dehydrogenase-N. It contains an in-frame TGA (opal) codon that specifies selenocysteine . Topology analysis suggests that FdoG is located in the cytoplasm ; however, the use or reporter fusions to determine toplogy of Tat-dependent proteins has been brought into question .

## Biological Role

Catalyzes formate:NAD+ oxidoreductase (reaction.R00519). Component of formate dehydrogenase O (complex.ecocyc.CPLX0-13310), formate dehydrogenase O subcomplex (complex.ecocyc.FORMATEDEHYDROGO-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Allows to use formate as major electron donor during aerobic respiration. Subunit alpha possibly forms the active site.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00519|reaction.R00519]] `KEGG` `database` - via EC:1.17.1.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-13310|complex.ecocyc.CPLX0-13310]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.FORMATEDEHYDROGO-CPLX|complex.ecocyc.FORMATEDEHYDROGO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3894|gene.b3894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32176`
- `KEGG:ecj:JW3865;eco:b3894;`
- `GeneID:948394;`
- `GO:GO:0005829; GO:0005886; GO:0006788; GO:0006974; GO:0008863; GO:0009055; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0019645; GO:0036397; GO:0042597; GO:0043546; GO:0045333; GO:0046872; GO:0047111; GO:0051539`
- `EC:1.17.1.9`

## Notes

Formate dehydrogenase-O major subunit (EC 1.17.1.9) (Aerobic formate dehydrogenase major subunit) (FDH-Z subunit alpha) (Formate dehydrogenase-O subunit alpha)
