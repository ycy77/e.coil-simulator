---
entity_id: "gene.b3503"
entity_type: "gene"
name: "arsC"
source_database: "NCBI RefSeq"
source_id: "gene-b3503"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3503"
  - "arsC"
---

# arsC

`gene.b3503`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3503`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arsC (gene.b3503) is a gene entity. It encodes arsC (protein.P0AB96). Encoded protein function: FUNCTION: Involved in resistance to arsenate. Catalyzes the reduction of arsenate [As(V)] to arsenite [As(III)]. {ECO:0000250|UniProtKB:P08692}. EcoCyc product frame: EG12237-MONOMER. EcoCyc synonyms: arsG. Genomic coordinates: 3650237-3650662. EcoCyc protein note: Based on sequence similarity with the R773-encoded enzyme, ArsC is thought to catalyze the reduction of arsenate to arsenite using glutathione with glutaredoxin as electron donors. The resulting arsenite is then removed from the cell via the ArsB transport protein. Unlike the chromosomally-encoded ArsC described here, the R773 plasmid-encoded enzyme has been studied experimentally. The arsenate reductase reaction involves sequential action of three different thiolate nucleophiles that function as a redox cascade . All three glutaredoxins in E. coli can participate in the arsenate reductase reaction, but glutaredoxin 2 appears the most effective . Crystal structures of ArsC have been solved , and residues involved in arsenate binding and transition-state stabilization were identified . Based on sequence similarity with the R773-plasmid encoded arsenite resistance operon, ArsB is a transporter and ArsC is an arsenate reductase...

## Biological Role

Repressed by arsR (protein.P37309). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB96|protein.P0AB96]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=arsC; function=+
- `represses` <-- [[protein.P37309|protein.P37309]] `RegulonDB` `S` - regulator=ArsR; target=arsC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011439,ECOCYC:EG12237,GeneID:948018`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3650237-3650662:+; feature_type=gene
