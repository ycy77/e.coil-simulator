---
entity_id: "gene.b1451"
entity_type: "gene"
name: "pqqU"
source_database: "NCBI RefSeq"
source_id: "gene-b1451"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1451"
  - "pqqU"
---

# pqqU

`gene.b1451`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1451`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pqqU (gene.b1451) is a gene entity. It encodes pqqU (protein.P76115). Encoded protein function: FUNCTION: Mediates the TonB-dependent high affinity transport across the outer membrane of pyrroloquinoline quinone (PQQ), a redox cofactor required for the activity of Gcd and Asd dehydrogenases (PubMed:36054785). The uptake process is energised via the TonB-ExbBD complex (PubMed:36054785). Not involved in the transport of an iron-containing substrate under laboratory conditions (PubMed:32355044, PubMed:36054785). {ECO:0000269|PubMed:32355044, ECO:0000269|PubMed:36054785}. EcoCyc product frame: G6762-MONOMER. EcoCyc synonyms: yncD. Genomic coordinates: 1520963-1523065. EcoCyc protein note: pqqU (formerly yncD) encodes an outer membrane protein that mediates binding and CPLX0-1923 TonB-dependent active transport of pyrroloquinoline quinone - a redox cofactor required by the dehydrogenases GLUCDEHYDROG-MONOMER Gcd and G6437-MONOMER YliI - across the outer membrane . PqqU supports the growth of a PTS-deficient E. coli strain in glucose minimal medium at low PQQ concentrations (~ 1nmol/L); at higher PQQ concentrations growth of this strain is PqqU-independent possibly due to porin-mediated PQQ diffusion . PqqU is a member of the Outer Membrane Receptor (OMR) family of TonB dependent transporters...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76115|protein.P76115]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=pqqU; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pqqU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004839,ECOCYC:G6762,GeneID:946015`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1520963-1523065:-; feature_type=gene
