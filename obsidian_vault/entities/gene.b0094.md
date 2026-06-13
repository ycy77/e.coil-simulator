---
entity_id: "gene.b0094"
entity_type: "gene"
name: "ftsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0094"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0094"
  - "ftsA"
---

# ftsA

`gene.b0094`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0094`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsA (gene.b0094) is a gene entity. It encodes ftsA (protein.P0ABH0). Encoded protein function: FUNCTION: Essential cell division protein that assists in the assembly of the Z ring (PubMed:11847116). May serve as the principal membrane anchor for the Z ring (PubMed:15752196). Also required for the recruitment to the septal ring of the downstream cell division proteins FtsK, FtsQ, FtsL, FtsI and FtsN (PubMed:10027987, PubMed:24750258, PubMed:9282742, PubMed:9495771, PubMed:9603865, PubMed:9882666). Binds ATP (PubMed:11053380). {ECO:0000269|PubMed:10027987, ECO:0000269|PubMed:11053380, ECO:0000269|PubMed:11847116, ECO:0000269|PubMed:15752196, ECO:0000269|PubMed:24750258, ECO:0000269|PubMed:9282742, ECO:0000269|PubMed:9495771, ECO:0000269|PubMed:9603865, ECO:0000269|PubMed:9882666}. EcoCyc product frame: EG10339-MONOMER. EcoCyc synonyms: divA. Genomic coordinates: 103982-105244. EcoCyc protein note: EG10339-MONOMER FtsA is an essential cell division protein which colocalizes with EG10347-MONOMER to the septal ring structure; localization is FtsZ-dependent . Both FtsA and G7258-MONOMER recruit ABC-54-CPLX and G6464-MONOMER , and thus other cell division proteins downstream, to the Z ring. However, premature targeting of cell division proteins to mid-cell allows recruitment of other members of the cell division machinery even in the absence of FtsA...

## Biological Role

Repressed by sdiA (protein.P07026), pdhR (protein.P0ACL9), mraZ (protein.P22186). Activated by rcsB (protein.P0DMC7), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABH0|protein.P0ABH0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `S` - regulator=RcsB; target=ftsA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ftsA; function=+
- `represses` <-- [[protein.P07026|protein.P07026]] `RegulonDB` `S` - regulator=SdiA; target=ftsA; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ftsA; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ftsA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000331,ECOCYC:EG10339,GeneID:944778`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:103982-105244:+; feature_type=gene
