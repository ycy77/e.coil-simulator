---
entity_id: "gene.b3291"
entity_type: "gene"
name: "mscL"
source_database: "NCBI RefSeq"
source_id: "gene-b3291"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3291"
  - "mscL"
---

# mscL

`gene.b3291`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3291`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mscL (gene.b3291) is a gene entity. It encodes mscL (protein.P0A742). Encoded protein function: FUNCTION: Mechanosensitive channel that opens in response to stretch forces in the membrane lipid bilayer. Forms a nonselective ion channel with a conductance of about 4 nanosiemens. Participates in the regulation of osmotic pressure changes within the cell. Opens at a pressure just below that which would cause cell disruption and death. The force required to trigger channel opening depends on the membrane lipids composition. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:23416054, ECO:0000269|PubMed:23875651, ECO:0000269|PubMed:7511799, ECO:0000269|PubMed:9632260}. EcoCyc product frame: EG11180-MONOMER. EcoCyc synonyms: yhdC. Genomic coordinates: 3438024-3438434. EcoCyc protein note: MscL is a mechanosensitive channel of large conductance. MscL converts mechanical tension in the cell membrane into an electrochemical response. Upon osmotic downshift water flows into a cell, increasing pressure on the membrane which activates MscL and allows solutes to exit. MscL acts as a pressure release valve, preventing cell lysis due to increased osmotic pressure. The protein was originally discovered by patch clamp studies on protein fractions reconstituted into liposomes . MscL conductance is 2.5 nanosiemens in E. coli spheroplasts...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A742|protein.P0A742]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mscL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010790,ECOCYC:EG11180,GeneID:947787`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3438024-3438434:+; feature_type=gene
