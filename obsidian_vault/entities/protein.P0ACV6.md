---
entity_id: "protein.P0ACV6"
entity_type: "protein"
name: "mpaA"
source_database: "UniProt"
source_id: "P0ACV6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02211, ECO:0000305|PubMed:12511517}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mpaA ycjI b1326 JW1319"
---

# mpaA

`protein.P0ACV6`

## Static

- Type: `protein`
- Source: `UniProt:P0ACV6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02211, ECO:0000305|PubMed:12511517}.

## Enriched Summary

FUNCTION: Involved in muropeptide degradation. Catalyzes the hydrolysis of the gamma-D-glutamyl-diaminopimelic acid (gamma-D-Glu-Dap) amide bond in the murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelic acid, leading to the formation of L-Ala-gamma-D-Glu and Dap (PubMed:12511517, PubMed:22970852). Has weak activity with L-Ala-gamma-D-Glu-L-Lys, MurNAc-tripeptide and gamma-D-Glu-meso-Dap (PubMed:22970852). Cannot hydrolyze murein tetrapeptide (PubMed:22970852). {ECO:0000269|PubMed:12511517, ECO:0000269|PubMed:22970852}.

## Biological Role

Component of murein tripeptide amidase A (complex.ecocyc.CPLX0-7989).

## Annotation

FUNCTION: Involved in muropeptide degradation. Catalyzes the hydrolysis of the gamma-D-glutamyl-diaminopimelic acid (gamma-D-Glu-Dap) amide bond in the murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelic acid, leading to the formation of L-Ala-gamma-D-Glu and Dap (PubMed:12511517, PubMed:22970852). Has weak activity with L-Ala-gamma-D-Glu-L-Lys, MurNAc-tripeptide and gamma-D-Glu-meso-Dap (PubMed:22970852). Cannot hydrolyze murein tetrapeptide (PubMed:22970852). {ECO:0000269|PubMed:12511517, ECO:0000269|PubMed:22970852}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7989|complex.ecocyc.CPLX0-7989]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1326|gene.b1326]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACV6`
- `KEGG:ecj:JW1319;eco:b1326;ecoc:C3026_07760;`
- `GeneID:93775454;945969;`
- `GO:GO:0004040; GO:0005737; GO:0006508; GO:0008270; GO:0009050; GO:0009253; GO:0016998; GO:0042803; GO:0061473; GO:0071555`
- `EC:3.4.17.-`

## Notes

Murein peptide amidase A (EC 3.4.17.-) (Gamma-D-Glu-Dap amidase) (Zinc metallocarboxypeptidase MpaA)
