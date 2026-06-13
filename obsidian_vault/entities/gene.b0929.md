---
entity_id: "gene.b0929"
entity_type: "gene"
name: "ompF"
source_database: "NCBI RefSeq"
source_id: "gene-b0929"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0929"
  - "ompF"
---

# ompF

`gene.b0929`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0929`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompF (gene.b0929) is a gene entity. It encodes ompF (protein.P02931). Encoded protein function: FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane. {ECO:0000305|PubMed:19721064}.; FUNCTION: (Microbial infection) It is also a receptor for the bacteriophage T2. Is the major receptor for colicin E5 (Probable). {ECO:0000305|PubMed:27723824}.; FUNCTION: (Microbial infection) Probably translocates colicin E3 (and other A-type colicins) across the outer membrane (PubMed:18636093). {ECO:0000269|PubMed:18636093}.; FUNCTION: (Microbial infection) A mixed OmpC-OmpF heterotrimer is the outer membrane receptor for toxin CdiA-EC536 (ECL_04451); polymorphisms in extracellular loops 4 and 5 of OmpC confer susceptibility to CdiA-EC536-mediated toxicity. {ECO:0000269|PubMed:27723824}. EcoCyc product frame: EG10671-MONOMER. EcoCyc synonyms: nfxB, tolF, cmlB, cry. Genomic coordinates: 985894-986982. EcoCyc protein note: OmpF is a general outer membrane (OM) porin which mediates the non-specific diffusion of small solutes such as sugars, ions and amino acids. The major non-specific OM porins of E. coli K-12 (OmpF and CPLX0-7533 "OmpC") are typically defined by an exclusion limit based on substrate mass (~600 daltons) but there are large differences in penetration rates within solutes due to factors such as size, hydrophobicity and charge (discussed in )...

## Biological Role

Repressed by rybB (gene.b4417), ompR (protein.P0AA16), cpxR (protein.P0AE88), nac (protein.Q47005). Activated by ompR (protein.P0AA16), nac (protein.Q47005).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02931|protein.P02931]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=ompF; function=-+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=ompF; function=-
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=ompF; function=-+
- `represses` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=ompF; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003153,ECOCYC:EG10671,GeneID:945554`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:985894-986982:-; feature_type=gene
