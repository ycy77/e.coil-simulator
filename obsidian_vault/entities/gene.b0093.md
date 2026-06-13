---
entity_id: "gene.b0093"
entity_type: "gene"
name: "ftsQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0093"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0093"
  - "ftsQ"
---

# ftsQ

`gene.b0093`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0093`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsQ (gene.b0093) is a gene entity. It encodes ftsQ (protein.P06136). Encoded protein function: FUNCTION: Essential cell division protein. May link together the upstream cell division proteins, which are predominantly cytoplasmic, with the downstream cell division proteins, which are predominantly periplasmic. May control correct divisome assembly. {ECO:0000255|HAMAP-Rule:MF_00911, ECO:0000269|PubMed:17185541, ECO:0000269|PubMed:19233928}. EcoCyc product frame: EG10342-MONOMER. Genomic coordinates: 103155-103985. EcoCyc protein note: FtsQ is an essential cell division protein that is required throughout the process of septum formation; the protein is present in very small amounts of approximately 22 molecules per cell . FtsQ localizes to the division site; the periplasmic domain of FtsQ is necessary and sufficient for correct localization . The cytoplasmic domain and membrane spanning region determine membrane localization, but are not otherwise required for FtsQ function . Localization to the Z ring is dependent on FtsZ, FtsA, ZipA, and FtsK, but not FtsI, FtsL and FtsN . Conversely, FtsL and FtsB require FtsQ for localization to the Z ring . FtsQ, FtsL and FtsB form a complex in vivo even in the absence of FtsK and thus independently of their localization to the septal region...

## Biological Role

Repressed by sdiA (protein.P07026), lrp (protein.P0ACJ0), pdhR (protein.P0ACL9), mraZ (protein.P22186). Activated by sdiA (protein.P07026), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06136|protein.P06136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P07026|protein.P07026]] `RegulonDB` `S` - regulator=SdiA; target=ftsQ; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ftsQ; function=+
- `represses` <-- [[protein.P07026|protein.P07026]] `RegulonDB` `S` - regulator=SdiA; target=ftsQ; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=ftsQ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=ftsQ; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=ftsQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000329,ECOCYC:EG10342,GeneID:944823`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:103155-103985:+; feature_type=gene
