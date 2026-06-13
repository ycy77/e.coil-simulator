---
entity_id: "protein.P08190"
entity_type: "protein"
name: "fimG"
source_database: "UniProt"
source_id: "P08190"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Fimbrium."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fimG b4319 JW4282"
---

# fimG

`protein.P08190`

## Static

- Type: `protein`
- Source: `UniProt:P08190`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Fimbrium.

## Enriched Summary

FUNCTION: Involved in regulation of length and mediation of adhesion of type 1 fimbriae (but not necessary for the production of fimbriae). Involved in the integration of FimH in the fimbriae. FimG is a minor component of the type 1 fimbriae in Escherichia coli. Two-dimensional gel electrophoresis indicated that FimG has a molecular weight of 17.0 kDa and exists in a 1:100 ratio with the major fimbrial subunit, FimA . FimF and FimG are subunits of the tip fibrillum which are thought to function as adaptor proteins, linking the helical rod composed of FimA subunits to the the adhesin FimH at the tip of the fibrillum . Transcription of fimG is induced upon biofilm formation . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including fimAICDFGH; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Component of fimbrial complex (complex.ecocyc.CPLX0-3401).

## Annotation

FUNCTION: Involved in regulation of length and mediation of adhesion of type 1 fimbriae (but not necessary for the production of fimbriae). Involved in the integration of FimH in the fimbriae.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3401|complex.ecocyc.CPLX0-3401]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4319|gene.b4319]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08190`
- `KEGG:ecj:JW4282;eco:b4319;ecoc:C3026_23330;`
- `GeneID:948846;`
- `GO:GO:0007155; GO:0007638; GO:0009289; GO:0009419; GO:0031589; GO:0043709`

## Notes

Protein FimG
