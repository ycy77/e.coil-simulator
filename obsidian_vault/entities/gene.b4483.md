---
entity_id: "gene.b4483"
entity_type: "gene"
name: "tatD"
source_database: "NCBI RefSeq"
source_id: "gene-b4483"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4483"
  - "tatD"
---

# tatD

`gene.b4483`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4483`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tatD (gene.b4483) is a gene entity. It encodes tatD (protein.P27859). Encoded protein function: FUNCTION: 3'-5' exonuclease that prefers single-stranded DNA and RNA. May play a role in the H(2)O(2)-induced DNA damage repair. {ECO:0000255|HAMAP-Rule:MF_00901, ECO:0000269|PubMed:10747959, ECO:0000269|PubMed:25114049}. EcoCyc product frame: EG11481-MONOMER. EcoCyc synonyms: b3841, yigX, b3840, mttC, yigW. Genomic coordinates: 4023554-4024336. EcoCyc protein note: TatD is a magnesium dependent 3' - 5' exonuclease with a preference for single strand DNA and RNA. A tatD knockout mutant is more sensitive to H2O2 than wild type. Purified TatD has efficient exonuclease activity on ssDNA containing a 3' terminal deaminated base (uracil or hypoxanthine). TatD may be involved in the repair of H2O2 induced DNA damage . Purified, crystallised TatD has a TIM barrel fold (an eight stranded α β barrel). The conserved residues Glu91, Glu201 and Asp 203 are involved in metal binding at the active site . TatD exhibits magnesium-dependent DNase activity . A tatD mutant shows increased RecA-GFP foci formation . Deletion of tatD has very little effect on growth . A tatD ycfH yjjV triple mutant does not exhibit phenotypes that would suggest involvement of the corresponding proteins in the Sec-independent Tat protein export system...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27859|protein.P27859]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0174116,ECOCYC:EG11481,GeneID:2847752`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4023554-4024336:+; feature_type=gene
