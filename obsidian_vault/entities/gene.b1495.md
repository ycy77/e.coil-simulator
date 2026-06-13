---
entity_id: "gene.b1495"
entity_type: "gene"
name: "yddB"
source_database: "NCBI RefSeq"
source_id: "gene-b1495"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1495"
  - "yddB"
---

# yddB

`gene.b1495`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1495`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yddB (gene.b1495) is a gene entity. It encodes yddB (protein.P31827). Encoded protein function: Uncharacterized protein YddB (CDS103) EcoCyc product frame: EG11743-MONOMER. Genomic coordinates: 1575247-1577619. EcoCyc protein note: YddB is an outer membrane protein; YddB forms a 22-strand β-barrel with an N-terminal globular domain that folds into the barrel plugging the pore; the protein contains 11 extracellular loops which are predicted to form an external binding site YddB is a distant homologue of FusA - the TonB-dependent outer membrane receptor of a ferredoxin uptake system (Fus) in plant pathogenic Pectobacterium spp.; YddB is structurally analagous to FusA . yddB is located in a 3 gene cluster with Fus homologs - yddA (fusD) predicted to be encode an inner membrane transporter and and ppqL (fusC) predicted to encode a substrate processing protein ; the cluster may represent a 3-component iron-uptake system . YddB does not support growth during iron limitation in LB media but may have a niche specific role in iron acquisition from a distinct protein substrate . In uropathogenic E. coli (UPEC) strain CFT073, yddB plays a role in fitness during systemic infection in a mammalian host...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31827|protein.P31827]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yddB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004982,ECOCYC:EG11743,GeneID:945961`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1575247-1577619:-; feature_type=gene
