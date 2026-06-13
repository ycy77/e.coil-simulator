---
entity_id: "gene.b1306"
entity_type: "gene"
name: "pspC"
source_database: "NCBI RefSeq"
source_id: "gene-b1306"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1306"
  - "pspC"
---

# pspC

`gene.b1306`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1306`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspC (gene.b1306) is a gene entity. It encodes pspC (protein.P0AFN2). Encoded protein function: FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspC is involved in transcription regulation. {ECO:0000269|PubMed:1712397}. EcoCyc product frame: EG10778-MONOMER. Genomic coordinates: 1369025-1369384. EcoCyc protein note: PspC is a positive regulator of the TU00326 operon expression . EG10777-MONOMER PspB and PspC together act to activate expression of the psp operon in response to infection with bacteriophage, exposure to ethanol, osmotic shock, and heat shock; PspC is essential for this activation, whereas PspB is not strictly required . PspC appears to be required for PspB to interact with PspA . PspC is also reported as the toxin of a potential PspC-PspB toxin-antitoxin pair . The intramembrane protease FtsH destabilizes PspC . PspC is an inner membrane protein that is proposed to consist of an N-terminal cytoplasmic domain, a central transmembrane domain (residues 40-68), and a C-terminal periplasmic domain with a leucine zipper motif . A conserved glycine residue at position 48 is required for PspC function...

## Biological Role

Activated by pspF (protein.P37344).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFN2|protein.P0AFN2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004391,ECOCYC:EG10778,GeneID:945499`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1369025-1369384:+; feature_type=gene
