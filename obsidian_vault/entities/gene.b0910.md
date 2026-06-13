---
entity_id: "gene.b0910"
entity_type: "gene"
name: "cmk"
source_database: "NCBI RefSeq"
source_id: "gene-b0910"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0910"
  - "cmk"
---

# cmk

`gene.b0910`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0910`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cmk (gene.b0910) is a gene entity. It encodes cmk (protein.P0A6I0). Encoded protein function: FUNCTION: ATP, dATP, and GTP are equally effective as phosphate donors. CMP and dCMP are the best phosphate acceptors. {ECO:0000269|PubMed:7836281, ECO:0000269|PubMed:8190075}. EcoCyc product frame: CMPKI-MONOMER. EcoCyc synonyms: ycaF, mssA, ycaG. Genomic coordinates: 961201-961884. EcoCyc protein note: Cytidylate kinase (Cmk) rephosphorylates CMP and dCMP that is produced by the turnover of nucleic acids and CDP diglycerides. Cmk is not an essential enzyme, because CMP is not an intermediate in the de novo pathway for the synthesis of CTP. Unlike the eukaryotic UMP/CMP kinases, this enzyme is specific for CMP or dCMP. Cytidylate kinase affects the rate of 5'-end-dependent mRNA degradation by acting together with DIAMINOPIMEPIM-MONOMER DapF to stimulate the activity of G7459-MONOMER RppH; in addition, by reducing the concentration of CMP in the cell, the synthesis of transcripts beginning with monophosphorylated cytidine is reduced . Cmk appears to have some peptidyl-prolyl cis-trans isomerase activity . Crystal strutures of Cmk have been solved . They dynamic properties of the ATP binding site were probed with a fluorescent dATP analog, and molecular modeling suggested that ATP-mediated induced fit is modulated by CMP binding, which leads to a closed conformation of the active site...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6I0|protein.P0A6I0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cmk; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003101,ECOCYC:EG11265,GeneID:945535`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:961201-961884:+; feature_type=gene
