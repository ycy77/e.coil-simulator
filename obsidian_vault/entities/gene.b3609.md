---
entity_id: "gene.b3609"
entity_type: "gene"
name: "secB"
source_database: "NCBI RefSeq"
source_id: "gene-b3609"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3609"
  - "secB"
---

# secB

`gene.b3609`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3609`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

secB (gene.b3609) is a gene entity. It encodes secB (protein.P0AG86). Encoded protein function: FUNCTION: One of the proteins required for the normal export of some preproteins out of the cell cytoplasm. It is a molecular chaperone that binds to a subset of precursor proteins, maintaining them in a translocation-competent state. For 2 proteins (MBP, MalE and PhoA) the substrate is wrapped around the homotetramer, which prevents it from folding (PubMed:27501151). It also specifically binds to its receptor SecA. Its substrates include DegP, FhuA, FkpA, GBP, LamB, MalE (MBP), OmpA, OmpF, OmpT, OmpX, OppA, PhoE, TolB, TolC, YbgF, YcgK, YgiW and YncE (PubMed:16352602). {ECO:0000269|PubMed:16352602, ECO:0000269|PubMed:16522795, ECO:0000269|PubMed:27501151}. EcoCyc product frame: SECB. Genomic coordinates: 3783661-3784128.

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG86|protein.P0AG86]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=secB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=secB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011798,ECOCYC:EG10937,GeneID:948123`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3783661-3784128:-; feature_type=gene
