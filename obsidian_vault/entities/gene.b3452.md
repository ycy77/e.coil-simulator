---
entity_id: "gene.b3452"
entity_type: "gene"
name: "ugpA"
source_database: "NCBI RefSeq"
source_id: "gene-b3452"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3452"
  - "ugpA"
---

# ugpA

`gene.b3452`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3452`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ugpA (gene.b3452) is a gene entity. It encodes ugpA (protein.P10905). Encoded protein function: FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304). Probably responsible for the translocation of the substrate across the membrane (Probable). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but it was shown later by Wuttge et al that UgpB does not bind G2P, questioning this transport activity (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304, ECO:0000305}. EcoCyc product frame: UGPA-MONOMER. EcoCyc synonyms: psiB, psiC, ugp. Genomic coordinates: 3590024-3590911. EcoCyc protein note: ugpA encodes one of two predicted inner membrane subunits of an sn-glycerol 3-phosphate and glycerophosphodiester ABC importer.

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), phoB (protein.P0AFJ5). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10905|protein.P10905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ugpA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ugpA; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=ugpA; function=-+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=ugpA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011272,ECOCYC:EG11046,GeneID:947957`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3590024-3590911:-; feature_type=gene
