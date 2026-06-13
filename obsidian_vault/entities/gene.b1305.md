---
entity_id: "gene.b1305"
entity_type: "gene"
name: "pspB"
source_database: "NCBI RefSeq"
source_id: "gene-b1305"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1305"
  - "pspB"
---

# pspB

`gene.b1305`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1305`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspB (gene.b1305) is a gene entity. It encodes pspB (protein.P0AFM9). Encoded protein function: FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspB is involved in transcription regulation. {ECO:0000269|PubMed:1712397}. EcoCyc product frame: EG10777-MONOMER. Genomic coordinates: 1368801-1369025. EcoCyc protein note: PspB and EG10778-MONOMER PspC together act to activate transcription of the TU00326 operon induced by infection with bacteriophage, exposure to ethanol, osmotic shock, or heat shock; PspC is essential for this activation, whereas PspB is not strictly required . PspC and PspB are also reported to be a toxin-antitoxin pair . EG10776-MONOMER PspA, PspB, and EG10778-MONOMER PspC form a complex, and PspC is required for PspA to bind to PspB . PspA, PspB, and PspC are not observed to cross-link with PspD . A pspB mutant exhibits a defect in protein translocation that is suppressed by production of PspA, which plays a role in maintenance of the protonmotive force under certain conditions of cellular stress . Multi-copy overexpression of the TU00326 operon increases survival upon stress caused by n-hexane treatment . The corresponding psp locus of Yersinia enterocolitica is virulence-related . Regulation has been described...

## Biological Role

Activated by pspF (protein.P37344).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFM9|protein.P0AFM9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004389,ECOCYC:EG10777,GeneID:945893`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1368801-1369025:+; feature_type=gene
