---
entity_id: "gene.b2393"
entity_type: "gene"
name: "nupC"
source_database: "NCBI RefSeq"
source_id: "gene-b2393"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2393"
  - "nupC"
---

# nupC

`gene.b2393`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2393`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nupC (gene.b2393) is a gene entity. It encodes nupC (protein.P0AFF2). Encoded protein function: FUNCTION: Nucleoside transport protein that can transport adenosine, uridine, thymidine, cytidine and deoxycytidine (PubMed:11466294, PubMed:14668133, PubMed:15678184, PubMed:374403). Shows weak activity with inosine and xanthosine (PubMed:11466294, PubMed:14668133). Transport is driven by a proton motive force (PubMed:14668133, PubMed:374403). Does not transport guanosine, deoxyguanosine, hypoxanthine or uracil (PubMed:14668133, PubMed:374403). Also shows activity with the chemotherapeutic drugs 3'-azido-3'-deoxythymidine (AZT), 2',3'- dideoxycytidine (ddC) and 2'-deoxy-2',2'-difluorocytidine (gemcitabine) (PubMed:14668133). {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:14668133, ECO:0000269|PubMed:15678184, ECO:0000269|PubMed:374403}. EcoCyc product frame: NUPC-MONOMER. EcoCyc synonyms: cru. Genomic coordinates: 2513042-2514244. EcoCyc protein note: Early studies in E. coli K-12 reported the presence of two different nucleoside transport systems, one of which (cru/nupC) transports pyrimidine and adenine nucleosides and is inhibited by the nucleoside antibiotic showdomycin, and the other (gru/NUPG-MONOMER nupG) which transports all nucleosides and is not affected by showdomycin...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFF2|protein.P0AFF2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nupC; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=nupC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007893,ECOCYC:EG11971,GeneID:946895`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2513042-2514244:+; feature_type=gene
