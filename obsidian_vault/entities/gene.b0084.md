---
entity_id: "gene.b0084"
entity_type: "gene"
name: "ftsI"
source_database: "NCBI RefSeq"
source_id: "gene-b0084"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0084"
  - "ftsI"
---

# ftsI

`gene.b0084`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0084`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsI (gene.b0084) is a gene entity. It encodes ftsI (protein.P0AD68). Encoded protein function: FUNCTION: Essential cell division protein that catalyzes cross-linking of the peptidoglycan cell wall at the division septum (PubMed:1103132, PubMed:3531167, PubMed:6450748, PubMed:7030331, PubMed:9614966). Required for localization of FtsN (PubMed:9282742). {ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:3531167, ECO:0000269|PubMed:6450748, ECO:0000269|PubMed:7030331, ECO:0000269|PubMed:9282742, ECO:0000269|PubMed:9614966}. EcoCyc product frame: EG10341-MONOMER. EcoCyc synonyms: pbpB, sep. Genomic coordinates: 91413-93179. EcoCyc protein note: FtsI (penicillin-binding protein 3, PBP3) is believed to be the primary peptidoglycan (PG) transpeptidase which functions together with the SEDS family protein EG10344-MONOMER FtsW to synthesize septal peptidoglycan (sPG) during cell division; FtsW-FtsI are the SEDS-bPBP pair of the divisome. The spatiotemporal coordination of sPG synthesis in E. coli is currently described by a 'two-track' model (see ). FtsI is an essential cell division protein which is present at low abundance (~100 molecules per cell) . Binding of beta-lactam antibiotics to FtsI inhibits FtsI activity and is lethal . FtsI localizes to the division site; localization is dependent on FtsZ, FtsA, FtsQ, FtsL and FtsW, but not EG10341-MONOMER FtsN...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD68|protein.P0AD68]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ftsI; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ftsI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000309,ECOCYC:EG10341,GeneID:944799`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:91413-93179:+; feature_type=gene
