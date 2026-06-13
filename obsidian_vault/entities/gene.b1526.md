---
entity_id: "gene.b1526"
entity_type: "gene"
name: "ptrR"
source_database: "NCBI RefSeq"
source_id: "gene-b1526"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1526"
  - "ptrR"
---

# ptrR

`gene.b1526`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1526`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptrR (gene.b1526) is a gene entity. It encodes yneJ (protein.P77309). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YneJ EcoCyc product frame: G6812-MONOMER. EcoCyc synonyms: yneJ. Genomic coordinates: 1614804-1615685. EcoCyc protein note: The LysR-type transcriptional regulator PtrR, putrescine utilization regulator, is involved in L-glutamate and putrescine metabolism and in resistance to the tetracycline group of antibiotics . Additionally, was predicted to regulate genes related to iron and succinate oxidation . PtrR contains a helix-turn-helix motif for DNA binding in its N-terminal domain . In systematic studies of oligomerization, it was shown that some members of the LysR family, like PtrR, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . The efficiency of PtrR binding to DNA was found to be more robust in the presence of Gln than Glu or putrescine . Genome-wide PtrR binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium and by ChIP-seq in M9 minimal medium with putrescine and with tryptone . The transcriptional response to the deletion of PtrR was characterized by RNA-seq in M9 minimal medium with Ptr and/or Glu as nitrogen source...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77309|protein.P77309]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005096,ECOCYC:G6812,GeneID:946079`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1614804-1615685:+; feature_type=gene
