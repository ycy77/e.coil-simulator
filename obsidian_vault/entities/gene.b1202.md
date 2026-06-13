---
entity_id: "gene.b1202"
entity_type: "gene"
name: "ycgV"
source_database: "NCBI RefSeq"
source_id: "gene-b1202"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1202"
  - "ycgV"
---

# ycgV

`gene.b1202`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1202`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycgV (gene.b1202) is a gene entity. It encodes ycgV (protein.P76017). Encoded protein function: FUNCTION: Upon overexpression shows increased adherence to polyvinyl chloride (PVC) plates, increased mature biofilm formation (PubMed:15659678). {ECO:0000269|PubMed:15659678}. EcoCyc product frame: G6629-MONOMER. Genomic coordinates: 1253085-1255952. EcoCyc protein note: ycgV has homology with G7080 "flu" - encoding the autotransporter (AT) self-recognizing adhesin Ag43; deletion of ycgV has no significant effect on adhesion properties in microtiter plate assays or on biofilm formation however increased expression of ycgV results in increased adhesion and increased biofilm formation compared to the wild-type; overexpression of ycgV promotes bacterial adhesion to microtiter PVC plates to a greater level than overexpression of flu . YcgV is predicted to be an outer membrane protein and a member of the Autotransporter (AT) family .

## Biological Role

Repressed by glaR (protein.P37338). Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76017|protein.P76017]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ycgV; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=ycgV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004035,ECOCYC:G6629,GeneID:945767`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1253085-1255952:-; feature_type=gene
