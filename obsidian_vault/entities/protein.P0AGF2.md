---
entity_id: "protein.P0AGF2"
entity_type: "protein"
name: "csdE"
source_database: "UniProt"
source_id: "P0AGF2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csdE ygdK b2811 JW2782"
---

# csdE

`protein.P0AGF2`

## Static

- Type: `protein`
- Source: `UniProt:P0AGF2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Stimulates the cysteine desulfurase activity of CsdA. Contains a cysteine residue (Cys-61) that acts to accept sulfur liberated via the desulfurase activity of CsdA. May be able to transfer sulfur to TcdA/CsdL. Seems to support the function of TcdA in the generation of cyclic threonylcarbamoyladenosine at position 37 (ct(6)A37) in tRNAs that read codons beginning with adenine. Does not appear to participate in Fe/S biogenesis. {ECO:0000269|PubMed:15901727, ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255}. CsdA and CsdE combine to form the CSD sulfur transfer system. CsdA activity doubles in the presence of CsdE, which contains a cysteine residue (C61) that acts to accept sulfur liberated via the desulfinase activity of CsdA . A physiologically relevant sulfur acceptor from CsdE has not been identified yet. CsdE also interacts with and may be able to transfer sulfur to TcdA ; a transient physical interaction between CsdE and TcdA was also shown by NMR and crosslinking experiments . Additional proteins that interact with CsdE have been identified . The pKa of the C61 residue was determined to be 6.5 . An NMR solution structure of CsdE has been solved . CsdE migrates as a dimer on a gel filtration column , but both the solution and crystal structures show it as a monomer...

## Biological Role

Component of sulfur acceptor protein CsdE (complex.ecocyc.CPLX0-7839).

## Annotation

FUNCTION: Stimulates the cysteine desulfurase activity of CsdA. Contains a cysteine residue (Cys-61) that acts to accept sulfur liberated via the desulfurase activity of CsdA. May be able to transfer sulfur to TcdA/CsdL. Seems to support the function of TcdA in the generation of cyclic threonylcarbamoyladenosine at position 37 (ct(6)A37) in tRNAs that read codons beginning with adenine. Does not appear to participate in Fe/S biogenesis. {ECO:0000269|PubMed:15901727, ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7839|complex.ecocyc.CPLX0-7839]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2811|gene.b2811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGF2`
- `KEGG:ecj:JW2782;eco:b2811;ecoc:C3026_15450;`
- `GeneID:75172895;947274;`
- `GO:GO:0008047; GO:0061504; GO:0097163; GO:1990228`

## Notes

Sulfur acceptor protein CsdE
