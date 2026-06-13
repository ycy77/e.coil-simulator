---
entity_id: "gene.b0443"
entity_type: "gene"
name: "fadM"
source_database: "NCBI RefSeq"
source_id: "gene-b0443"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0443"
  - "fadM"
---

# fadM

`gene.b0443`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0443`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadM (gene.b0443) is a gene entity. It encodes fadM (protein.P77712). Encoded protein function: FUNCTION: Long-chain acyl-CoA thioesterase that could be involved in beta-oxidation of fatty acids (PubMed:18576672). Is most active with 3,5-tetradecadienoyl-CoA, a metabolite of oleic acid that is hydrolyzed during oleate beta-oxidation, but can also use other substrates such as 3,5-dodecadienoyl-CoA, 9-cis-octadecenoyl-CoA, octadecanoyl-CoA, hexadecanoyl-CoA, 3-hydroxytetradecanoyl-CoA and tetradecanoyl-CoA (PubMed:18576672). {ECO:0000269|PubMed:18576672}. EcoCyc product frame: G6244-MONOMER. EcoCyc synonyms: ybaW, tesC. Genomic coordinates: 464402-464800. EcoCyc protein note: Thioesterase III (FadM) is a long-chain acyl-CoA thioesterase that is involved in the β-oxidation of oleic acid. The enzyme is able to hydrolyze a number of related substrates. The best substrate is 3,5-tetradecadienoyl-CoA, which is a minor side product of oleate β-oxidation that is resistant to further degradation. The hydrolysis product, 3,5-tetradecadienoate, is released into the growth medium . Thioesterase III is expressed upon growth on oleic acid as the sole source of carbon . fadM is a member of the fad regulon; expression is induced by a number of fatty acids, with C18:1 as the best inducer...

## Biological Role

Activated by pdhR (protein.P0ACL9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77712|protein.P77712]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACL9|protein.P0ACL9]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001537,ECOCYC:G6244,GeneID:945812`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:464402-464800:+; feature_type=gene
