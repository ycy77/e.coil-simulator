---
entity_id: "protein.P0AFP6"
entity_type: "protein"
name: "ybgI"
source_database: "UniProt"
source_id: "P0AFP6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybgI b0710 JW0700"
---

# ybgI

`protein.P0AFP6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFP6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Provides significant protection from radiation damage and may be involved in the degradation of radiation-damaged nucleotides. {ECO:0000269|PubMed:25049088}. YbgI is proposed to be a hydrolase-oxidase. YbgI has structural similarity to proteins with DNA-related functions . A recent study of the DUF34 protein family suggests that the proteins may function as metal ion insertases, chaperones, or metallocofactor maturases rather than GTP cyclohydrolases . YbgI localizes to the cell poles . Crystal structures of YbgI have been solved at 2.2 Å resolution. YbgI forms a toroidal complex comprising three sets of homodimers, with metal ions (two per monomer) coordinated within the ring . ybgI insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A ybgI deletion mutant has a substantial decrease in IR survival , but does not appear to have increased sensitivity to UV damage; it is more sensitive to fosfomycin, carbenicillin, vancomycin, and amoxicillin . A proteomics experiment comparing wild type and the ΔybgI mutant grown on M9 minimal medium showed upregulation of TnaA and AphA and downregulation of YgiW, YgaU, Dps, and OsmY protein levels .

## Biological Role

Component of radiation resistance protein YbgI (complex.ecocyc.CPLX0-1863).

## Annotation

FUNCTION: Provides significant protection from radiation damage and may be involved in the degradation of radiation-damaged nucleotides. {ECO:0000269|PubMed:25049088}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1863|complex.ecocyc.CPLX0-1863]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0710|gene.b0710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFP6`
- `KEGG:ecj:JW0700;eco:b0710;ecoc:C3026_03550;`
- `GeneID:75170699;75205542;945824;`
- `GO:GO:0005737; GO:0005829; GO:0006281; GO:0010212; GO:0034214; GO:0042802; GO:0046872; GO:0060187`

## Notes

GTP cyclohydrolase 1 type 2 homolog (Radiation resistance protein YbgI)
