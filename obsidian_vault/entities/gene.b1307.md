---
entity_id: "gene.b1307"
entity_type: "gene"
name: "pspD"
source_database: "NCBI RefSeq"
source_id: "gene-b1307"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1307"
  - "pspD"
---

# pspD

`gene.b1307`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1307`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspD (gene.b1307) is a gene entity. It encodes pspD (protein.P0AFV8). Encoded protein function: FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. {ECO:0000269|PubMed:1712397}. EcoCyc product frame: EG10779-MONOMER. Genomic coordinates: 1369393-1369614. EcoCyc protein note: PspD is a peripheral inner membrane protein . PspA, PspB, and PspC are not observed to cross-link with PspD, whereas PspA, PspB, and PspC form a complex, and PspC is required for PspA to bind to PspB . Multi-copy overexpression of the psp operon increases survival of stress caused by n-hexane treatment . The corresponding psp locus of Yersinia enterocolitica is virulence-related . Regulation has been described . The psp operon shows induction upon phage infection, temperature increase, or exposure to ethanol, osmotic shock , or the organic solvents n-hexane or cyclooctane . Induction is mediated by sigma54, PspB, PspC , PspF , and IHF . Transcription is induced by conditions that cause stress related to energy depletion . Treatment with the drugs diazaborine or cerulenin, which inhibit synthesis of fatty acids and phospholipids, or treatment with globomycin, which disrupts lipoprotein processing, causes transcriptional induction of pspA...

## Biological Role

Activated by pspF (protein.P37344).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFV8|protein.P0AFV8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004394,ECOCYC:EG10779,GeneID:945635`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1369393-1369614:+; feature_type=gene
