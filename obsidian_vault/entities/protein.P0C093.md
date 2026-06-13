---
entity_id: "protein.P0C093"
entity_type: "protein"
name: "slmA"
source_database: "UniProt"
source_id: "P0C093"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000255|HAMAP-Rule:MF_01839, ECO:0000269|PubMed:15916962}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "slmA ttk yicB b3641 JW5641"
---

# slmA

`protein.P0C093`

## Static

- Type: `protein`
- Source: `UniProt:P0C093`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000255|HAMAP-Rule:MF_01839, ECO:0000269|PubMed:15916962}.

## Enriched Summary

FUNCTION: Required for nucleoid occlusion (NO) phenomenon, which prevents Z-ring formation and cell division over the nucleoid. Acts as a DNA-associated cell division inhibitor that binds simultaneously chromosomal DNA and FtsZ, and disrupts the assembly of FtsZ polymers. SlmA-DNA-binding sequences (SBS) are dispersed on non-Ter regions of the chromosome, preventing FtsZ polymerization at these regions. {ECO:0000255|HAMAP-Rule:MF_01839, ECO:0000269|PubMed:15916962, ECO:0000269|PubMed:21113127, ECO:0000269|PubMed:21321206}.

## Biological Role

Component of nucleoid occlusion factor SlmA (complex.ecocyc.CPLX0-7922).

## Annotation

FUNCTION: Required for nucleoid occlusion (NO) phenomenon, which prevents Z-ring formation and cell division over the nucleoid. Acts as a DNA-associated cell division inhibitor that binds simultaneously chromosomal DNA and FtsZ, and disrupts the assembly of FtsZ polymers. SlmA-DNA-binding sequences (SBS) are dispersed on non-Ter regions of the chromosome, preventing FtsZ polymerization at these regions. {ECO:0000255|HAMAP-Rule:MF_01839, ECO:0000269|PubMed:15916962, ECO:0000269|PubMed:21113127, ECO:0000269|PubMed:21321206}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7922|complex.ecocyc.CPLX0-7922]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3641|gene.b3641]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C093`
- `KEGG:ecj:JW5641;eco:b3641;ecoc:C3026_19730;`
- `GeneID:93778356;948158;`
- `GO:GO:0000918; GO:0000976; GO:0003677; GO:0003700; GO:0005737; GO:0006355; GO:0010974; GO:0032272; GO:0042802; GO:0042803; GO:0043565; GO:0043590`

## Notes

Nucleoid occlusion factor SlmA (Protein Ttk) (Synthetically lethal with a defective Min system protein A)
