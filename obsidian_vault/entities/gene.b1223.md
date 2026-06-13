---
entity_id: "gene.b1223"
entity_type: "gene"
name: "narK"
source_database: "NCBI RefSeq"
source_id: "gene-b1223"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1223"
  - "narK"
---

# narK

`gene.b1223`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1223`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narK (gene.b1223) is a gene entity. It encodes narK (protein.P10903). Encoded protein function: FUNCTION: Catalyzes nitrate uptake, nitrite uptake and nitrite export across the cytoplasmic membrane (PubMed:11967075, PubMed:15667293, PubMed:16804183, PubMed:23665960, PubMed:25959928, PubMed:2668029). Functions as a nitrate/nitrite exchanger, and protons are unlikely to be co-transported (PubMed:15667293, PubMed:23665960, PubMed:25959928, PubMed:2668029). {ECO:0000269|PubMed:11967075, ECO:0000269|PubMed:15667293, ECO:0000269|PubMed:16804183, ECO:0000269|PubMed:23665960, ECO:0000269|PubMed:25959928, ECO:0000269|PubMed:2668029}. EcoCyc product frame: NARK-MONOMER. Genomic coordinates: 1277957-1279348. EcoCyc protein note: NarK is a nitrate/nitrite transporter with a physiological role in nitrate-dependent respiration. NarK mediates the uptake of nitrate and the extrusion of nitrite - the exact mechanism of transport has been debated but structural constraints suggest that NarK functions as a nitrate:nitrite exchanger . Purified NarK, reconstituted in liposomes functions as a nitrate:nitrite antiporter . The location of nitrate and nitrite ions in crystal structures of NarK suggest that the two ions bind to the same site competitively (see also ). Early studies characterizing narK mutant alleles in E. coli K-12 include and...

## Biological Role

Repressed by nac (protein.Q47005). Activated by DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fnr (protein.P0A9E5), narL (protein.P0AF28).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10903|protein.P10903]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=narK; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=narK; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=narK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004111,ECOCYC:EG10642,GeneID:945783`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1277957-1279348:+; feature_type=gene
