---
entity_id: "gene.b2526"
entity_type: "gene"
name: "hscA"
source_database: "NCBI RefSeq"
source_id: "gene-b2526"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2526"
  - "hscA"
---

# hscA

`gene.b2526`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2526`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hscA (gene.b2526) is a gene entity. It encodes hscA (protein.P0A6Z1). Encoded protein function: FUNCTION: Chaperone involved in the maturation of iron-sulfur cluster-containing proteins. Has a low intrinsic ATPase activity which is markedly stimulated by HscB. Involved in the maturation of IscU. EcoCyc product frame: EG12130-MONOMER. EcoCyc synonyms: hsc. Genomic coordinates: 2657085-2658935. EcoCyc protein note: HscA together with HscB comprises a chaperone/cochaperone system similar to DnaK/DnaJ . HscA is required for the assembly of iron-sulfur clusters . Models for chaperone-facilitated Fe-S cluster transfer have been proposed. One model involves an exchange of Fe-S cluster ligands in the iron-sulfur cluster scaffold protein G7324-MONOMER IscU upon chaperone binding that facilitates cluster transfer ; another involves chaperone-mediated disordering of IscU that promotes the transfer of the Fe-S cluster to an acceptor protein . HscA consists of two domains, a nucleotide-binding domain (NBD) that binds and hydrolyzes ATP and a substrate-binding domain that binds IscU . The inter-domain linker peptide is able to stimulate the rate of ATP hydrolysis of the isolated NBD . Under steady-state conditions, ATP hydrolysis rather than ADP/ATP nucleotide exchange is the rate-limiting step in the HscA reaction cycle ; the dissociation rates for ATP and ADP are comparatively fast...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Z1|protein.P0A6Z1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=hscA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008315,ECOCYC:EG12130,GeneID:944885`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2657085-2658935:-; feature_type=gene
