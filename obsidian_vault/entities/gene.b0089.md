---
entity_id: "gene.b0089"
entity_type: "gene"
name: "ftsW"
source_database: "NCBI RefSeq"
source_id: "gene-b0089"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0089"
  - "ftsW"
---

# ftsW

`gene.b0089`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0089`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsW (gene.b0089) is a gene entity. It encodes ftsW (protein.P0ABG4). Encoded protein function: FUNCTION: Peptidoglycan polymerase that is essential for cell division (Probable). Functions probably in conjunction with the penicillin-binding protein 3 (ftsI) (PubMed:11807049, PubMed:9603865). Required for localization of FtsI (PubMed:11807049). {ECO:0000269|PubMed:11807049, ECO:0000269|PubMed:9603865, ECO:0000305|PubMed:27643381, ECO:0000305|PubMed:9218774}. EcoCyc product frame: EG10344-MONOMER. Genomic coordinates: 98403-99647. EcoCyc protein note: The SEDS family protein FtsW is is believed to be the primary peptidoglycan (PG) glycosyltransferase which functions together with its cognate transpeptidase EG10341-MONOMER "FtsI" (PBP3) to synthesize septal peptidoglycan (sPG) during cell division; FtsW-FtsI are the SEDS-bPBP pair of the divisome. The spatiotemporal coordination of sPG synthesis in E. coli is currently described by a 'two-track' model (see ). FtsW is an essential cell division protein that is conserved in most walled bacteria; the protein is produced at low levels and localizes to the septum . FtsW is an integral membrane protein belonging to the SEDS (shape, elongation, division, sporulation) family; it is predicted to consist of 10 transmembrane (TM) segments with both the N- and C-terminal end located in the cytoplasm...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABG4|protein.P0ABG4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ftsW; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ftsW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000320,ECOCYC:EG10344,GeneID:946322`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:98403-99647:+; feature_type=gene
