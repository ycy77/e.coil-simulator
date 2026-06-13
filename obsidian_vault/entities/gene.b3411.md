---
entity_id: "gene.b3411"
entity_type: "gene"
name: "rpnA"
source_database: "NCBI RefSeq"
source_id: "gene-b3411"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3411"
  - "rpnA"
---

# rpnA

`gene.b3411`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3411`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpnA (gene.b3411) is a gene entity. It encodes rpnA (protein.P31667). Encoded protein function: FUNCTION: A low activity DNA endonuclease yielding 3'-hydroxyl ends, equally active on ss or dsDNA, not active on dsRNA (PubMed:28096446). Shows no sequence specificity (PubMed:28096446). Upon expression enhances RecA-independent DNA recombination 49-fold, concomitantly reducing viability by 88% and probably inducing DNA damage as measured by induction of the SOS repair response in RecA cells (PubMed:28096446). RecA-independent DNA recombination leads to replacement of recipient genes with large segments of donor DNA rather than DNA addition to the donor strain; increased expression of RpnA leads to smaller replacement segments, suggesting this protein may play a role in generating crossover events (PubMed:28096446). {ECO:0000269|PubMed:28096446}. EcoCyc product frame: EG11750-MONOMER. EcoCyc synonyms: yhgA. Genomic coordinates: 3543167-3544045. EcoCyc protein note: In vitro, the RpnA protein has Mg2+-dependent nonspecific DNA endonuclease activity that is stimulated by Ca2+ . RpnA is one of five proteins in E. coli that belong to the "transposase_31" family , which is distantly related to the PD-(D/E)XK nuclease superfamily . It was previously noted that RpnA has similarity to RpnC, which is encoded within the panBCD gene cluster...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31667|protein.P31667]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011134,ECOCYC:EG11750,GeneID:947917`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3543167-3544045:+; feature_type=gene
