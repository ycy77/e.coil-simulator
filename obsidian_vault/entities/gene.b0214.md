---
entity_id: "gene.b0214"
entity_type: "gene"
name: "rnhA"
source_database: "NCBI RefSeq"
source_id: "gene-b0214"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0214"
  - "rnhA"
---

# rnhA

`gene.b0214`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0214`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnhA (gene.b0214) is a gene entity. It encodes rnhA (protein.P0A7Y4). Encoded protein function: FUNCTION: Endonuclease that specifically degrades the RNA of RNA-DNA hybrids. RNase H participates in DNA replication; it helps to specify the origin of genomic replication by suppressing initiation at origins other than the oriC locus; along with the 5'-3' exonuclease of pol1, it removes RNA primers from the Okazaki fragments of lagging strand synthesis; and it defines the origin of replication for ColE1-type plasmids by specific cleavage of an RNA preprimer. Involved in production of retron derived msDNA (a branched RNA linked by a 2',5'-phosphodiester bond to a single-stranded DNA). Strain K12 / MG1655 does not have retrons, however they can be expressed in this strain which requires this enzyme (tested with retron Ec86) (PubMed:7568472). {ECO:0000269|PubMed:7568472}. EcoCyc product frame: EG10860-MONOMER. EcoCyc synonyms: cer, sin, dasF, herA, rnh, sdrA. Genomic coordinates: 235535-236002. EcoCyc protein note: RNase H carries out the endonucleolytic cleavage of RNA in RNA-DNA hybrids, cleaving near the 3' terminus of the RNA and then digesting the remainder of the RNA . Although its physiological functions are not fully understood, it is involved in DNA replication and repair...

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7Y4|protein.P0A7Y4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000717,ECOCYC:EG10860,GeneID:946955`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:235535-236002:-; feature_type=gene
