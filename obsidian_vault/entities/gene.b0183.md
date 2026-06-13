---
entity_id: "gene.b0183"
entity_type: "gene"
name: "rnhB"
source_database: "NCBI RefSeq"
source_id: "gene-b0183"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0183"
  - "rnhB"
---

# rnhB

`gene.b0183`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0183`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnhB (gene.b0183) is a gene entity. It encodes rnhB (protein.P10442). Encoded protein function: FUNCTION: Endonuclease that specifically degrades the RNA of RNA-DNA hybrids. {ECO:0000250, ECO:0000269|PubMed:2172991}. EcoCyc product frame: EG10861-MONOMER. Genomic coordinates: 204493-205089. EcoCyc protein note: RNase HII (type 2 RNase H) cleaves RNA in RNA-DNA hybrids by nicking DNA 5' to the incorporated ribonucleotide . RNase HII is required for removal of misincorporated ribose from DNA . A second RNase with a similar structure and catalytic mechanism is encoded by gene EG10860 which produces RNase HI (type 1 RNase H). RNase HII has also been reported to have junction RNase activity, cleaving RNA-DNADNA and RNA-DNARNA duplexes at the 5' side of the last ribonulceotide at the RNA-DNA junction . In vivo studies show that RNase HII targets isolated mispaired ribonucleoside monophosphates within chromosomal DNA in competition with the mismatch repair system, whereas RNase HI targets a mismatch within an RNA-DNA heteroduplex. RNase HII efficiently targets a single mispaired ribonucleoside monophosphate, whereas RNase HI targets a tract of five ribonucleoside monophosphates with a mispair . Genetic and biochemical evidence suggest that RNase HII initiates the ribonucleotide excision repair process, followed by DNA polymerase I . In an E...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10442|protein.P10442]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rnhB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000622,ECOCYC:EG10861,GeneID:944852`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:204493-205089:+; feature_type=gene
