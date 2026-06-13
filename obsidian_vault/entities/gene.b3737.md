---
entity_id: "gene.b3737"
entity_type: "gene"
name: "atpE"
source_database: "NCBI RefSeq"
source_id: "gene-b3737"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3737"
  - "atpE"
---

# atpE

`gene.b3737`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3737`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpE (gene.b3737) is a gene entity. It encodes atpE (protein.P68699). Encoded protein function: FUNCTION: F(1)F(0) ATP synthase produces ATP from ADP in the presence of a proton or sodium gradient. F-type ATPases consist of two structural domains, F(1) containing the extramembraneous catalytic core and F(0) containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain of F(1) is coupled via a rotary mechanism of the central stalk subunits to proton translocation.; FUNCTION: Key component of the F(0) channel; it plays a direct role in translocation across the membrane. A homomeric c-ring of 10 subunits forms the central stalk rotor element with the F(1) delta and epsilon subunits. EcoCyc product frame: ATPE-MONOMER. EcoCyc synonyms: papH, uncE. Genomic coordinates: 3920950-3921189. EcoCyc protein note: The c subunit of the Fo complex of ATP synthase is absolutely required for proton translocation and is also necessary for binding of the F1 complex. The number of subunit c monomers determines the number of transported ions per revolution. The stoichiometry of the subunits has been obtained within the range of 9 to 18 ; the preferred number of c subunits is 10...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68699|protein.P68699]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012220,ECOCYC:EG10102,GeneID:948253`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3920950-3921189:-; feature_type=gene
