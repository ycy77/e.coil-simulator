---
entity_id: "gene.b2527"
entity_type: "gene"
name: "hscB"
source_database: "NCBI RefSeq"
source_id: "gene-b2527"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2527"
  - "hscB"
---

# hscB

`gene.b2527`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2527`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hscB (gene.b2527) is a gene entity. It encodes hscB (protein.P0A6L9). Encoded protein function: FUNCTION: Co-chaperone involved in the maturation of iron-sulfur cluster-containing proteins. Seems to help targeting proteins to be folded toward HscA. EcoCyc product frame: EG12131-MONOMER. EcoCyc synonyms: yfhE. Genomic coordinates: 2658952-2659467. EcoCyc protein note: The EG12130-MONOMER together with EG12131-MONOMER comprises a chaperone/cochaperone system similar to DnaK/DnaJ that is involved in iron-sulfur cluster assembly . Models for chaperone-facilitated Fe-S cluster transfer have been proposed. One model involves an exchange of Fe-S cluster ligands in the iron-sulfur cluster scaffold protein G7324-MONOMER IscU upon chaperone binding that facilitates cluster transfer ; another involves chaperone-mediated disordering of IscU that promotes the transfer of the Fe-S cluster to an acceptor protein . A crystal structure of HscB has been solved at 1.8 Å resolution . HscB consists of an N-terminal J-domain that is similar to the J-domain of DnaJ, and a compact three-helix bundle C-terminal domain . A solution structure indicates that the crystal structure is representative of the solution state . HscB is a co-chaperone that stimulates HscA (Hsc66) ATPase activity . HscB physically interacts with HscA and with IscU and aids in targeting IscU to HscA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6L9|protein.P0A6L9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008317,ECOCYC:EG12131,GeneID:946995`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2658952-2659467:-; feature_type=gene
