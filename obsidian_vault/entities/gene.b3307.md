---
entity_id: "gene.b3307"
entity_type: "gene"
name: "rpsN"
source_database: "NCBI RefSeq"
source_id: "gene-b3307"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3307"
  - "rpsN"
---

# rpsN

`gene.b3307`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3307`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsN (gene.b3307) is a gene entity. It encodes rpsN (protein.P0AG59). Encoded protein function: FUNCTION: Binds 16S rRNA, required for the assembly of 30S particles and may also be responsible for determining the conformation of the 16S rRNA at the A site. EcoCyc product frame: EG10913-MONOMER. Genomic coordinates: 3446579-3446884. EcoCyc protein note: The S14 protein is a component of the 30S subunit of the ribosome. S14 has a role in tRNA binding . S14 is photoaffinity labeled by streptomycin , puromycin, an analog of the 3' end of aminoacylated tRNA , and dihydrospiramycin . S14 may be required for in vitro assembly of the small subunit ; it assembles late in the biogenesis of the 30S subunit . S14 can be crosslinked to S19 and L7/L12 . A mixture containing S7, S14, and S19 protects the hairpin loop 41 near the 3' terminus of 16S rRNA against ribonuclease digestion . S14 can also be crosslinked to 16S rRNA and mRNA . The sites of interaction of S14 with 16S rRNA have been identified by hydroxyl radical probing . rpsN is part of the spc operon . An amber mutation in rpsN exerts a polar effect on the genes distal to the rpsN gene in the spc operon .

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG59|protein.P0AG59]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rpsN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010831,ECOCYC:EG10913,GeneID:947801`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3446579-3446884:-; feature_type=gene
