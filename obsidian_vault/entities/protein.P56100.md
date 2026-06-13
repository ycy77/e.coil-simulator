---
entity_id: "protein.P56100"
entity_type: "protein"
name: "cydX"
source_database: "UniProt"
source_id: "P56100"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=In sucrose cushions fractionates with both the inner and outer membranes. {ECO:0000269|PubMed:19121005, ECO:0000269|PubMed:21778229}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cydX ybgT b4515 JW0724"
---

# cydX

`protein.P56100`

## Static

- Type: `protein`
- Source: `UniProt:P56100`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Note=In sucrose cushions fractionates with both the inner and outer membranes. {ECO:0000269|PubMed:19121005, ECO:0000269|PubMed:21778229}.

## Enriched Summary

FUNCTION: Required for correct functioning of cytochrome bd-I oxidase. This protein and AppX may have some functional overlap. CydX is small, noncatalytic, single transmembrane, accessory subunit of CYT-D-UBIOX-CPLX . A strain lacking cydX is slow growing in aerobic liquid culture and on plates and has increased sensitivity to β-mercaptoethanol; a wild-type phenotype can be restored when cydX is expressed from a plasmid . Membrane extracts from a strain lacking cydX display reduced levels of N N N' N'-tetramethyl-p-phenylenediamine (TMPD) oxidation . Preparations of CydAB lacking CydX do not contain the di-heme centre (hemes b595 and d) suggesting that CydX may be involved in the assembly or stabilisation of the di-heme active centre (further ). The cydX open reading frame contains a predicted transmembrane segment, and the protein can be found in the membrane fraction . Using a sucrose fractionation protocol CydX partitions into both the inner membrane and outer membrane fractions . Topology assays using GFP and PhoA fusion proteins suggest that CydX is oriented with the C-terminus in the cytoplasm . Translocation of CydX is impaired in both SecE depleted and YidC depleted E. coli strains . CydX is highly expressed during both exponential and stationary phase...

## Biological Role

Component of cytochrome bd-I ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-D-UBIOX-CPLX).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Required for correct functioning of cytochrome bd-I oxidase. This protein and AppX may have some functional overlap.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CYT-D-UBIOX-CPLX|complex.ecocyc.CYT-D-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4515|gene.b4515]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P56100`
- `KEGG:ecj:JW0724;eco:b4515;ecoc:C3026_03685;`
- `GeneID:1450246;89520040;93776750;`
- `GO:GO:0005886; GO:0006119; GO:0016020; GO:0016679; GO:0019646; GO:0019867; GO:0070069`
- `EC:7.1.1.7`

## Notes

Cytochrome bd-I ubiquinol oxidase subunit X (EC 7.1.1.7) (Cytochrome bd-I oxidase subunit X) (Cytochrome d ubiquinol oxidase subunit X)
