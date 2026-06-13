---
entity_id: "gene.b0996"
entity_type: "gene"
name: "torC"
source_database: "NCBI RefSeq"
source_id: "gene-b0996"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0996"
  - "torC"
---

# torC

`gene.b0996`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0996`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torC (gene.b0996) is a gene entity. It encodes torC (protein.P33226). Encoded protein function: FUNCTION: Part of the anaerobic respiratory chain of trimethylamine-N-oxide reductase TorA which acts by transferring electrons from the membranous menaquinones to TorA (PubMed:11056172, PubMed:39769096). This transfer probably involves an electron transfer pathway from menaquinones to the N-terminal domain of TorC, then from the N-terminus to the C-terminus, and finally to TorA (PubMed:11056172). TorC apocytochrome negatively autoregulates the torCAD operon probably by inhibiting the TorS kinase activity (PubMed:10411745, PubMed:11562502). {ECO:0000269|PubMed:10411745, ECO:0000269|PubMed:11056172, ECO:0000269|PubMed:11562502, ECO:0000269|PubMed:39769096}. EcoCyc product frame: EG11815-MONOMER. Genomic coordinates: 1058084-1059256. EcoCyc protein note: TorC is a pentaheme c-type cytochrome that is anchored to the inner membrane . The protein is predicted to be largely hydrophilic but contains a small stretch of hydrophobic amino acids towards the N-terminus . TorC is required for anaerobic growth in the presence of trimethylamine N-oxide; TorC shuttles electrons from a membrane quinol to TorA in the periplasm...

## Biological Role

Activated by torR (protein.P38684).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33226|protein.P33226]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `C` - regulator=TorR; target=torC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003370,ECOCYC:EG11815,GeneID:946252`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1058084-1059256:+; feature_type=gene
