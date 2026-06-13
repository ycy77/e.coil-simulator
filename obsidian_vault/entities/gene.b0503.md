---
entity_id: "gene.b0503"
entity_type: "gene"
name: "selU"
source_database: "NCBI RefSeq"
source_id: "gene-b0503"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0503"
  - "selU"
---

# selU

`gene.b0503`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0503`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

selU (gene.b0503) is a gene entity. It encodes selU (protein.P33667). Encoded protein function: FUNCTION: Involved in the post-transcriptional modification of the uridine at the wobble position (U34) of tRNA(Lys), tRNA(Glu) and tRNA(Gln) (PubMed:14594807, PubMed:22983156, PubMed:24971911, PubMed:29862510). Catalyzes the conversion of 2-thiouridine (S2U-RNA) to 2-selenouridine (Se2U-RNA) (PubMed:14594807, PubMed:24971911, PubMed:29862510). Acts in a two-step process involving geranylation of 2-thiouridine (S2U) to S-geranyl-2-thiouridine (geS2U) and subsequent selenation of the latter derivative to 2-selenouridine (Se2U) in the tRNA chain (PubMed:24971911, PubMed:29862510). {ECO:0000269|PubMed:14594807, ECO:0000269|PubMed:22983156, ECO:0000269|PubMed:24971911, ECO:0000269|PubMed:29862510}. EcoCyc product frame: EG11768-MONOMER. EcoCyc synonyms: ybbB, mnmH. Genomic coordinates: 530132-531226. EcoCyc protein note: tRNA 2-selenouridine synthase (SelU) is responsible for formation of the special selenium-containing wobble base of the three tRNAs tRNALys, tRNAGlu, and tRNAGln . The enzyme catalyzes formation of 5-methylaminomethyl-2-selenouridine (mnm5se2U) from 5-methylaminomethyl-2-thiouridine and SePO3. Purified SelU was shown to contain tRNA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33667|protein.P33667]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001740,ECOCYC:EG11768,GeneID:947063`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:530132-531226:-; feature_type=gene
