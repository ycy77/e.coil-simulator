---
entity_id: "protein.P04128"
entity_type: "protein"
name: "fimA"
source_database: "UniProt"
source_id: "P04128"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Fimbrium."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fimA pilA b4314 JW4277"
---

# fimA

`protein.P04128`

## Static

- Type: `protein`
- Source: `UniProt:P04128`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Fimbrium.

## Enriched Summary

FUNCTION: Fimbriae (also called pili), polar filaments radiating from the surface of the bacterium to a length of 0.5-1.5 micrometers and numbering 100-300 per cell, enable bacteria to colonize the epithelium of specific host organs. FimA, the major subunit of the Escherichia coli type 1 fimbriae (pili), has been identified and its gene sequence determined . A typical pilus is composed of around 1,000 subunits of FimA which form a right-handed helical rod connected to a short tip fibrillum composed of the adaptor proteins FimG and FimF, and the adhesin FimH attached at its distal end . The fimA promoter is contained within fimS, the fim switch, which controls transcription of fimA and the genes for the other fimbrial structural proteins by undergoing a site-specific inversion . Monomeric FimA is the dominant protein in K-12 MG1655 outer membrane vesicles (OMVs); disruption of fimbrial assembly alters OMV cargo . Deletion of fimA impairs pili-dependent surface motility (PDSM) in E. coli strain W3110 . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including fimAICDFGH; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Component of fimbrial complex (complex.ecocyc.CPLX0-3401).

## Annotation

FUNCTION: Fimbriae (also called pili), polar filaments radiating from the surface of the bacterium to a length of 0.5-1.5 micrometers and numbering 100-300 per cell, enable bacteria to colonize the epithelium of specific host organs.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3401|complex.ecocyc.CPLX0-3401]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4314|gene.b4314]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04128`
- `KEGG:ecj:JW4277;eco:b4314;ecoc:C3026_23305;`
- `GeneID:948838;`
- `GO:GO:0007155; GO:0009289; GO:0042802; GO:0043709`

## Notes

Type-1 fimbrial protein, A chain (Type-1A pilin)
