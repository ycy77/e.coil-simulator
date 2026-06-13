---
entity_id: "gene.b0055"
entity_type: "gene"
name: "djlA"
source_database: "NCBI RefSeq"
source_id: "gene-b0055"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0055"
  - "djlA"
---

# djlA

`gene.b0055`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0055`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

djlA (gene.b0055) is a gene entity. It encodes djlA (protein.P31680). Encoded protein function: FUNCTION: Regulatory DnaK co-chaperone. Direct interaction between DnaK and DjlA is needed for the induction of the wcaABCDE operon, involved in the synthesis of a colanic acid polysaccharide capsule, possibly through activation of the RcsB/RcsC phosphotransfer signaling pathway. The colanic acid capsule may help the bacterium survive conditions outside the host. {ECO:0000255|HAMAP-Rule:MF_01153, ECO:0000269|PubMed:11106641, ECO:0000269|PubMed:11758943, ECO:0000269|PubMed:9364917}. EcoCyc product frame: EG11570-MONOMER. EcoCyc synonyms: yabH. Genomic coordinates: 57364-58179. EcoCyc protein note: DjlA functions as a co-chaperone with DnaK and is implicated in regulating synthesis of the colanic acid capsule. DjlA is located in the inner membrane, with a short N terminal region in the periplasmic space, a single transmembrane dimerization domain , and a large cytoplasmic domain containing a J-domain with similarity to the chaperone DnaJ . The J-domain can functionally substitute for the J-domain of DnaJ . Together with the transmembrane domain, it is essential for stimulation of the synthesis of the colanic acid mucoid capsule via the RcsB/C signal transduction system . DnaK and GrpE as well as direct interaction of DjlA and DnaK are required for this function...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31680|protein.P31680]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000187,ECOCYC:EG11570,GeneID:948992`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:57364-58179:+; feature_type=gene
