---
entity_id: "gene.b0460"
entity_type: "gene"
name: "hha"
source_database: "NCBI RefSeq"
source_id: "gene-b0460"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0460"
  - "hha"
---

# hha

`gene.b0460`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0460`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hha (gene.b0460) is a gene entity. It encodes hha (protein.P0ACE3). Encoded protein function: FUNCTION: Down-regulates hemolysin (hly) expression in complex with H-NS (PubMed:10778755, PubMed:11790731, PubMed:1956303, PubMed:21600204). Stimulates transposition events in vivo (PubMed:8145648). Modifies the set of genes regulated by H-NS; Hha and Cnu (YdgT) increase the number of genes DNA bound by H-NS/StpA and may also modulate the oligomerization of the H-NS/StpA-complex (PubMed:23543115). Binds DNA and influences DNA topology in response to environmental stimuli; does not however interact with DNA in the absence of H-NS (PubMed:23543115). Involved in persister cell formation, acting downstream of mRNA interferase (toxin) MqsR (PubMed:19909729). Decreases biofilm formation by repressing the transcription of fimbrial genes fimA and ihfA, and by repressing the transcription of tRNAs corresponding to rare codons, which are abundant in type 1 fimbrial genes (PubMed:18545668). {ECO:0000269|PubMed:10778755, ECO:0000269|PubMed:11790731, ECO:0000269|PubMed:16317765, ECO:0000269|PubMed:18545668, ECO:0000269|PubMed:1956303, ECO:0000269|PubMed:19909729, ECO:0000269|PubMed:21600204, ECO:0000269|PubMed:23543115, ECO:0000269|PubMed:8145648}. EcoCyc product frame: EG10439-MONOMER. Genomic coordinates: 480090-480308...

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88), basR (protein.P30843).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACE3|protein.P0ACE3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hha; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=hha; function=+
- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=hha; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001594,ECOCYC:EG10439,GeneID:945098`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:480090-480308:-; feature_type=gene
