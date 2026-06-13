---
entity_id: "gene.b3604"
entity_type: "gene"
name: "lldR"
source_database: "NCBI RefSeq"
source_id: "gene-b3604"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3604"
  - "lldR"
---

# lldR

`gene.b3604`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3604`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lldR (gene.b3604) is a gene entity. It encodes lldR (protein.P0ACL7). Encoded protein function: FUNCTION: May be a regulatory protein for the LCT genes. EcoCyc product frame: EG11962-MONOMER. EcoCyc synonyms: lct, lctR. Genomic coordinates: 3779054-3779830. EcoCyc protein note: LldR, formerly named "lactate regulator," is a transcription factor that controls expression of genes involved in transport and catabolism of L-lactate and genes involved in acid stress . This regulator has a dual function and is positively and negatively autoregulated. In the absence of L-lactate and under anaerobic conditions, this regulator represses the transcription of the lldPRD operon . In this repression system, LldR binds to two operators and probably leads to repressor DNA looping . Expression of this regulator is also stimulated in the presence of L-lactate, and this inductor promotes a conformational change that probably destabilizes the DNA loop, promoting the transcription open complex . Both L-lactate and D-lactate are able to bind to LldR to regulate its activity . At a low concentration of the effector, LldR binds to the target sequence, but at high concentration it is dissociated . The affinity of LldR is greater in the lldPRD operon regulatory region than in other targets (genes related to acid stress) of this regulator...

## Biological Role

Repressed by arcA (protein.P0A9Q1), lldR (protein.P0ACL7). Activated by rpoD (protein.P00579), lldR (protein.P0ACL7).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACL7|protein.P0ACL7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lldR; function=+
- `activates` <-- [[protein.P0ACL7|protein.P0ACL7]] `RegulonDB` `C` - regulator=LldR; target=lldR; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=lldR; function=-
- `represses` <-- [[protein.P0ACL7|protein.P0ACL7]] `RegulonDB` `C` - regulator=LldR; target=lldR; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011782,ECOCYC:EG11962,GeneID:948122`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3779054-3779830:+; feature_type=gene
